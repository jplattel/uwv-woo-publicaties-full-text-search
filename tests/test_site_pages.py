from __future__ import annotations

import unittest

from scripts.build_site import (
    build_publications,
    find_duplicate_groups,
    is_besluit_document,
    order_publication_documents,
    render_doc_page,
    render_extracted_text,
    render_internal_dashboard,
    render_publications_page,
    render_statistics_page,
    search_build_id,
)


class PublicationOrderTests(unittest.TestCase):
    def test_besluit_stays_first_without_reshuffling_the_rest(self) -> None:
        documents = [
            {"label": "Bijlage 2", "url": "doc/a/bijlage-2.html"},
            {"label": "Bijlage 1", "url": "doc/a/bijlage-1.html"},
            {"label": "Woo-besluit", "url": "doc/a/woo-besluit.html"},
            {"label": "Nota", "url": "doc/a/nota.html"},
        ]

        ordered = order_publication_documents(documents)

        self.assertEqual(
            [item["label"] for item in ordered],
            ["Woo-besluit", "Bijlage 2", "Bijlage 1", "Nota"],
        )
        self.assertTrue(is_besluit_document(documents[2]))
        self.assertFalse(is_besluit_document(documents[0]))

    def test_publication_folder_name_does_not_count_as_the_decision(self) -> None:
        documents = [
            {
                "label": "Bijlage",
                "url": "doc/2026-01-01-woo-besluit-foo/bijlage.html",
            },
            {
                "label": "Nota",
                "url": "doc/2026-01-01-woo-besluit-foo/nota.html",
            },
            {
                "label": "Woo-besluit",
                "url": "doc/2026-01-01-woo-besluit-foo/woo-besluit.html",
            },
        ]

        ordered = order_publication_documents(documents)

        self.assertEqual(
            [item["label"] for item in ordered],
            ["Woo-besluit", "Bijlage", "Nota"],
        )

    def test_bijlage_that_mentions_besluit_stays_in_source_order(self) -> None:
        documents = [
            {
                "label": "Bijlage 1 bij besluit Wob-verzoek",
                "url": "doc/x/bijlage-1.html",
            },
            {"label": "Bijlage 2", "url": "doc/x/bijlage-2.html"},
            {"label": "Besluit Wob-verzoek", "url": "doc/x/besluit.html"},
        ]

        ordered = order_publication_documents(documents)

        self.assertEqual(
            [item["label"] for item in ordered],
            ["Besluit Wob-verzoek", "Bijlage 1 bij besluit Wob-verzoek", "Bijlage 2"],
        )

    def test_supporting_documents_that_mention_besluit_stay_behind_the_letter(self) -> None:
        documents = [
            {
                "label": "Herziening intrekking beslissing afhandelen",
                "url": "doc/pub/2026-08-04-herziening-intrekking-beslissing-afhandelen-handboek.html",
            },
            {
                "label": "Inventarislijst bij Woo-besluit 2025014",
                "url": "doc/pub/2025-08-25-woo-besluit-2025014-inventarislijst.html",
            },
            {
                "label": "Woo-besluit 2026068",
                "url": "doc/pub/2026-08-04-woo-besluit-2026068.html",
            },
            {
                "label": "Afhandelen terugvordering",
                "url": "doc/pub/2026-08-04-afhandelen-terugvordering.html",
            },
        ]

        ordered = order_publication_documents(documents)

        self.assertEqual(
            [item["label"] for item in ordered],
            [
                "Woo-besluit 2026068",
                "Herziening intrekking beslissing afhandelen",
                "Inventarislijst bij Woo-besluit 2025014",
                "Afhandelen terugvordering",
            ],
        )
        self.assertTrue(is_besluit_document(documents[2]))
        self.assertFalse(is_besluit_document(documents[0]))
        self.assertFalse(is_besluit_document(documents[1]))


class SearchBuildTests(unittest.TestCase):
    def test_build_id_changes_when_a_shard_hash_changes(self) -> None:
        shards = [
            {"year": "2025", "hash": "aaa"},
            {"year": "2026", "hash": "bbb"},
        ]
        self.assertEqual(search_build_id(shards), search_build_id(list(reversed(shards))))
        self.assertNotEqual(
            search_build_id(shards),
            search_build_id([{"year": "2025", "hash": "aaa"}, {"year": "2026", "hash": "ccc"}]),
        )
        self.assertEqual(len(search_build_id(shards)), 16)


class DocumentPageTests(unittest.TestCase):
    def test_document_page_shows_text_and_can_highlight_a_query(self) -> None:
        html = render_doc_page(
            {
                "publication_title": "Voorbeeld",
                "pdf_label": "Woo-besluit",
                "publication_date": "2026-08-04",
                "publication_type": "Woo",
                "page_count": 3,
                "ocr_used": False,
                "retrieved_at": "2026-08-05",
                "source_page_url": "https://www.uwv.nl/voorbeeld",
                "pdf_url": "https://www.uwv.nl/voorbeeld.pdf",
                "sha256": "abc123def456abc123def456abc123def456abc123def456abc123def456abcd",
                "blocks": [
                    {"type": "heading", "page": 1, "text": "Besluit"},
                    {"type": "paragraph", "page": 1, "text": "Deze tekst hoort op de pagina."},
                ],
            },
            "/",
        )

        self.assertIn("https://www.uwv.nl/voorbeeld.pdf", html)
        self.assertNotIn('class="pdf-frame"', html)
        self.assertNotIn("<iframe", html)
        self.assertNotIn("SHA256", html)
        self.assertNotIn("abc123def456", html)
        self.assertIn("Deze tekst hoort op de pagina.", html)
        self.assertIn("<h2>Besluit</h2>", html)
        self.assertIn('id="doc-text"', html)
        self.assertNotIn('class="doc-sheet"', html)
        self.assertIn('params.get("q")', html)
        self.assertIn('name="viewport"', html)

    def test_ocr_lines_stay_inside_their_boxes(self) -> None:
        html = render_extracted_text(
            [
                {
                    "type": "paragraph",
                    "page": 1,
                    "bbox": [40, 40, 280, 52],
                    "text": "Linkerkolom",
                    "source": "ocr",
                },
                {
                    "type": "paragraph",
                    "page": 1,
                    "bbox": [320, 42, 540, 54],
                    "text": "Rechterkolom",
                    "source": "ocr",
                },
                {
                    "type": "paragraph",
                    "page": 2,
                    "bbox": [40, 40, 200, 52],
                    "text": "Volgende pagina",
                    "source": "ocr",
                },
            ]
        )
        self.assertIn('class="doc-sheet"', html)
        self.assertIn("Linkerkolom", html)
        self.assertIn("Rechterkolom", html)
        self.assertIn("left:", html)
        self.assertIn("top:", html)
        self.assertNotIn("<p>Linkerkolom</p>", html)
        self.assertEqual(html.count('class="doc-page-separator"'), 1)

    def test_shorter_run_on_the_same_line_is_not_painted_on_top(self) -> None:
        html = render_extracted_text(
            [
                {
                    "type": "paragraph",
                    "page": 1,
                    "bbox": [70, 205, 518, 216],
                    "text": "Nieuwsuur besteed 15 juli aandacht de risicoscan",
                    "source": "text",
                },
                {
                    "type": "paragraph",
                    "page": 1,
                    "bbox": [167, 207, 456, 216],
                    "text": "op aan van",
                    "source": "text",
                },
            ]
        )
        self.assertIn("Nieuwsuur besteed 15 juli aandacht de risicoscan", html)
        self.assertNotIn("op aan van", html)


class PublicationsPageTests(unittest.TestCase):
    def test_year_browser_and_publication_stats(self) -> None:
        html = render_publications_page(
            [
                {
                    "slug": "een",
                    "title": "Publicatie",
                    "date": "2026-08-04",
                    "type": "Woo",
                    "source_page_url": "https://www.uwv.nl/p",
                    "page_count": 12,
                    "ocr_count": 1,
                    "documents": [
                        {
                            "label": "Woo-besluit",
                            "url": "doc/een/besluit.html",
                            "ocr_used": False,
                        }
                    ],
                }
            ],
            "/",
        )

        self.assertIn("publications.html?year=2026", html)
        self.assertIn("12 pagina's", html)
        self.assertIn("1 met OCR", html)
        self.assertIn('data-year="2026"', html)
        self.assertNotIn('id="search-input"', html)

    def test_publication_card_shows_pages_and_duplicate_marker(self) -> None:
        publications = build_publications(
            [
                {
                    "publication_slug": "eerste",
                    "publication_title": "Eerste",
                    "publication_date": "2026-07-08",
                    "publication_type": "Woo",
                    "source_page_url": "",
                    "pdf_label": "Woo-besluit",
                    "url": "doc/eerste/besluit.html",
                    "ocr_used": False,
                    "page_count": 3,
                    "sha256": "hash-a",
                    "pdf_url": "https://www.uwv.nl/a.pdf",
                },
                {
                    "publication_slug": "tweede",
                    "publication_title": "Tweede",
                    "publication_date": "2026-07-09",
                    "publication_type": "Woo",
                    "source_page_url": "",
                    "pdf_label": "Bijlage",
                    "url": "doc/tweede/bijlage.html",
                    "ocr_used": True,
                    "page_count": 4,
                    "sha256": "hash-b",
                    "pdf_url": "https://www.uwv.nl/a.pdf?download=1",
                },
            ]
        )
        html = render_publications_page(publications, "/")

        self.assertIn("3 pagina's", html)
        self.assertIn("4 pagina's", html)
        self.assertIn("ook elders", html)
        self.assertNotIn("hash-a", html)


class DuplicateTests(unittest.TestCase):
    def test_same_source_pdf_is_grouped_without_showing_a_hash(self) -> None:
        groups = find_duplicate_groups(
            [
                {
                    "sha256": "aaa",
                    "pdf_url": "https://example/a.pdf",
                    "label": "Een",
                    "title": "Publicatie A",
                    "url": "doc/a/1.html",
                },
                {
                    "sha256": "bbb",
                    "pdf_url": "https://example/a.pdf?x=1",
                    "label": "Twee",
                    "title": "Publicatie B",
                    "url": "doc/b/1.html",
                },
                {
                    "sha256": "ccc",
                    "pdf_url": "https://example/b.pdf",
                    "label": "Drie",
                    "title": "Publicatie C",
                    "url": "doc/c/1.html",
                },
            ]
        )

        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["reason"], "zelfde bron-PDF")
        self.assertEqual(len(groups[0]["documents"]), 2)

        html = render_statistics_page(
            {
                "document_count": 3,
                "publication_count": 3,
                "total_pages": 6,
                "average_pages": 2,
                "ocr_documents": 0,
                "ocr_percentage": 0,
                "total_blocks": 1,
                "total_characters": 10,
                "documents_by_year": {"2026": 3},
                "documents_by_type": {"Woo": 3},
                "documents_by_retrieved_month": {},
                "largest_documents": [],
                "example_searches": [],
                "duplicate_groups": groups,
                "duplicate_group_count": 1,
                "duplicate_document_count": 2,
            },
            "/",
        )

        self.assertIn("zelfde bron-PDF", html)
        self.assertIn("1 groep", html)
        self.assertNotIn("1 groepen", html)
        self.assertIn("doc/a/1.html", html)
        self.assertNotIn("SHA256", html)
        self.assertNotIn("aaa", html)


class InternalDashboardTests(unittest.TestCase):
    def test_dashboard_is_current_and_not_indexed(self) -> None:
        html = render_internal_dashboard(
            {
                "document_count": 4,
                "publication_count": 2,
                "total_pages": 10,
                "duplicate_group_count": 1,
                "documents_by_year": {"2026": 4},
            },
            [
                {
                    "title": "Nieuwste",
                    "date": "2026-09-03",
                    "documents": [{}, {}],
                    "page_count": 8,
                }
            ],
            "/",
        )

        self.assertIn('content="noindex, nofollow"', html)
        self.assertIn("Nieuwste", html)
        self.assertIn("niet opgenomen in de publieke navigatie", html)
        self.assertNotIn("site-nav-link", html)


if __name__ == "__main__":
    unittest.main()
