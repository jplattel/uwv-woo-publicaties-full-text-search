from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class ProcessedPdf:
    pdf_url: str
    publication_slug: str
    pdf_slug: str
    sha256: str
    retrieved_at: str
    md_path: str
    json_path: str


class StateStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._data: dict[str, dict[str, Any]] = {}
        self.load()

    def load(self) -> None:
        if self.path.exists():
            with self.path.open(encoding="utf-8") as handle:
                self._data = json.load(handle)
        else:
            self._data = {}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(self._data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")

    def should_process(self, pdf_url: str, sha256: str) -> bool:
        existing = self._data.get(pdf_url)
        if not existing:
            return True
        return existing.get("sha256") != sha256

    def output_paths(
        self,
        data_dir: Path,
        publication_slug: str,
        pdf_slug: str,
    ) -> tuple[Path, Path]:
        output_dir = data_dir / publication_slug
        return output_dir / f"{pdf_slug}.md", output_dir / f"{pdf_slug}.json"

    def outputs_exist(self, md_path: Path, json_path: Path) -> bool:
        return md_path.is_file() and json_path.is_file()

    def outputs_match(self, pdf_url: str, md_path: Path, json_path: Path) -> bool:
        if not self.outputs_exist(md_path, json_path):
            return False
        try:
            with json_path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, json.JSONDecodeError):
            return False
        return payload.get("pdf_url") == pdf_url

    def register_existing(
        self,
        pdf_url: str,
        publication_slug: str,
        pdf_slug: str,
        md_path: Path,
        json_path: Path,
        sha256: str = "",
    ) -> bool:
        if not self.outputs_exist(md_path, json_path):
            return False

        resolved_sha256 = sha256
        if not resolved_sha256:
            try:
                with json_path.open(encoding="utf-8") as handle:
                    resolved_sha256 = json.load(handle).get("sha256") or ""
            except (OSError, json.JSONDecodeError):
                resolved_sha256 = ""

        self.mark_processed(
            ProcessedPdf(
                pdf_url=pdf_url,
                publication_slug=publication_slug,
                pdf_slug=pdf_slug,
                sha256=resolved_sha256,
                retrieved_at=self._data.get(pdf_url, {}).get("retrieved_at") or self.now_iso(),
                md_path=str(md_path),
                json_path=str(json_path),
            )
        )
        return True

    def _read_sha256(self, json_path: Path) -> str:
        try:
            with json_path.open(encoding="utf-8") as handle:
                return json.load(handle).get("sha256") or ""
        except (OSError, json.JSONDecodeError):
            return ""

    def should_skip(
        self,
        pdf_url: str,
        sha256: str,
        md_path: Path,
        json_path: Path,
    ) -> bool:
        if self.outputs_exist(md_path, json_path) and self.outputs_match(
            pdf_url, md_path, json_path
        ):
            existing_sha256 = self._read_sha256(json_path)
            if existing_sha256 == sha256:
                self.register_existing(
                    pdf_url=pdf_url,
                    publication_slug=md_path.parent.name,
                    pdf_slug=json_path.stem,
                    md_path=md_path,
                    json_path=json_path,
                    sha256=sha256,
                )
                return True
            return False

        return not self.should_process(pdf_url, sha256)

    def mark_processed(self, record: ProcessedPdf) -> None:
        self._data[record.pdf_url] = {
            "publication_slug": record.publication_slug,
            "pdf_slug": record.pdf_slug,
            "sha256": record.sha256,
            "retrieved_at": record.retrieved_at,
            "paths": {
                "md": record.md_path,
                "json": record.json_path,
            },
        }

    @staticmethod
    def now_iso() -> str:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
