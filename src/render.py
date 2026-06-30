from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from src.extract import Block


@dataclass(frozen=True)
class DocumentMetadata:
    source_id: str
    publication_slug: str
    pdf_slug: str
    source_page_url: str
    pdf_url: str
    publication_title: str
    publication_date: str
    publication_type: str
    pdf_label: str
    retrieved_at: str
    sha256: str
    page_count: int
    ocr_used: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "publication_slug": self.publication_slug,
            "pdf_slug": self.pdf_slug,
            "source_page_url": self.source_page_url,
            "pdf_url": self.pdf_url,
            "publication_title": self.publication_title,
            "publication_date": self.publication_date,
            "publication_type": self.publication_type,
            "pdf_label": self.pdf_label,
            "retrieved_at": self.retrieved_at,
            "sha256": self.sha256,
            "page_count": self.page_count,
            "ocr_used": self.ocr_used,
        }


def _block_to_markdown(block: Block) -> str:
    if block.type == "heading":
        return f"## {block.text}"
    return block.text


def render_document(
    metadata: DocumentMetadata,
    blocks: list[Block],
    data_dir: Path,
) -> tuple[Path, Path]:
    output_dir = data_dir / metadata.publication_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"{metadata.pdf_slug}.json"
    md_path = output_dir / f"{metadata.pdf_slug}.md"

    payload = {
        **metadata.to_dict(),
        "blocks": [block.to_dict() for block in blocks],
    }

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    frontmatter = metadata.to_dict()
    body_lines = [_block_to_markdown(block) for block in blocks if block.text.strip()]
    body = "\n\n".join(body_lines)
    footer = (
        f"\n\n---\n\n"
        f"Bron: [{metadata.publication_title}]({metadata.source_page_url}) · "
        f"[{metadata.pdf_label}]({metadata.pdf_url})"
    )

    md_content = (
        "---\n"
        + yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
        + "---\n\n"
        + body
        + footer
        + "\n"
    )

    md_path.write_text(md_content, encoding="utf-8")
    return md_path, json_path
