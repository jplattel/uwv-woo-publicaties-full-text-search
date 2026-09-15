from __future__ import annotations

import unittest
from pathlib import Path

from src.config import load_settings
from src.crawl import parse_listing_seed


LISTING_HTML = """
<html>
  <mdgs-dynamic-list
    fetch-results="/api/overview/nl/wet-open-overheid/publicaties/woo-publicaties"
    entry-id="/nl/wet-open-overheid/publicaties/woo-publicaties)"
    first-results='{"results":[{"date":"2026-09-03T22:00:00Z","type":"WOO publicatie","title":"Newest decision","url":"/nl/wet-open-overheid/woo-publicaties/2026/newest-decision"},{"date":"2026-08-16T22:00:00Z","type":"WOO publicatie","title":"Second newest","url":"/nl/wet-open-overheid/woo-publicaties/2026/second-newest"}]}'>
  </mdgs-dynamic-list>
</html>
"""


class ParseListingSeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.settings = load_settings(Path("config/sources.yml"), data_dir=Path("data"))

    def test_reads_newest_results_and_entry_id(self) -> None:
        publications, entry_id = parse_listing_seed(LISTING_HTML, self.settings)
        self.assertEqual(entry_id, "/nl/wet-open-overheid/publicaties/woo-publicaties)")
        self.assertEqual(
            [item.title for item in publications],
            ["Newest decision", "Second newest"],
        )
        self.assertEqual(publications[0].date, "2026-09-03T22:00:00Z")
        self.assertTrue(publications[0].url.startswith("https://www.uwv.nl/"))

    def test_missing_widget_returns_empty(self) -> None:
        publications, entry_id = parse_listing_seed("<html></html>", self.settings)
        self.assertEqual(publications, [])
        self.assertEqual(entry_id, "")


if __name__ == "__main__":
    unittest.main()
