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
]

HIDDEN_FRONTMATTER_KEYS = {
    "sha256",
    "blocks",
    "publication_slug",
    "pdf_slug",
    "source_id",
}

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

BUILD_VERSION = 2
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


def search_build_id(shards: list[dict]) -> str:
    """Short id that changes whenever a deployed search shard changes."""
    digest = hashlib.sha256()
    for shard in sorted(shards, key=lambda item: str(item.get("year"))):
        digest.update(str(shard.get("year")).encode())
        digest.update(b"\0")
        digest.update(str(shard.get("hash") or "").encode())
        digest.update(b"\0")
    return digest.hexdigest()[:16]


def apply_search_build(index_path: Path, build_id: str) -> None:
    if not index_path.exists():
        return
    text = index_path.read_text(encoding="utf-8")
    if "{{ search_build }}" in text:
        text = text.replace("{{ search_build }}", build_id)
    elif 'name="search-build"' in text:
        text = re.sub(
            r'(<meta name="search-build" content=")[^"]*(")',
            rf"\1{build_id}\2",
            text,
            count=1,
        )
    else:
        text = text.replace(
            '<meta name="base-path"',
            f'<meta name="search-build" content="{build_id}" />\n    <meta name="base-path"',
            1,
        )
    index_path.write_text(text, encoding="utf-8")


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
                "page_count": int(payload.get("page_count") or 0),
                "sha256": payload.get("sha256") or "",
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


def document_filename(document: dict) -> str:
    url = document.get("url") or ""
    return url.rsplit("/", 1)[-1].lower()


_NOT_BESLUIT_RE = re.compile(
    r"bijlage|inventarislijst|handboek|werkinstructie",
    re.IGNORECASE,
)
_BESLUIT_LABEL_RE = re.compile(
    r"^(?:aanvullende?\s+|samengevoegde?\s+|formele\s+|eerste\s+|tweede\s+|derde\s+)*"
    r"(?:woo-besluit|wob-besluit|deelbesluit|beslissing|besluit)\b",
    re.IGNORECASE,
)
_DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
_BESLUIT_STEM_RE = re.compile(
    r"^(?:\d{2}-)?"
    r"(?:aanvullende?-|samengevoegde?-|formele-|eerste-|tweede-|derde-)?"
    r"(?:woo-besluit|wob-besluit|deelbesluit|beslissing|besluit)(?:-|\.|$)",
    re.IGNORECASE,
)


def is_besluit_document(document: dict) -> bool:
    """Match the decision letter itself.

    A bijlage, inventarislijst, handboek or werkinstructie stays in source order,
    even when its title mentions a besluit. The publication folder name is ignored.
    """
    label = (document.get("label") or document.get("pdf_label") or "").strip()
    filename = document_filename(document)
    stem = filename[:-5] if filename.endswith(".html") else filename
    stem = _DATE_PREFIX_RE.sub("", stem)
    if _NOT_BESLUIT_RE.search(label) or _NOT_BESLUIT_RE.search(stem):
        return False
    if _BESLUIT_LABEL_RE.search(label):
        return True
    return bool(_BESLUIT_STEM_RE.search(stem))


def canonical_pdf_url(url: str) -> str:
    return (url or "").split("?", 1)[0].strip().lower()


def find_duplicate_groups(records: list[dict]) -> list[dict]:
    """Group documents that share a file hash or the same source PDF URL."""
    parent = list(range(len(records)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    by_hash: dict[str, list[int]] = defaultdict(list)
    by_url: dict[str, list[int]] = defaultdict(list)
    for index, record in enumerate(records):
        digest = record.get("sha256") or ""
        if digest:
            by_hash[digest].append(index)
        pdf_url = canonical_pdf_url(record.get("pdf_url", ""))
        if pdf_url:
            by_url[pdf_url].append(index)

    for indexes in list(by_hash.values()) + list(by_url.values()):
        for other in indexes[1:]:
            union(indexes[0], other)

    grouped: dict[int, list[dict]] = defaultdict(list)
    for index, record in enumerate(records):
        grouped[find(index)].append(record)

    groups: list[dict] = []
    for items in grouped.values():
        if len(items) < 2:
            continue
        hashes = {item.get("sha256") or "" for item in items}
        urls = {canonical_pdf_url(item.get("pdf_url", "")) for item in items}
        if len(hashes) == 1 and "" not in hashes:
            reason = "identiek bestand"
        elif len(urls) == 1 and "" not in urls:
            reason = "zelfde bron-PDF"
        else:
            reason = "zelfde document"
        groups.append({"reason": reason, "documents": items})

    groups.sort(key=lambda group: len(group["documents"]), reverse=True)
    return groups


def mark_publication_duplicates(publications: list[dict]) -> None:
    hash_counts: Counter[str] = Counter()
    url_counts: Counter[str] = Counter()
    for publication in publications:
        for document in publication["documents"]:
            digest = document.get("sha256") or ""
            pdf_key = canonical_pdf_url(document.get("pdf_url", ""))
            document["pdf_key"] = pdf_key
            if digest:
                hash_counts[digest] += 1
            if pdf_key:
                url_counts[pdf_key] += 1

    for publication in publications:
        duplicate_count = 0
        for document in publication["documents"]:
            digest = document.get("sha256") or ""
            pdf_key = document.get("pdf_key") or ""
            if (digest and hash_counts[digest] > 1) or (pdf_key and url_counts[pdf_key] > 1):
                duplicate_count += 1
        publication["duplicate_count"] = duplicate_count


def order_publication_documents(documents: list[dict]) -> list[dict]:
    """Keep source order, but always place Woo-besluiten first."""
    indexed = list(enumerate(documents))
    indexed.sort(key=lambda item: (0 if is_besluit_document(item[1]) else 1, item[0]))
    return [document for _, document in indexed]


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
                "page_count": int(document.get("page_count") or 0),
                "sha256": document.get("sha256") or "",
                "pdf_url": document.get("pdf_url") or "",
            }
        )

    publications = list(grouped.values())
    for publication in publications:
        publication["documents"] = order_publication_documents(publication["documents"])
        publication["page_count"] = sum(item["page_count"] for item in publication["documents"])
        publication["ocr_count"] = sum(1 for item in publication["documents"] if item["ocr_used"])
    publications.sort(key=lambda item: item["date"], reverse=True)
    mark_publication_duplicates(publications)
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

    year_links = [
        f'<a class="year-chip" href="{html.escape(base_path)}publications.html">Alle jaren</a>'
    ]
    for year in sorted(by_year.keys(), reverse=True):
        year_links.append(
            f'<a class="year-chip" href="{html.escape(base_path)}publications.html?year={html.escape(year)}">{html.escape(year)}</a>'
        )

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
                    {format_number(len(publication['documents']))} documenten ·
                    {format_number(publication['page_count'])} pagina's ·
                    {format_number(publication['ocr_count'])} met OCR
                    {f" · <span class='dup-badge'>{format_number(publication['duplicate_count'])} ook elders</span>" if publication.get('duplicate_count') else ""}
                    {f" · {source_link}" if source_link else ""}
                  </div>
                  <ul class="publication-docs">{doc_links}</ul>
                </article>
                """
            )
        sections.append(
            f"""
            <section class="publications-year" data-year="{html.escape(year)}">
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
        {format_number(sum(len(pub['documents']) for pub in publications))} documenten.
        Kies een jaartal, zonder zoekscherm. Het besluit staat bovenaan, de overige documenten blijven in bronvolgorde.
      </p>
      <nav class="year-nav" aria-label="Filter op jaartal">{"".join(year_links)}</nav>
      {"".join(sections)}
    </main>
    {render_site_footer(base_path)}
    <script>
      const selectedYear = new URLSearchParams(window.location.search).get("year");
      document.querySelectorAll(".year-chip").forEach((link) => {{
        const href = new URL(link.href);
        const linkYear = href.searchParams.get("year") || "";
        const active = selectedYear ? linkYear === selectedYear : linkYear === "";
        link.classList.toggle("is-active", active);
      }});
      if (selectedYear) {{
        document.querySelectorAll(".publications-year").forEach((section) => {{
          section.hidden = section.dataset.year !== selectedYear;
        }});
      }}
    </script>
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
    duplicate_records: list[dict] = []

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

        doc_url = f"doc/{payload['publication_slug']}/{payload['pdf_slug']}.html"
        largest.append(
            {
                "title": payload.get("publication_title", ""),
                "label": payload.get("pdf_label", ""),
                "pages": page_count,
                "url": doc_url,
            }
        )
        duplicate_records.append(
            {
                "title": payload.get("publication_title", ""),
                "label": payload.get("pdf_label", ""),
                "url": doc_url,
                "publication_slug": payload.get("publication_slug", ""),
                "sha256": payload.get("sha256") or "",
                "pdf_url": payload.get("pdf_url") or "",
            }
        )

    largest.sort(key=lambda item: item["pages"], reverse=True)
    duplicate_groups = find_duplicate_groups(duplicate_records)
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
        "duplicate_groups": duplicate_groups[:30],
        "duplicate_group_count": len(duplicate_groups),
        "duplicate_document_count": sum(len(group["documents"]) for group in duplicate_groups),
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

    duplicate_groups = stats.get("duplicate_groups") or []
    if duplicate_groups:
        duplicate_rows = "".join(
            f"""
            <tr>
              <td>{html.escape(group.get("reason") or "zelfde document")}</td>
              <td>{"".join(
                  f'<div><a href="{html.escape(base_path)}{html.escape(item["url"])}">{html.escape(item["label"] or item["title"])}</a>'
                  f'<span class="dup-pub">{html.escape(item.get("title") or "")}</span></div>'
                  for item in group["documents"]
              )}</td>
            </tr>
            """
            for group in duplicate_groups
        )
        group_count = int(stats.get("duplicate_group_count", len(duplicate_groups)) or 0)
        document_count = int(stats.get("duplicate_document_count", 0) or 0)
        group_label = "groep" if group_count == 1 else "groepen"
        document_label = "document" if document_count == 1 else "documenten"
        duplicate_html = f"""
        <section class="stats-panel" id="dubbele-documenten">
          <h2>Dubbele documenten</h2>
          <p class="stats-footnote">
            {format_number(group_count)} {group_label}
            ({format_number(document_count)} {document_label})
            die hetzelfde bestand of dezelfde bron-PDF zijn.
          </p>
          <div class="table-scroll">
            <table class="stats-table">
              <thead>
                <tr><th>Overeenkomst</th><th>Documenten</th></tr>
              </thead>
              <tbody>{duplicate_rows}</tbody>
            </table>
          </div>
        </section>
        """
    else:
        duplicate_html = """
        <section class="stats-panel" id="dubbele-documenten">
          <h2>Dubbele documenten</h2>
          <p class="stats-empty">Geen documenten gevonden die hetzelfde bestand of dezelfde bron-PDF delen.</p>
        </section>
        """

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

      {duplicate_html}

      <p class="stats-footnote">
        {stats["ocr_percentage"]}% van de documenten is via OCR geëxtraheerd.
        Totaal {format_number(stats["total_characters"])} tekens geïndexeerd voor zoeken.
      </p>
    </main>
    {render_site_footer(base_path)}
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
          <a class="site-nav-link site-nav-link--github" href="https://github.com/jplattel/uwv-woo-publicaties-full-text-search" target="_blank" rel="noopener noreferrer">GitHub</a>
        </nav>
      </div>
    </header>
    """


def render_site_footer(base_path: str) -> str:
    return """
    <footer class="site-footer">
      <div class="site-footer-inner">
        <p>
          Deze site draait op GitHub Pages en wordt automatisch bijgewerkt. Bekijk de broncode en de dagelijkse
          crawl op <a href="https://github.com/jplattel/uwv-woo-publicaties-full-text-search/actions" target="_blank" rel="noopener noreferrer">GitHub</a>.
        </p>
      </div>
    </footer>
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


def render_internal_dashboard(stats: dict, publications: list[dict], base_path: str) -> str:
    latest_rows = "".join(
        f"""
        <tr>
          <td>{format_date(publication['date'])}</td>
          <td>{html.escape(publication['title'])}</td>
          <td>{format_number(len(publication['documents']))}</td>
          <td>{format_number(publication.get('page_count') or 0)}</td>
        </tr>
        """
        for publication in publications[:20]
    )
    summary_cards = [
        ("Documenten", stats.get("document_count", 0)),
        ("Publicaties", stats.get("publication_count", 0)),
        ("Pagina's", stats.get("total_pages", 0)),
        ("Dubbele groepen", stats.get("duplicate_group_count", 0)),
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
    <meta name="robots" content="noindex, nofollow" />
    <meta name="base-path" content="{html.escape(base_path)}" />
    <title>Actueel overzicht</title>
    <link rel="stylesheet" href="{html.escape(base_path)}assets/style.css" />
  </head>
  <body>
    <header class="site-header">
      <div class="site-header-inner">
        <div>
          <h1>Actueel overzicht</h1>
          <p>Intern dashboard, bijgewerkt uit de laatste crawl, niet opgenomen in de publieke navigatie.</p>
        </div>
      </div>
    </header>
    <main class="stats-main">
      <section class="stats-summary">{cards_html}</section>
      <section class="stats-panel">
        <h2>Nieuwste publicaties</h2>
        <table class="stats-table">
          <thead>
            <tr><th>Datum</th><th>Publicatie</th><th>Documenten</th><th>Pagina's</th></tr>
          </thead>
          <tbody>{latest_rows}</tbody>
        </table>
      </section>
      <section class="stats-panel">
        <h2>Documenten per publicatiejaar</h2>
        {render_bar_rows(stats.get("documents_by_year") or {}, limit=12)}
      </section>
    </main>
  </body>
</html>
"""


def format_frontmatter_value(key: str, value) -> str:
    if value is None or value == "":
        return "—"
    if key == "publication_date" or key == "retrieved_at":
        return format_date(str(value))
    if key == "ocr_used":
        return "Ja" if value else "Nee"
    if key == "page_count":
        return str(value)
    if key in {"source_page_url", "pdf_url"}:
        url = html.escape(str(value))
        label = "Open bronpagina" if key == "source_page_url" else "Download PDF"
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
    return html.escape(str(value))


def render_frontmatter(payload: dict) -> str:
    rows: list[str] = []
    seen: set[str] = set()

    for key in FRONTMATTER_ORDER:
        if key not in payload or key in HIDDEN_FRONTMATTER_KEYS:
            continue
        seen.add(key)
        label = FRONTMATTER_LABELS.get(key, key.replace("_", " ").title())
        value_html = format_frontmatter_value(key, payload.get(key))
        rows.append(f"<dt>{html.escape(label)}</dt><dd>{value_html}</dd>")

    for key, value in payload.items():
        if key in seen or key in HIDDEN_FRONTMATTER_KEYS:
            continue
        label = FRONTMATTER_LABELS.get(key, key.replace("_", " ").title())
        value_html = format_frontmatter_value(key, value)
        rows.append(f"<dt>{html.escape(label)}</dt><dd>{value_html}</dd>")

    return f'<section class="frontmatter-card"><h2>Metadata</h2><dl class="frontmatter-grid">{"".join(rows)}</dl></section>'


def _block_box(block: dict) -> tuple[float, float, float, float] | None:
    bbox = block.get("bbox")
    if not isinstance(bbox, (list, tuple)) or len(bbox) < 4:
        return None
    try:
        x0, y0, x1, y1 = (float(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3]))
    except (TypeError, ValueError):
        return None
    if x1 <= x0 or y1 <= y0:
        return None
    return x0, y0, x1, y1


def _render_flow_block(block: dict) -> str:
    text = html.escape(str(block.get("text") or "").strip())
    tag = "h2" if block.get("type") == "heading" else "p"
    return f"<{tag}>{text}</{tag}>"


def _overlap_ratio(start_a: float, end_a: float, start_b: float, end_b: float) -> float:
    overlap = min(end_a, end_b) - max(start_a, start_b)
    if overlap <= 0:
        return 0.0
    shorter = min(end_a - start_a, end_b - start_b)
    if shorter <= 0:
        return 0.0
    return overlap / shorter


def _boxes_cover_same_text(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    """True when a shorter run sits on top of a longer line, not beside it."""
    return _overlap_ratio(a[1], a[3], b[1], b[3]) >= 0.5 and _overlap_ratio(a[0], a[2], b[0], b[2]) >= 0.45


def _without_overlapping_duplicates(blocks: list[dict]) -> list[dict] | None:
    placed: list[tuple[dict, tuple[float, float, float, float]]] = []
    for block in blocks:
        box = _block_box(block)
        if box is None:
            return None
        placed.append((block, box))
    placed.sort(key=lambda item: (-len(str(item[0].get("text") or "")), -(item[1][2] - item[1][0]) * (item[1][3] - item[1][1])))
    kept: list[tuple[dict, tuple[float, float, float, float]]] = []
    for block, box in placed:
        if any(_boxes_cover_same_text(box, other) for _, other in kept):
            continue
        kept.append((block, box))
    kept.sort(key=lambda item: (item[1][1], item[1][0]))
    return [block for block, _box in kept]


def _render_layout_page(blocks: list[dict]) -> str | None:
    """Place each line in its stored box so columns and spacing stay put."""
    visible = _without_overlapping_duplicates(blocks)
    if visible is None:
        return None
    placed: list[tuple[dict, tuple[float, float, float, float]]] = []
    for block in visible:
        box = _block_box(block)
        if box is None:
            return None
        placed.append((block, box))
    if not placed:
        return None

    min_x = min(box[0] for _, box in placed)
    min_y = min(box[1] for _, box in placed)
    max_x = max(box[2] for _, box in placed)
    max_y = max(box[3] for _, box in placed)
    pad_x = max((max_x - min_x) * 0.03, 1.0)
    pad_y = max((max_y - min_y) * 0.02, 1.0)
    origin_x = min_x - pad_x
    origin_y = min_y - pad_y
    page_w = max(max_x - origin_x + pad_x, 1.0)
    page_h = max(max_y - origin_y + pad_y, 1.0)

    lines: list[str] = []
    for block, (x0, y0, x1, y1) in placed:
        text = str(block.get("text") or "").strip()
        left = (x0 - origin_x) / page_w * 100
        top = (y0 - origin_y) / page_h * 100
        box_w = (x1 - x0) / page_w * 100
        box_h = (y1 - y0) / page_h * 100
        # Size from the line height. Stretching a short run to its box width
        # paints it across the longer line underneath.
        fit_height = max(box_h * 0.85, 0.4)
        heading = " doc-line-heading" if block.get("type") == "heading" else ""
        lines.append(
            f'<span class="doc-line{heading}" style="left:{left:.2f}%;top:{top:.2f}%;'
            f'width:{box_w:.2f}%;font-size:{fit_height:.2f}cqh">{html.escape(text)}</span>'
        )

    return (
        f'<div class="doc-sheet" style="aspect-ratio:{page_w:.2f} / {page_h:.2f}">'
        + "".join(lines)
        + "</div>"
    )


def render_extracted_text(blocks: list) -> str:
    pages: dict[object, list[dict]] = {}
    order: list[object] = []
    for block in blocks or []:
        text = str(block.get("text") or "").strip()
        if not text:
            continue
        page = block.get("page")
        if page not in pages:
            pages[page] = []
            order.append(page)
        pages[page].append(block)

    if not order:
        return '<p class="doc-text-empty">Geen tekst beschikbaar voor dit document.</p>'

    parts: list[str] = []
    for index, page in enumerate(order):
        if index:
            parts.append('<hr class="doc-page-separator" />')
        page_blocks = pages[page]
        if page:
            parts.append(f'<p class="doc-page-label">Pagina {html.escape(str(page))}</p>')
        layout = _render_layout_page(page_blocks)
        if layout is not None:
            parts.append(layout)
            continue
        parts.extend(_render_flow_block(block) for block in page_blocks)
    return "\n".join(parts)


def render_doc_page(payload: dict, base_path: str) -> str:
    title = html.escape(payload.get("publication_title", "Document"))
    pdf_label = html.escape(payload.get("pdf_label", ""))
    pdf_url = html.escape(payload.get("pdf_url", ""))
    frontmatter_html = render_frontmatter(payload)
    header_html = render_site_header(title, pdf_label, base_path, active="")
    text_html = render_extracted_text(payload.get("blocks") or [])

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
      <section class="doc-panel">
        <div class="panel-heading">
          <h2>Tekst</h2>
          <a class="pdf-open-link" href="{pdf_url}" target="_blank" rel="noopener noreferrer">Open de PDF</a>
        </div>
        <div class="doc-text" id="doc-text">
          {text_html}
        </div>
      </section>
    </main>
    {render_site_footer(base_path)}
    <script>
      (function () {{
        const params = new URLSearchParams(window.location.search);
        const query = (params.get("q") || "").trim();
        const base = document.querySelector('meta[name="base-path"]')?.content || "/";
        const back = document.querySelector(".back-link");
        if (back && query) {{
          back.href = base + "?q=" + encodeURIComponent(query);
        }}
        if (!query) {{
          return;
        }}
        const terms = query.split(/\\s+/).filter(Boolean);
        if (!terms.length) {{
          return;
        }}
        const pattern = new RegExp(
          "(" + terms.map((term) => term.replace(/[.*+?^${{}}()|[\\]\\\\]/g, "\\\\$&")).join("|") + ")",
          "gi",
        );
        const root = document.querySelector("#doc-text");
        if (!root) {{
          return;
        }}
        const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
        const nodes = [];
        while (walker.nextNode()) {{
          nodes.push(walker.currentNode);
        }}
        let first = null;
        for (const node of nodes) {{
          const text = node.textContent || "";
          pattern.lastIndex = 0;
          if (!pattern.test(text)) {{
            continue;
          }}
          pattern.lastIndex = 0;
          const fragment = document.createDocumentFragment();
          let last = 0;
          for (const match of text.matchAll(pattern)) {{
            const index = match.index || 0;
            fragment.append(text.slice(last, index));
            const mark = document.createElement("mark");
            mark.textContent = match[0];
            fragment.append(mark);
            if (!first) {{
              first = mark;
            }}
            last = index + match[0].length;
          }}
          fragment.append(text.slice(last));
          node.parentNode.replaceChild(fragment, node);
        }}
        if (first) {{
          first.scrollIntoView({{ block: "center" }});
        }}
      }})();
    </script>
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
                "hash": shard_content_hash(sources),
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
                    "buildId": search_build_id(shard_manifest),
                    "indexBasePath": "search-index/",
                    "indexShards": [
                        {
                            "year": shard["year"],
                            "path": f"search-index/{shard['path']}",
                            "count": shard["count"],
                            "hash": shard["hash"],
                        }
                        for shard in shard_manifest
                    ],
                },
                handle,
                ensure_ascii=False,
            )
        log(f"  Wrote search-meta.json ({format_bytes(meta_path.stat().st_size)})")
        apply_search_build(staging_dir / "index.html", search_build_id(shard_manifest))

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

        log("  Writing internal dashboard…")
        dashboard_dir = staging_dir / "internal"
        dashboard_dir.mkdir(parents=True, exist_ok=True)
        (dashboard_dir / "actueel.html").write_text(
            render_internal_dashboard(stats, publications, base_path),
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

        if not json_path.with_suffix(".md").exists():
            missing_markdown += 1

        doc_path = staging_dir / source.output_rel
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        doc_path.write_text(
            render_doc_page(payload, base_path),
            encoding="utf-8",
        )
        label = payload.get("pdf_label") or payload.get("publication_title") or payload["pdf_slug"]
        log_progress("rendered", render_index, render_total, label)

    (staging_dir / ".nojekyll").touch()
    (staging_dir / "robots.txt").write_text(
        f"User-agent: *\nDisallow: {base_path}internal/\n",
        encoding="utf-8",
    )

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
        staging_dir / "internal" / "actueel.html",
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
