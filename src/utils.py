from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import PurePosixPath
from urllib.parse import urljoin, urlparse


def slugify(text: str, max_length: int = 120) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^\w\s-]", "", ascii_text.lower())
    slug = re.sub(r"[-\s]+", "-", cleaned).strip("-")
    return (slug or "untitled")[:max_length]


def date_prefix(date: str) -> str:
    if not date:
        return ""
    match = re.match(r"(\d{4}-\d{2}-\d{2})", date)
    if match:
        return match.group(1)
    return slugify(date)[:10]


def slug_with_date(base_slug: str, date: str) -> str:
    prefix = date_prefix(date)
    if prefix:
        return f"{prefix}-{base_slug}"
    return base_slug


def publication_slug(url: str, date: str = "") -> str:
    path = urlparse(url).path.rstrip("/")
    return slug_with_date(slugify(PurePosixPath(path).name), date)


def pdf_slug(pdf_url: str, date: str = "") -> str:
    path = urlparse(pdf_url).path
    name = PurePosixPath(path).stem
    return slug_with_date(slugify(name), date)


def absolute_url(host: str, url: str) -> str:
    return urljoin(host.rstrip("/") + "/", url.lstrip("/"))


def sha256_file(path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
