from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

from src.config import load_settings
from src.crawl import create_session, iter_new_pdfs
from src.extract import extract_pdf
from src.render import DocumentMetadata, render_document
from src.state import ProcessedPdf, StateStore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl UWV Woo publications, OCR PDFs, and write markdown/json output."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/sources.yml"),
        help="Path to YAML config file.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Directory for output files and state.json.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=1,
        help="Number of overview pages to fetch (default: 1 for daily runs).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    settings = load_settings(args.config, data_dir=args.data_dir)
    state = StateStore(settings.data_dir / "state.json")
    session = create_session(settings)

    processed_count = 0

    with tempfile.TemporaryDirectory(prefix="uwv-woo-pdf-") as temp_dir_name:
        temp_dir = Path(temp_dir_name)

        for downloaded in iter_new_pdfs(
            session=session,
            settings=settings,
            state=state,
            temp_dir=temp_dir,
            max_pages=args.max_pages,
        ):
            candidate = downloaded.candidate
            try:
                extraction = extract_pdf(
                    downloaded.local_path,
                    ocr_lang=settings.ocr_lang,
                    min_chars_per_page=settings.min_chars_per_page,
                )
                metadata = DocumentMetadata(
                    source_id=f"{candidate.publication.slug}/{candidate.slug}",
                    publication_slug=candidate.publication.slug,
                    pdf_slug=candidate.slug,
                    source_page_url=candidate.publication_page_url,
                    pdf_url=candidate.pdf_url,
                    publication_title=candidate.publication.title,
                    publication_date=candidate.publication.date,
                    publication_type=candidate.publication.publication_type,
                    pdf_label=candidate.pdf_label,
                    retrieved_at=StateStore.now_iso(),
                    sha256=downloaded.sha256,
                    page_count=extraction.page_count,
                    ocr_used=extraction.ocr_used,
                )
                md_path, json_path = render_document(
                    metadata=metadata,
                    blocks=extraction.blocks,
                    data_dir=settings.data_dir,
                )
                state.mark_processed(
                    ProcessedPdf(
                        pdf_url=candidate.pdf_url,
                        publication_slug=candidate.publication.slug,
                        pdf_slug=candidate.slug,
                        sha256=downloaded.sha256,
                        retrieved_at=metadata.retrieved_at,
                        md_path=str(md_path),
                        json_path=str(json_path),
                    )
                )
                state.save()
                processed_count += 1
                print(f"Processed {candidate.pdf_url} -> {json_path}")
            except Exception as exc:  # noqa: BLE001 - keep pipeline running
                print(f"Failed to process {candidate.pdf_url}: {exc}", file=sys.stderr)
            finally:
                downloaded.local_path.unlink(missing_ok=True)

    state.save()
    print(f"Done. Processed {processed_count} new PDF(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
