from __future__ import annotations

import logging
import os
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pdfplumber
from pdf2image import convert_from_path


@dataclass(frozen=True)
class Block:
    type: str
    page: int
    bbox: list[float]
    text: str
    source: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "type": self.type,
            "page": self.page,
            "bbox": self.bbox,
            "text": self.text,
            "source": self.source,
        }


@dataclass(frozen=True)
class ExtractionResult:
    blocks: list[Block]
    page_count: int
    ocr_used: bool


@contextmanager
def _quiet_pdf_parsing():
    loggers = [
        logging.getLogger("pdfminer"),
        logging.getLogger("pdfplumber"),
    ]
    previous_levels = [logger.level for logger in loggers]
    for logger in loggers:
        logger.setLevel(logging.ERROR)
    try:
        yield
    finally:
        for logger, level in zip(loggers, previous_levels, strict=True):
            logger.setLevel(level)


def _classify_block(text: str, height: float, avg_height: float) -> str:
    stripped = text.strip()
    if not stripped:
        return "empty"
    if height >= avg_height * 1.35 and len(stripped) <= 120:
        return "heading"
    if stripped.isupper() and len(stripped.split()) <= 12:
        return "heading"
    return "paragraph"


def _group_words_to_blocks(words: list[dict[str, Any]], page_num: int, source: str) -> list[Block]:
    if not words:
        return []

    heights = [max(word["bottom"] - word["top"], 1.0) for word in words]
    avg_height = sum(heights) / len(heights)

    lines: dict[tuple[int, float], list[dict[str, Any]]] = {}
    for word in words:
        key = (round(word["top"], 1), round(word.get("size", word["bottom"] - word["top"]), 1))
        lines.setdefault(key, []).append(word)

    blocks: list[Block] = []
    for _, line_words in sorted(lines.items(), key=lambda item: (item[0][0], item[0][1])):
        line_words = sorted(line_words, key=lambda word: word["x0"])
        text = " ".join(word["text"] for word in line_words).strip()
        if not text:
            continue
        x0 = min(word["x0"] for word in line_words)
        y0 = min(word["top"] for word in line_words)
        x1 = max(word["x1"] for word in line_words)
        y1 = max(word["bottom"] for word in line_words)
        height = max(y1 - y0, 1.0)
        blocks.append(
            Block(
                type=_classify_block(text, height, avg_height),
                page=page_num,
                bbox=[round(x0, 2), round(y0, 2), round(x1, 2), round(y1, 2)],
                text=text,
                source=source,
            )
        )

    return blocks


def _extract_text_layer_blocks(page, page_num: int) -> list[Block]:
    words = page.extract_words(use_text_flow=True, keep_blank_chars=False) or []
    normalized = []
    for word in words:
        text = (word.get("text") or "").strip()
        if not text:
            continue
        normalized.append(
            {
                "text": text,
                "x0": float(word["x0"]),
                "x1": float(word["x1"]),
                "top": float(word["top"]),
                "bottom": float(word["bottom"]),
                "size": float(word.get("size") or (word["bottom"] - word["top"])),
            }
        )
    return _group_words_to_blocks(normalized, page_num, "text")


# Tesseract used ISO 639-2 codes. PaddleOCR 3.x uses its own short codes.
_PADDLE_LANG_ALIASES = {
    "nld": "nl",
    "dut": "nl",
    "dutch": "nl",
    "eng": "en",
    "deu": "de",
    "ger": "de",
}

_paddle_engine: Any = None
_paddle_engine_lang: str | None = None


def paddle_lang(ocr_lang: str) -> str:
    key = (ocr_lang or "nl").strip().lower()
    return _PADDLE_LANG_ALIASES.get(key, key)


def _as_rows(value: Any) -> list[Any]:
    if value is None:
        return []
    if hasattr(value, "tolist"):
        value = value.tolist()
    return list(value)


def blocks_from_paddle_result(page_num: int, result: Any, min_score: float = 0.5) -> list[Block]:
    """Turn one PaddleOCR page result into line blocks."""
    texts = _as_rows(result["rec_texts"] if result is not None else None)
    scores = _as_rows(result["rec_scores"] if result is not None else None)
    boxes = _as_rows(result["rec_boxes"] if result is not None else None)
    if not texts:
        return []

    lines: list[tuple[float, float, float, float, float, str]] = []
    for index, text in enumerate(texts):
        cleaned = (text or "").strip()
        if not cleaned:
            continue
        score = float(scores[index]) if index < len(scores) else 1.0
        if score < min_score:
            continue
        if index >= len(boxes):
            continue
        box = _as_rows(boxes[index])
        if len(box) < 4:
            continue
        x0, y0, x1, y1 = (float(box[0]), float(box[1]), float(box[2]), float(box[3]))
        lines.append((y0, x0, x1, y1, score, cleaned))

    if not lines:
        return []

    lines.sort(key=lambda item: (item[0], item[1]))
    heights = [max(item[3] - item[0], 1.0) for item in lines]
    avg_height = sum(heights) / len(heights)
    blocks: list[Block] = []
    for y0, x0, x1, y1, _score, text in lines:
        height = max(y1 - y0, 1.0)
        blocks.append(
            Block(
                type=_classify_block(text, height, avg_height),
                page=page_num,
                bbox=[round(x0, 2), round(y0, 2), round(x1, 2), round(y1, 2)],
                text=text,
                source="ocr",
            )
        )
    return blocks


def _get_paddle_engine(ocr_lang: str) -> Any:
    global _paddle_engine, _paddle_engine_lang
    lang = paddle_lang(ocr_lang)
    if _paddle_engine is not None and _paddle_engine_lang == lang:
        return _paddle_engine

    os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")
    from paddleocr import PaddleOCR

    _paddle_engine = PaddleOCR(
        lang=lang,
        engine="onnxruntime",
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=True,
        text_rec_score_thresh=0.5,
    )
    _paddle_engine_lang = lang
    return _paddle_engine


def _image_to_array(image: Any) -> Any:
    import numpy as np

    if hasattr(image, "convert"):
        image = image.convert("RGB")
    return np.asarray(image)


def _extract_ocr_blocks(image, page_num: int, ocr_lang: str) -> list[Block]:
    engine = _get_paddle_engine(ocr_lang)
    predicted = engine.predict(_image_to_array(image))
    pages = list(predicted or [])
    if not pages:
        return []
    return blocks_from_paddle_result(page_num, pages[0])


def extract_pdf(
    pdf_path: Path,
    ocr_lang: str = "nld",
    min_chars_per_page: int = 40,
) -> ExtractionResult:
    blocks: list[Block] = []
    ocr_used = False

    with _quiet_pdf_parsing(), pdfplumber.open(pdf_path) as pdf:
        page_count = len(pdf.pages)
        images = None

        for index, page in enumerate(pdf.pages, start=1):
            page_blocks = _extract_text_layer_blocks(page, index)
            text_chars = sum(len(block.text) for block in page_blocks)

            if text_chars < min_chars_per_page:
                if images is None:
                    images = convert_from_path(str(pdf_path))
                image = images[index - 1]
                page_blocks = _extract_ocr_blocks(image, index, ocr_lang)
                ocr_used = True

            blocks.extend(block for block in page_blocks if block.type != "empty")

    return ExtractionResult(blocks=blocks, page_count=page_count, ocr_used=ocr_used)
