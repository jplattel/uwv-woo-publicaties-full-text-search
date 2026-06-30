from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class Settings:
    host: str
    overview_api: str
    referer: str
    ocr_lang: str
    min_chars_per_page: int
    request_delay: float
    data_dir: Path
    config_path: Path

    @property
    def overview_url(self) -> str:
        return f"{self.host.rstrip('/')}{self.overview_api}"


def load_settings(config_path: Path, data_dir: Path | None = None) -> Settings:
    with config_path.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    return Settings(
        host=raw["host"],
        overview_api=raw["overview_api"],
        referer=raw["referer"],
        ocr_lang=raw.get("ocr_lang", "nld"),
        min_chars_per_page=int(raw.get("min_chars_per_page", 40)),
        request_delay=float(raw.get("request_delay", 0.5)),
        data_dir=data_dir or Path("data"),
        config_path=config_path,
    )
