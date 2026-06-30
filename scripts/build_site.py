#!/usr/bin/env python3
"""Build a static GitHub Pages site from data/**/*.json extracts."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SITE_SRC = ROOT / "site"
DOCS_DIR = ROOT / "docs"

FRONTMATTER_LABELS = {
    "publication_title": "Publicatie",
    "pdf_label": "Document",
    "publication_date": "Publicatiedatum",
    "publication_type": "Type",
    "source_page_url": "Bronpagina",
    "pdf_url": "Originele PDF",
    "retrieved_at": "Opgehaald op",
    "page_count": "Pagina's",
    "ocr_used": "OCR gebruikt",
    "sha256": "SHA256",
}

FRONTMATTER_ORDER = [
    "publication_title",
    "pdf_label",
    "publication_date",
    "publication_type",
    "page_count",
    "ocr_used",
    "retrieved_at",
    "source_page_url",
    "pdf_url",
    "sha256",
]

SEARCH_SUGGESTIONS = [
    "WIA beoordeling",
    "loonsanctie",
    "bezwaar beroep",
    "fraudeonderzoek",
    "Ziektewet",
    "WW uitkering",
    "eigenrisicodrager",
    "WGA uitkering",
    "inkomensverrekening",
    "Woo-besluit",
]

VERBOSE = False


def log(message: str) -> None:
    print(message, flush=True)


def format_bytes(size: int) -> str:
    if size < 1024:
        return f"{size} B"
    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 * 1024):.1f} MB"


def truncate(text: str, max_length: int = 70) -> str:
    text = " ".join(text.split())
    if len(text) <= max_length:
        return text
    return f"{text[: max_length - 1]}…"


def should_log_progress(index: int, total: int) -> bool:
    if VERBOSE:
        return True
    if total <= 20:
        return True
    if index == 1 or index == total:
        return True
    return index % 25 == 0


def log_progress(prefix: str, index: int, total: int, label: str) -> None:
    if not should_log_progress(index, total):
        return
    width = len(str(total))
    log(f"  [{index:>{width}}/{total}] {prefix} {truncate(label)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build GitHub Pages site from data/")
    parser.add_argument(
        "--base-path",
        default=os.environ.get("SITE_BASE_PATH", ""),
        help="Base path for GitHub Pages project site (e.g. /uwv-woo-verzoeken/).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DOCS_DIR,
        help="Output directory for the built site.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Log progress for every document instead of every 25.",
    )
    return parser.parse_args()


def normalize_base_path(value: str) -> str:
    if not value:
        repo = os.environ.get("GITHUB_REPOSITORY", "")
        if repo and "/" in repo:
            value = f"/{repo.split('/', 1)[1]}/"
        else:
            value = "/"
    if not value.startswith("/"):
        value = f"/{value}"
    if not value.endswith("/"):
        value = f"{value}/"
    return value


def load_documents() -> list[dict]:
    json_paths = sorted(
        path
        for path in DATA_DIR.rglob("*.json")
        if path.name != "state.json"
    )
    documents: list[dict] = []
    total = len(json_paths)
    documents: list[dict] = []

    for index, json_path in enumerate(json_paths, start=1):
        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)

        blocks = payload.get("blocks") or []
        text = "\n".join(
            block.get("text", "").strip()
            for block in blocks
            if block.get("text", "").strip()
        )
        publication_slug = payload["publication_slug"]
        pdf_slug = payload["pdf_slug"]
        doc_url = f"doc/{publication_slug}/{pdf_slug}.html"
        label = payload.get("pdf_label") or payload.get("publication_title") or pdf_slug

        documents.append(
            {
                "id": payload.get("source_id") or f"{publication_slug}/{pdf_slug}",
                "publication_title": payload.get("publication_title", ""),
                "pdf_label": payload.get("pdf_label", ""),
                "publication_date": payload.get("publication_date", ""),
                "publication_type": payload.get("publication_type", ""),
                "source_page_url": payload.get("source_page_url", ""),
                "pdf_url": payload.get("pdf_url", ""),
                "url": doc_url,
                "text": text,
            }
        )
        log_progress("indexed", index, total, label)

    return documents


def format_date(value: str) -> str:
    match = re.match(r"(\d{4}-\d{2}-\d{2})", value or "")
    if not match:
        return html.escape(value or "")
    year, month, day = match.group(1).split("-")
    months = [
        "januari",
        "februari",
        "maart",
        "april",
        "mei",
        "juni",
        "juli",
        "augustus",
        "september",
        "oktober",
        "november",
        "december",
    ]
    return f"{int(day)} {months[int(month) - 1]} {year}"


def strip_leading_metadata_text(body: str) -> str:
    lines = body.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line or line == "---":
            index += 1
            continue
        if re.match(r"^[a-z_]+:\s", line, re.IGNORECASE):
            index += 1
            continue
        break
    return "\n".join(lines[index:]).strip()


def markdown_body(md_path: Path) -> tuple[dict, str]:
    text = md_path.read_text(encoding="utf-8")
    frontmatter: dict = {}
    if text.startswith("---\n"):
        frontmatter_text, rest = text.split("---\n", 1)
        frontmatter = yaml.safe_load(frontmatter_text) or {}
        body = rest.split("\n", 1)[1] if "\n" in rest else ""
    else:
        body = text

    footer_split = body.split("\n\n---\n\n", 1)
    body = strip_leading_metadata_text(footer_split[0].strip())
    return frontmatter, markdown.markdown(body, extensions=["extra", "sane_lists"])


def format_frontmatter_value(key: str, value) -> str:
    if value is None or value == "":
        return "—"
    if key == "publication_date" or key == "retrieved_at":
        return format_date(str(value))
    if key == "ocr_used":
        return "Ja" if value else "Nee"
    if key == "page_count":
        return str(value)
    if key == "sha256":
        text = str(value)
        short = f"{text[:12]}…{text[-8:]}" if len(text) > 24 else text
        return f'<code class="hash" title="{html.escape(text)}">{html.escape(short)}</code>'
    if key in {"source_page_url", "pdf_url"}:
        url = html.escape(str(value))
        label = "Open bronpagina" if key == "source_page_url" else "Download PDF"
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
    return html.escape(str(value))


def render_frontmatter(payload: dict) -> str:
    rows: list[str] = []
    seen: set[str] = set()

    for key in FRONTMATTER_ORDER:
        if key not in payload or key in {"publication_slug", "pdf_slug", "source_id"}:
            continue
        seen.add(key)
        label = FRONTMATTER_LABELS.get(key, key.replace("_", " ").title())
        value_html = format_frontmatter_value(key, payload.get(key))
        rows.append(f"<dt>{html.escape(label)}</dt><dd>{value_html}</dd>")

    for key, value in payload.items():
        if key in seen or key in {"blocks", "publication_slug", "pdf_slug", "source_id"}:
            continue
        label = FRONTMATTER_LABELS.get(key, key.replace("_", " ").title())
        value_html = format_frontmatter_value(key, value)
        rows.append(f"<dt>{html.escape(label)}</dt><dd>{value_html}</dd>")

    return f'<section class="frontmatter-card"><h2>Metadata</h2><dl class="frontmatter-grid">{"".join(rows)}</dl></section>'


def render_doc_page(payload: dict, body_html: str, base_path: str) -> str:
    title = html.escape(payload.get("publication_title", "Document"))
    pdf_label = html.escape(payload.get("pdf_label", ""))
    pdf_url = html.escape(payload.get("pdf_url", ""))
    frontmatter_html = render_frontmatter(payload)

    return f"""<!DOCTYPE html>
<html lang="nl">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="base-path" content="{html.escape(base_path)}" />
    <title>{title}</title>
    <link rel="stylesheet" href="{html.escape(base_path)}assets/style.css" />
  </head>
  <body class="doc-page">
    <header class="site-header">
      <h1>{title}</h1>
      <p>{pdf_label}</p>
    </header>
    <main class="doc-main">
      <a class="back-link" href="{html.escape(base_path)}">← Terug naar zoeken</a>
      {frontmatter_html}
      <div class="doc-layout">
        <section class="doc-panel doc-panel-text">
          <div class="panel-heading">
            <h2>Geëxtraheerde tekst</h2>
            <p class="panel-note">Automatisch geëxtraheerd; controleer altijd de originele PDF.</p>
          </div>
          <article class="doc-content">{body_html}</article>
        </section>
        <section class="doc-panel doc-panel-pdf">
          <div class="panel-heading">
            <h2>Originele PDF</h2>
            <a class="pdf-open-link" href="{pdf_url}" target="_blank" rel="noopener noreferrer">Open in nieuw tabblad</a>
          </div>
          <div class="pdf-frame-wrap">
            <iframe
              class="pdf-frame"
              src="{pdf_url}"
              title="Originele PDF"
              loading="lazy"
            ></iframe>
            <p class="pdf-fallback">
              PDF niet zichtbaar? <a href="{pdf_url}" target="_blank" rel="noopener noreferrer">Open de PDF op uwv.nl</a>.
            </p>
          </div>
        </section>
      </div>
    </main>
  </body>
</html>
"""


def build_site(output_dir: Path, base_path: str) -> None:
    started_at = time.perf_counter()
    log(f"Building site → {output_dir}")
    log(f"  Base path: {base_path}")

    if output_dir.exists():
        log("  Clearing previous output…")
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    log("  Copying static assets…")
    assets_src = SITE_SRC / "assets"
    assets_dst = output_dir / "assets"
    shutil.copytree(assets_src, assets_dst)

    log("  Writing index.html…")
    index_template = (SITE_SRC / "index.html").read_text(encoding="utf-8")
    index_html = index_template.replace("{{ base_path }}", base_path)
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")

    log("  Building search index from data/…")
    documents = load_documents()
    index_path = output_dir / "search-index.json"
    with index_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "documents": documents,
                "suggestions": SEARCH_SUGGESTIONS,
            },
            handle,
            ensure_ascii=False,
        )
    log(f"  Wrote search-index.json ({format_bytes(index_path.stat().st_size)})")

    json_paths = sorted(
        path
        for path in DATA_DIR.rglob("*.json")
        if path.name != "state.json"
    )
    publication_slugs = set()
    missing_markdown = 0

    log(f"  Rendering {len(json_paths)} HTML pages…")
    doc_root = output_dir / "doc"
    render_total = len(json_paths)
    for index, json_path in enumerate(json_paths, start=1):
        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)

        md_path = json_path.with_suffix(".md")
        if md_path.exists():
            _, body_html = markdown_body(md_path)
        else:
            body_html = ""
            missing_markdown += 1

        publication_slugs.add(payload["publication_slug"])
        doc_dir = doc_root / payload["publication_slug"]
        doc_dir.mkdir(parents=True, exist_ok=True)
        doc_path = doc_dir / f"{payload['pdf_slug']}.html"
        doc_path.write_text(
            render_doc_page(payload, body_html, base_path),
            encoding="utf-8",
        )
        label = payload.get("pdf_label") or payload.get("publication_title") or payload["pdf_slug"]
        log_progress("rendered", index, render_total, label)

    (output_dir / ".nojekyll").touch()

    elapsed = time.perf_counter() - started_at
    html_count = len(list(doc_root.rglob("*.html")))
    log("")
    log("Build complete")
    log(f"  Documents:   {len(documents)}")
    log(f"  Publications:{len(publication_slugs)}")
    log(f"  HTML pages:  {html_count}")
    log(f"  Suggestions: {len(SEARCH_SUGGESTIONS)}")
    if missing_markdown:
        print(
            f"  Warning:     {missing_markdown} document(s) without markdown source",
            file=sys.stderr,
        )
    log(f"  Output:      {output_dir}")
    log(f"  Duration:    {elapsed:.1f}s")


def main() -> int:
    global VERBOSE
    args = parse_args()
    VERBOSE = args.verbose
    base_path = normalize_base_path(args.base_path)
    build_site(args.output, base_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
