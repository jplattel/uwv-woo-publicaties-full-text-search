#!/usr/bin/env python3
"""Build a static GitHub Pages site from data/**/*.json extracts."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SITE_SRC = ROOT / "site"
DOCS_DIR = ROOT / "docs"
SCRIPTS_DIR = ROOT / "scripts"

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

BUILD_VERSION = 1
MANIFEST_NAME = ".build-manifest.json"

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
    parser.add_argument(
        "--force-rebuild",
        action="store_true",
        help="Ignore cached outputs and rebuild the entire site.",
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


@dataclass(frozen=True)
class DocumentSource:
    json_rel: str
    json_hash: str
    md_hash: str
    output_rel: str
    year: str


def file_sha256(path: Path) -> str:
    if not path.exists():
        return ""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compute_site_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(SITE_SRC.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(SITE_SRC).as_posix()
        hashes[rel] = file_sha256(path)
    return hashes


def collect_json_paths() -> list[Path]:
    return sorted(
        path
        for path in DATA_DIR.rglob("*.json")
        if path.name != "state.json"
    )


def collect_document_sources(json_paths: list[Path]) -> dict[str, DocumentSource]:
    sources: dict[str, DocumentSource] = {}

    for json_path in json_paths:
        json_rel = json_path.relative_to(ROOT).as_posix()
        md_path = json_path.with_suffix(".md")
        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        publication_slug = payload["publication_slug"]
        pdf_slug = payload["pdf_slug"]
        sources[json_rel] = DocumentSource(
            json_rel=json_rel,
            json_hash=file_sha256(json_path),
            md_hash=file_sha256(md_path),
            output_rel=f"doc/{publication_slug}/{pdf_slug}.html",
            year=year_from_date(payload.get("publication_date", "")) or "unknown",
        )

    return sources


def shard_content_hash(sources: list[DocumentSource]) -> str:
    digest = hashlib.sha256()
    for source in sorted(sources, key=lambda item: item.json_rel):
        digest.update(source.json_rel.encode())
        digest.update(source.json_hash.encode())
    return digest.hexdigest()


def load_manifest(path: Path) -> dict | None:
    if not path.exists():
        return None
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_manifest(path: Path, payload: dict) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


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
                "publication_slug": publication_slug,
                "publication_title": payload.get("publication_title", ""),
                "pdf_label": payload.get("pdf_label", ""),
                "publication_date": payload.get("publication_date", ""),
                "publication_type": payload.get("publication_type", ""),
                "ocr_used": bool(payload.get("ocr_used")),
                "source_page_url": payload.get("source_page_url", ""),
                "pdf_url": payload.get("pdf_url", ""),
                "url": doc_url,
                "text": text,
            }
        )
        log_progress("indexed", index, total, label)

    return documents


def compute_filter_options(documents: list[dict]) -> dict:
    types = sorted({doc.get("publication_type") or "Onbekend" for doc in documents})
    years = sorted(
        {
            year
            for doc in documents
            if (year := year_from_date(doc.get("publication_date", "")))
        }
    )
    return {
        "publicationTypes": types,
        "yearRange": {"min": years[0], "max": years[-1]} if years else None,
    }


def build_publications(documents: list[dict]) -> list[dict]:
    grouped: dict[str, dict] = {}

    for document in documents:
        slug = document["publication_slug"]
        if slug not in grouped:
            grouped[slug] = {
                "slug": slug,
                "title": document["publication_title"],
                "date": document["publication_date"],
                "type": document.get("publication_type") or "Onbekend",
                "source_page_url": document.get("source_page_url", ""),
                "documents": [],
            }
        grouped[slug]["documents"].append(
            {
                "label": document["pdf_label"],
                "url": document["url"],
                "ocr_used": document.get("ocr_used", False),
            }
        )

    publications = list(grouped.values())
    for publication in publications:
        publication["documents"].sort(key=lambda item: item["label"])
    publications.sort(key=lambda item: item["date"], reverse=True)
    return publications


def build_minisearch_index(
    documents: list[dict],
    output_dir: Path,
    years: set[str] | None = None,
) -> list[dict]:
    node_modules = SCRIPTS_DIR / "node_modules"
    if not node_modules.exists():
        log("  Installing Node dependencies for search index…")
        subprocess.run(
            ["npm", "install", "--prefix", str(SCRIPTS_DIR)],
            check=True,
            cwd=SCRIPTS_DIR,
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    temp_docs = output_dir / ".documents.tmp.json"
    command = [
        "node",
        "--max-old-space-size=4096",
        str(SCRIPTS_DIR / "build_search_index.mjs"),
        str(temp_docs),
        str(output_dir),
    ]
    if years is not None:
        command.append(",".join(sorted(years)))

    try:
        docs_to_index = documents
        if years is not None:
            docs_to_index = [
                document
                for document in documents
                if (year_from_date(document.get("publication_date", "")) or "unknown") in years
            ]
        with temp_docs.open("w", encoding="utf-8") as handle:
            json.dump(docs_to_index, handle, ensure_ascii=False)

        subprocess.run(command, check=True, cwd=SCRIPTS_DIR)
    finally:
        temp_docs.unlink(missing_ok=True)

    manifest_path = output_dir / "manifest.json"
    if years is None and manifest_path.exists():
        with manifest_path.open(encoding="utf-8") as handle:
            manifest = json.load(handle)
        return manifest.get("shards", [])

    return [
        {
            "year": year,
            "path": f"{year}.json",
            "count": len(
                [
                    document
                    for document in documents
                    if (year_from_date(document.get("publication_date", "")) or "unknown") == year
                ]
            ),
        }
        for year in sorted(years or [])
    ]


def write_search_manifest(
    output_dir: Path,
    document_count: int,
    shards: list[dict],
) -> None:
    manifest_path = output_dir / "manifest.json"
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "version": 1,
                "documentCount": document_count,
                "shards": shards,
            },
            handle,
            ensure_ascii=False,
            indent=2,
        )


def render_publications_page(publications: list[dict], base_path: str) -> str:
    by_year: dict[str, list[dict]] = defaultdict(list)
    for publication in publications:
        year = year_from_date(publication["date"]) or "Onbekend"
        by_year[year].append(publication)

    sections: list[str] = []
    for year in sorted(by_year.keys(), reverse=True):
        cards: list[str] = []
        for publication in by_year[year]:
            doc_links = "".join(
                f"""
                <li>
                  <a href="{html.escape(base_path)}{html.escape(doc['url'])}">{html.escape(doc['label'])}</a>
                  {('<span class="ocr-badge">OCR</span>' if doc.get('ocr_used') else '')}
                </li>
                """
                for doc in publication["documents"]
            )
            source_link = ""
            if publication.get("source_page_url"):
                source_link = (
                    f'<a class="publication-source" href="{html.escape(publication["source_page_url"])}" '
                    f'target="_blank" rel="noopener noreferrer">Bron op uwv.nl</a>'
                )
            cards.append(
                f"""
                <article class="publication-card">
                  <h3>{html.escape(publication['title'])}</h3>
                  <div class="publication-meta">
                    {format_date(publication['date'])} · {html.escape(publication['type'])} ·
                    {format_number(len(publication['documents']))} documenten
                    {f" · {source_link}" if source_link else ""}
                  </div>
                  <ul class="publication-docs">{doc_links}</ul>
                </article>
                """
            )
        sections.append(
            f"""
            <section class="publications-year">
              <h2>{html.escape(year)}</h2>
              <div class="publications-grid">{''.join(cards)}</div>
            </section>
            """
        )

    return f"""<!DOCTYPE html>
<html lang="nl">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="base-path" content="{html.escape(base_path)}" />
    <title>Publicaties · UWV Woo-publicaties</title>
    <link rel="stylesheet" href="{html.escape(base_path)}assets/style.css" />
  </head>
  <body>
    {render_site_header("UWV Woo-publicaties", "Blader door alle Woo-publicaties", base_path, active="publications")}
    <main class="publications-main">
      <p class="publications-intro">
        {format_number(len(publications))} publicaties met
        {format_number(sum(len(pub['documents']) for pub in publications))} documenten,
        gegroepeerd op publicatiejaar.
      </p>
      {"".join(sections)}
    </main>
  </body>
</html>
"""


def document_search_text(document: dict) -> str:
    return " ".join(
        [
            document.get("publication_title", ""),
            document.get("pdf_label", ""),
            document.get("text", ""),
        ]
    ).lower()


def count_example_matches(documents: list[dict], term: str) -> int:
    words = [word.lower() for word in term.split() if word.strip()]
    if not words:
        return 0

    total = 0
    for document in documents:
        haystack = document_search_text(document)
        if all(word in haystack for word in words):
            total += 1
    return total


def compute_example_searches(documents: list[dict]) -> list[dict]:
    return [
        {"term": term, "count": count_example_matches(documents, term)}
        for term in SEARCH_SUGGESTIONS
    ]


def year_from_date(value: str) -> str | None:
    match = re.match(r"(\d{4})", value or "")
    return match.group(1) if match else None


def month_from_date(value: str) -> str | None:
    match = re.match(r"(\d{4}-\d{2})", value or "")
    return match.group(1) if match else None


def compute_statistics(documents: list[dict]) -> dict:
    json_paths = sorted(
        path
        for path in DATA_DIR.rglob("*.json")
        if path.name != "state.json"
    )

    publication_slugs: set[str] = set()
    years: Counter[str] = Counter()
    types: Counter[str] = Counter()
    retrieved_months: Counter[str] = Counter()
    total_pages = 0
    ocr_documents = 0
    total_blocks = 0
    total_chars = 0
    largest: list[dict] = []

    for json_path in json_paths:
        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)

        publication_slugs.add(payload.get("publication_slug", ""))
        page_count = int(payload.get("page_count") or 0)
        total_pages += page_count
        if payload.get("ocr_used"):
            ocr_documents += 1

        blocks = payload.get("blocks") or []
        total_blocks += len(blocks)
        for block in blocks:
            total_chars += len(block.get("text") or "")

        year = year_from_date(payload.get("publication_date", ""))
        if year:
            years[year] += 1

        pub_type = (payload.get("publication_type") or "Onbekend").strip()
        types[pub_type] += 1

        retrieved_month = month_from_date(payload.get("retrieved_at", ""))
        if retrieved_month:
            retrieved_months[retrieved_month] += 1

        largest.append(
            {
                "title": payload.get("publication_title", ""),
                "label": payload.get("pdf_label", ""),
                "pages": page_count,
                "url": f"doc/{payload['publication_slug']}/{payload['pdf_slug']}.html",
            }
        )

    largest.sort(key=lambda item: item["pages"], reverse=True)
    document_count = len(documents)
    publication_count = len(publication_slugs)

    return {
        "document_count": document_count,
        "publication_count": publication_count,
        "total_pages": total_pages,
        "average_pages": round(total_pages / document_count, 1) if document_count else 0,
        "ocr_documents": ocr_documents,
        "ocr_percentage": round(100 * ocr_documents / document_count, 1) if document_count else 0,
        "total_blocks": total_blocks,
        "total_characters": total_chars,
        "documents_by_year": dict(sorted(years.items())),
        "documents_by_type": dict(types.most_common()),
        "documents_by_retrieved_month": dict(sorted(retrieved_months.items())[-12:]),
        "largest_documents": largest[:8],
        "example_searches": compute_example_searches(documents),
    }


def format_number(value: int | float) -> str:
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    return f"{value:,}".replace(",", ".")


def render_bar_rows(items: dict[str, int], limit: int = 10) -> str:
    if not items:
        return "<p class=\"stats-empty\">Geen gegevens beschikbaar.</p>"

    top_items = list(items.items())[:limit]
    max_value = max(value for _, value in top_items) or 1
    rows: list[str] = []

    for label, value in top_items:
        width = max(4, round(100 * value / max_value))
        rows.append(
            f"""
            <div class="stats-bar-row">
              <div class="stats-bar-label">{html.escape(label)}</div>
              <div class="stats-bar-track" aria-hidden="true">
                <span class="stats-bar-fill" style="width: {width}%"></span>
              </div>
              <div class="stats-bar-value">{format_number(value)}</div>
            </div>
            """
        )

    return "".join(rows)


def render_statistics_page(stats: dict, base_path: str) -> str:
    example_rows = "".join(
        f"""
        <tr>
          <td><a href="{html.escape(base_path)}?q={quote(item['term'])}">{html.escape(item["term"])}</a></td>
          <td>{format_number(item["count"])}</td>
        </tr>
        """
        for item in stats["example_searches"]
    )

    largest_rows = "".join(
        f"""
        <tr>
          <td><a href="{html.escape(base_path)}{html.escape(item["url"])}">{html.escape(truncate(item["title"] or item["label"], 80))}</a></td>
          <td>{format_number(item["pages"])}</td>
        </tr>
        """
        for item in stats["largest_documents"]
    )

    summary_cards = [
        ("Documenten", stats["document_count"]),
        ("Publicaties", stats["publication_count"]),
        ("Pagina's totaal", stats["total_pages"]),
        ("Gem. pagina's", stats["average_pages"]),
        ("OCR-documenten", stats["ocr_documents"]),
        ("Tekstblokken", stats["total_blocks"]),
    ]

    cards_html = "".join(
        f"""
        <article class="stats-card">
          <p class="stats-card-label">{html.escape(label)}</p>
          <p class="stats-card-value">{html.escape(format_number(value))}</p>
        </article>
        """
        for label, value in summary_cards
    )

    return f"""<!DOCTYPE html>
<html lang="nl">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="base-path" content="{html.escape(base_path)}" />
    <title>Statistieken · UWV Woo-publicaties</title>
    <link rel="stylesheet" href="{html.escape(base_path)}assets/style.css" />
  </head>
  <body>
    {render_site_header("UWV Woo-publicaties", "Overzicht van geïndexeerde Woo-documenten", base_path, active="stats")}
    <main class="stats-main">
      <section class="stats-summary">
        {cards_html}
      </section>

      <section class="stats-panel">
        <h2>Documenten per publicatiejaar</h2>
        {render_bar_rows(stats["documents_by_year"], limit=12)}
      </section>

      <div class="stats-grid">
        <section class="stats-panel">
          <h2>Documenten per type</h2>
          {render_bar_rows(stats["documents_by_type"], limit=8)}
        </section>
        <section class="stats-panel">
          <h2>Recent opgehaald (per maand)</h2>
          {render_bar_rows(stats["documents_by_retrieved_month"], limit=12)}
        </section>
      </div>

      <div class="stats-grid">
        <section class="stats-panel">
          <h2>Voorbeeldzoekopdrachten</h2>
          <table class="stats-table">
            <thead>
              <tr><th>Zoekterm</th><th>Documenten</th></tr>
            </thead>
            <tbody>{example_rows}</tbody>
          </table>
        </section>
        <section class="stats-panel">
          <h2>Grootste documenten</h2>
          <table class="stats-table">
            <thead>
              <tr><th>Document</th><th>Pagina's</th></tr>
            </thead>
            <tbody>{largest_rows}</tbody>
          </table>
        </section>
      </div>

      <p class="stats-footnote">
        {stats["ocr_percentage"]}% van de documenten is via OCR geëxtraheerd.
        Totaal {format_number(stats["total_characters"])} tekens geïndexeerd voor zoeken.
      </p>
    </main>
  </body>
</html>
"""


def render_site_header(title: str, subtitle: str, base_path: str, active: str) -> str:
    search_active = " is-active" if active == "search" else ""
    publications_active = " is-active" if active == "publications" else ""
    stats_active = " is-active" if active == "stats" else ""
    about_active = " is-active" if active == "about" else ""
    return f"""
    <header class="site-header">
      <div class="site-header-inner">
        <div>
          <h1>{html.escape(title)}</h1>
          <p>{html.escape(subtitle)}</p>
        </div>
        <nav class="site-nav" aria-label="Hoofdnavigatie">
          <a class="site-nav-link{search_active}" href="{html.escape(base_path)}">Zoeken</a>
          <a class="site-nav-link{publications_active}" href="{html.escape(base_path)}publications.html">Publicaties</a>
          <a class="site-nav-link{stats_active}" href="{html.escape(base_path)}statistics.html">Statistieken</a>
          <a class="site-nav-link{about_active}" href="{html.escape(base_path)}about.html">Over</a>
        </nav>
      </div>
    </header>
    """


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
    header_html = render_site_header(title, pdf_label, base_path, active="")

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
    {header_html}
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


def remove_tree(path: Path) -> None:
    if not path.exists():
        return
    shutil.rmtree(path, ignore_errors=True)
    if path.exists():
        raise RuntimeError(f"Failed to remove existing directory: {path}")


def build_site(output_dir: Path, base_path: str, force_rebuild: bool = False) -> None:
    started_at = time.perf_counter()
    staging_dir = output_dir.with_name(f"{output_dir.name}.build")
    previous_manifest_path = output_dir / MANIFEST_NAME
    previous_manifest = None if force_rebuild else load_manifest(previous_manifest_path)

    site_hashes = compute_site_hashes()
    json_paths = collect_json_paths()
    document_sources = collect_document_sources(json_paths)

    site_changed = (
        previous_manifest is None
        or previous_manifest.get("buildVersion") != BUILD_VERSION
        or previous_manifest.get("basePath") != base_path
        or previous_manifest.get("site") != site_hashes
    )

    previous_documents = previous_manifest.get("documents", {}) if previous_manifest else {}
    changed_docs: list[str] = []
    removed_outputs: list[str] = []

    for json_rel, source in document_sources.items():
        previous = previous_documents.get(json_rel)
        if (
            site_changed
            or previous is None
            or previous.get("jsonHash") != source.json_hash
            or previous.get("mdHash") != source.md_hash
        ):
            changed_docs.append(json_rel)

    for json_rel, previous in previous_documents.items():
        if json_rel not in document_sources:
            removed_outputs.append(previous["outputRel"])

    sources_by_year: dict[str, list[DocumentSource]] = defaultdict(list)
    for source in document_sources.values():
        sources_by_year[source.year].append(source)

    previous_shards = previous_manifest.get("searchShards", {}) if previous_manifest else {}
    changed_years: set[str] = set()
    for year, sources in sources_by_year.items():
        current_hash = shard_content_hash(sources)
        previous = previous_shards.get(year)
        if site_changed or previous is None or previous.get("hash") != current_hash:
            changed_years.add(year)

    for year in previous_shards:
        if year not in sources_by_year:
            changed_years.add(year)

    can_incremental = (
        not force_rebuild
        and output_dir.exists()
        and previous_manifest is not None
        and previous_manifest.get("buildVersion") == BUILD_VERSION
        and previous_manifest.get("basePath") == base_path
    )

    log(f"Building site → {output_dir}")
    log(f"  Base path: {base_path}")
    log(f"  Staging in: {staging_dir}")
    if force_rebuild:
        log("  Mode: full rebuild (--force-rebuild)")
    elif can_incremental:
        log(
            "  Mode: incremental "
            f"({len(changed_docs)} docs, {len(changed_years)} search shards, "
            f"site={'yes' if site_changed else 'no'})"
        )
    else:
        log("  Mode: full rebuild (no usable cache)")

    remove_tree(staging_dir)
    if can_incremental:
        shutil.copytree(output_dir, staging_dir)
    else:
        staging_dir.mkdir(parents=True)

    if site_changed or not can_incremental:
        log("  Updating static assets…")
        assets_src = SITE_SRC / "assets"
        assets_dst = staging_dir / "assets"
        remove_tree(assets_dst)
        shutil.copytree(assets_src, assets_dst)

        log("  Writing index.html…")
        index_template = (SITE_SRC / "index.html").read_text(encoding="utf-8")
        index_html = index_template.replace("{{ base_path }}", base_path)
        (staging_dir / "index.html").write_text(index_html, encoding="utf-8")

        log("  Writing about.html…")
        about_template = (SITE_SRC / "about.html").read_text(encoding="utf-8")
        about_html = about_template.replace("{{ base_path }}", base_path)
        (staging_dir / "about.html").write_text(about_html, encoding="utf-8")
    else:
        log("  Static assets unchanged")

    data_changed = bool(changed_docs or removed_outputs or changed_years)
    if data_changed or not can_incremental:
        log("  Loading documents for search metadata…")
        documents = load_documents()
        example_searches = compute_example_searches(documents)
        stats = compute_statistics(documents)
        filter_options = compute_filter_options(documents)
        publications = build_publications(documents)
    else:
        documents = []
        example_searches = previous_manifest.get("exampleSearches", [])
        stats = previous_manifest.get("stats", {})
        filter_options = previous_manifest.get("filters", {})
        publications = []

    index_dir = staging_dir / "search-index"
    index_dir.mkdir(parents=True, exist_ok=True)

    if changed_years or not can_incremental:
        if can_incremental and changed_years and len(changed_years) < len(sources_by_year):
            log(f"  Rebuilding search shards: {', '.join(sorted(changed_years))}")
            if not documents:
                documents = load_documents()
            build_minisearch_index(documents, index_dir, years=changed_years)
            for year in changed_years:
                if year not in sources_by_year:
                    shard_path = index_dir / f"{year}.json"
                    if shard_path.exists():
                        shard_path.unlink()
        else:
            log("  Building search index from data/…")
            if not documents:
                documents = load_documents()
            remove_tree(index_dir)
            index_dir.mkdir(parents=True)
            build_minisearch_index(documents, index_dir)
    else:
        log("  Search index unchanged")

    shard_manifest: list[dict] = []
    for year in sorted(sources_by_year):
        sources = sources_by_year[year]
        shard_manifest.append(
            {
                "year": year,
                "path": f"{year}.json",
                "count": len(sources),
            }
        )
    write_search_manifest(index_dir, len(document_sources), shard_manifest)
    index_bytes = sum(path.stat().st_size for path in index_dir.glob("*.json"))

    if data_changed or not can_incremental:
        meta_path = staging_dir / "search-meta.json"
        with meta_path.open("w", encoding="utf-8") as handle:
            json.dump(
                {
                    "documentCount": len(documents),
                    "publicationCount": stats["publication_count"],
                    "suggestions": SEARCH_SUGGESTIONS,
                    "exampleSearches": example_searches,
                    "filters": filter_options,
                    "indexBasePath": "search-index/",
                    "indexShards": [
                        {
                            "year": shard["year"],
                            "path": f"search-index/{shard['path']}",
                            "count": shard["count"],
                        }
                        for shard in shard_manifest
                    ],
                },
                handle,
                ensure_ascii=False,
            )
        log(f"  Wrote search-meta.json ({format_bytes(meta_path.stat().st_size)})")

        log("  Writing statistics.html…")
        (staging_dir / "statistics.html").write_text(
            render_statistics_page(stats, base_path),
            encoding="utf-8",
        )

        log("  Writing publications.html…")
        (staging_dir / "publications.html").write_text(
            render_publications_page(publications, base_path),
            encoding="utf-8",
        )
    else:
        log("  Aggregate pages unchanged")

    log(f"  Search index: {len(shard_manifest)} shards ({format_bytes(index_bytes)})")

    for output_rel in removed_outputs:
        stale_path = staging_dir / output_rel
        if stale_path.exists():
            stale_path.unlink()

    docs_to_render = set(changed_docs)
    if site_changed and can_incremental:
        docs_to_render = set(document_sources.keys())

    if not can_incremental:
        docs_to_render = set(document_sources.keys())

    render_total = len(docs_to_render)
    copied_docs = len(document_sources) - render_total
    if render_total:
        log(f"  Rendering {render_total} HTML page(s)…")
    if copied_docs:
        log(f"  Reused {copied_docs} unchanged HTML page(s)")

    publication_slugs: set[str] = set()
    missing_markdown = 0
    render_index = 0
    json_path_by_rel = {
        path.relative_to(ROOT).as_posix(): path for path in json_paths
    }

    for json_rel, source in document_sources.items():
        publication_slugs.add(Path(source.output_rel).parts[1])
        if json_rel not in docs_to_render:
            continue

        render_index += 1
        json_path = json_path_by_rel[json_rel]
        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)

        md_path = json_path.with_suffix(".md")
        if md_path.exists():
            _, body_html = markdown_body(md_path)
        else:
            body_html = ""
            missing_markdown += 1

        doc_path = staging_dir / source.output_rel
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        doc_path.write_text(
            render_doc_page(payload, body_html, base_path),
            encoding="utf-8",
        )
        label = payload.get("pdf_label") or payload.get("publication_title") or payload["pdf_slug"]
        log_progress("rendered", render_index, render_total, label)

    (staging_dir / ".nojekyll").touch()

    manifest_documents = {
        json_rel: {
            "jsonRel": source.json_rel,
            "jsonHash": source.json_hash,
            "mdHash": source.md_hash,
            "outputRel": source.output_rel,
            "year": source.year,
        }
        for json_rel, source in document_sources.items()
    }
    manifest_shards = {
        year: {
            "hash": shard_content_hash(sources),
            "count": len(sources),
            "path": f"{year}.json",
        }
        for year, sources in sources_by_year.items()
    }

    if not stats and previous_manifest:
        stats = previous_manifest.get("stats", {})

    write_manifest(
        staging_dir / MANIFEST_NAME,
        {
            "buildVersion": BUILD_VERSION,
            "basePath": base_path,
            "site": site_hashes,
            "documents": manifest_documents,
            "searchShards": manifest_shards,
            "exampleSearches": example_searches,
            "filters": filter_options,
            "stats": stats,
        },
    )

    required_paths = [
        staging_dir / "index.html",
        staging_dir / "about.html",
        staging_dir / "publications.html",
        staging_dir / "statistics.html",
        staging_dir / "assets" / "style.css",
        staging_dir / "assets" / "app.js",
        staging_dir / "assets" / "search-worker.js",
        staging_dir / "search-meta.json",
        staging_dir / "search-index" / "manifest.json",
        staging_dir / MANIFEST_NAME,
    ]
    missing = [path for path in required_paths if not path.exists()]
    if missing:
        missing_list = ", ".join(str(path.relative_to(staging_dir)) for path in missing)
        raise RuntimeError(f"Build incomplete, missing: {missing_list}")

    log("  Promoting staged build to output directory…")
    backup_dir = output_dir.with_name(f"{output_dir.name}.old")
    remove_tree(backup_dir)
    if output_dir.exists():
        output_dir.rename(backup_dir)
    staging_dir.rename(output_dir)
    remove_tree(backup_dir)

    elapsed = time.perf_counter() - started_at
    html_count = len(list((output_dir / "doc").rglob("*.html")))
    log("")
    log("Build complete")
    log(f"  Documents:   {len(document_sources)}")
    log(f"  Publications:{len(publication_slugs)}")
    log(f"  HTML pages:  {html_count} ({render_total} rendered, {copied_docs} reused)")
    log(f"  Search:      {len(shard_manifest)} shards ({len(changed_years)} rebuilt)")
    log(f"  Index page:  {output_dir / 'index.html'}")
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
    build_site(args.output, base_path, force_rebuild=args.force_rebuild)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
