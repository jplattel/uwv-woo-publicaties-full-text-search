from __future__ import annotations

import logging
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from pytesseract import Output


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


def _extract_ocr_blocks(image, page_num: int, ocr_lang: str) -> list[Block]:
    data = pytesseract.image_to_data(image, lang=ocr_lang, output_type=Output.DICT)
    words: list[dict[str, Any]] = []
    count = len(data["text"])

    for index in range(count):
        text = (data["text"][index] or "").strip()
        if not text or int(data["conf"][index]) < 0:
            continue
        words.append(
            {
                "text": text,
                "x0": float(data["left"][index]),
                "x1": float(data["left"][index] + data["width"][index]),
                "top": float(data["top"][index]),
                "bottom": float(data["top"][index] + data["height"][index]),
                "size": float(data["height"][index]),
                "block_num": int(data["block_num"][index]),
                "par_num": int(data["par_num"][index]),
                "line_num": int(data["line_num"][index]),
            }
        )

    if not words:
        return []

    heights = [max(word["bottom"] - word["top"], 1.0) for word in words]
    avg_height = sum(heights) / len(heights)

    lines: dict[tuple[int, int, int], list[dict[str, Any]]] = {}
    for word in words:
        key = (word["block_num"], word["par_num"], word["line_num"])
        lines.setdefault(key, []).append(word)

    blocks: list[Block] = []
    for key in sorted(lines.keys()):
        line_words = sorted(lines[key], key=lambda word: word["x0"])
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
                source="ocr",
            )
        )

    return blocks


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
