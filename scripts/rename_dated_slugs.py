#!/usr/bin/env python3
"""One-off migration: rename data dirs/files to YYYY-MM-DD-prefixed slugs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.utils import slug_with_date  # noqa: E402

DATA_DIR = ROOT / "data"
STATE_PATH = DATA_DIR / "state.json"
DATED_DIR_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def update_markdown(path: Path, metadata: dict) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing frontmatter in {path}")

    _, rest = text.split("---\n", 1)
    body = rest.split("\n", 1)[1] if "\n" in rest else ""
    return (
        "---\n"
        + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False)
        + "---\n\n"
        + body
    )


def metadata_from_payload(payload: dict) -> dict:
    return {
        "source_id": payload["source_id"],
        "publication_slug": payload["publication_slug"],
        "pdf_slug": payload["pdf_slug"],
        "source_page_url": payload["source_page_url"],
        "pdf_url": payload["pdf_url"],
        "publication_title": payload["publication_title"],
        "publication_date": payload["publication_date"],
        "publication_type": payload["publication_type"],
        "pdf_label": payload["pdf_label"],
        "retrieved_at": payload["retrieved_at"],
        "sha256": payload["sha256"],
        "page_count": payload["page_count"],
        "ocr_used": payload["ocr_used"],
    }


def main() -> int:
    if not DATA_DIR.exists():
        print("No data directory found.")
        return 1

    planned: list[tuple[Path, Path, Path, dict]] = []

    for old_dir in sorted(p for p in DATA_DIR.iterdir() if p.is_dir()):
        if DATED_DIR_RE.match(old_dir.name):
            continue

        for json_path in sorted(old_dir.glob("*.json")):
            payload = load_json(json_path)
            publication_date = payload.get("publication_date") or ""
            old_publication_slug = payload.get("publication_slug") or old_dir.name
            old_pdf_slug = payload.get("pdf_slug") or json_path.stem

            new_publication_slug = slug_with_date(old_publication_slug, publication_date)
            new_pdf_slug = slug_with_date(old_pdf_slug, publication_date)
            new_dir = DATA_DIR / new_publication_slug

            payload["publication_slug"] = new_publication_slug
            payload["pdf_slug"] = new_pdf_slug
            payload["source_id"] = f"{new_publication_slug}/{new_pdf_slug}"

            new_json_path = new_dir / f"{new_pdf_slug}.json"
            old_md_path = old_dir / f"{old_pdf_slug}.md"
            planned.append((json_path, old_md_path, new_json_path, payload))

    if not planned:
        print("Nothing to rename.")
        return 0

    new_paths = {item[2] for item in planned}
    new_md_paths = {
        item[2].with_suffix(".md")
        for item in planned
        if item[1].exists()
    }
    for target in new_paths | new_md_paths:
        if target.exists():
            raise SystemExit(f"Refusing to overwrite existing file: {target}")

    dirs_seen: set[str] = set()
    for old_json_path, old_md_path, new_json_path, payload in planned:
        new_md_path = new_json_path.with_suffix(".md")
        metadata = metadata_from_payload(payload)

        save_json(new_json_path, payload)
        if old_md_path.exists():
            new_md_path.write_text(update_markdown(old_md_path, metadata), encoding="utf-8")

        old_json_path.unlink(missing_ok=True)
        if old_md_path.exists() and old_md_path != new_md_path:
            old_md_path.unlink(missing_ok=True)

        old_dir_name = old_json_path.parent.name
        if old_dir_name not in dirs_seen:
            print(f"{old_dir_name} -> {payload['publication_slug']}")
            dirs_seen.add(old_dir_name)

    for old_dir in sorted(p for p in DATA_DIR.iterdir() if p.is_dir()):
        if DATED_DIR_RE.match(old_dir.name):
            continue
        if not any(old_dir.iterdir()):
            old_dir.rmdir()
            print(f"Removed empty directory {old_dir.name}")

    if STATE_PATH.exists():
        state = load_json(STATE_PATH)
        payload_by_pdf_url = {
            item[3]["pdf_url"]: item[3]
            for item in planned
        }
        for pdf_url, entry in state.items():
            payload = payload_by_pdf_url.get(pdf_url)
            if payload:
                entry["publication_slug"] = payload["publication_slug"]
                entry["pdf_slug"] = payload["pdf_slug"]
                entry["paths"] = {
                    "md": str(Path("data") / payload["publication_slug"] / f"{payload['pdf_slug']}.md"),
                    "json": str(Path("data") / payload["publication_slug"] / f"{payload['pdf_slug']}.json"),
                }
            else:
                date = entry.get("publication_date", "")
                entry["publication_slug"] = slug_with_date(entry["publication_slug"], date)
                entry["pdf_slug"] = slug_with_date(entry["pdf_slug"], date)
                entry["paths"] = {
                    "md": str(Path("data") / entry["publication_slug"] / f"{entry['pdf_slug']}.md"),
                    "json": str(Path("data") / entry["publication_slug"] / f"{entry['pdf_slug']}.json"),
                }
        save_json(STATE_PATH, state)

    print(f"Migrated {len(planned)} document(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
