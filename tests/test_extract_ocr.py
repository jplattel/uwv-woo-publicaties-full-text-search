from __future__ import annotations

import unittest
from unittest.mock import patch

from src.extract import (
    blocks_from_paddle_result,
    extract_pdf,
    paddle_lang,
)


class PaddleLanguageTests(unittest.TestCase):
    def test_tesseract_dutch_code_maps_to_paddle(self) -> None:
        self.assertEqual(paddle_lang("nld"), "nl")
        self.assertEqual(paddle_lang("NL"), "nl")
        self.assertEqual(paddle_lang("en"), "en")


class PaddleResultTests(unittest.TestCase):
    def test_lines_become_ordered_ocr_blocks(self) -> None:
        blocks = blocks_from_paddle_result(
            2,
            {
                "rec_texts": ["onderaan", "BESLUIT", "ruis"],
                "rec_scores": [0.91, 0.95, 0.2],
                "rec_boxes": [[10, 80, 90, 96], [10, 20, 80, 40], [0, 0, 4, 4]],
            },
        )

        self.assertEqual([block.text for block in blocks], ["BESLUIT", "onderaan"])
        self.assertEqual(blocks[0].page, 2)
        self.assertEqual(blocks[0].source, "ocr")
        self.assertEqual(blocks[0].bbox, [10.0, 20.0, 80.0, 40.0])
        self.assertEqual(blocks[0].type, "heading")

    def test_empty_page_returns_no_blocks(self) -> None:
        self.assertEqual(
            blocks_from_paddle_result(1, {"rec_texts": [], "rec_scores": [], "rec_boxes": []}),
            [],
        )


class ExtractFallbackTests(unittest.TestCase):
    def test_short_text_layer_uses_paddleocr(self) -> None:
        class FakePage:
            def extract_words(self, **_kwargs):
                return []

        class FakePdf:
            pages = [FakePage()]

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

        calls: list[str] = []

        def fake_ocr(image, page_num, ocr_lang):
            calls.append(ocr_lang)
            from src.extract import Block

            return [
                Block(
                    type="paragraph",
                    page=page_num,
                    bbox=[1, 2, 3, 4],
                    text="gelezen met paddle",
                    source="ocr",
                )
            ]

        with (
            patch("src.extract.pdfplumber.open", return_value=FakePdf()),
            patch("src.extract.convert_from_path", return_value=["image"]),
            patch("src.extract._extract_ocr_blocks", side_effect=fake_ocr),
        ):
            result = extract_pdf("unused.pdf", ocr_lang="nld", min_chars_per_page=40)

        self.assertTrue(result.ocr_used)
        self.assertEqual(result.page_count, 1)
        self.assertEqual(result.blocks[0].text, "gelezen met paddle")
        self.assertEqual(calls, ["nld"])


if __name__ == "__main__":
    unittest.main()
