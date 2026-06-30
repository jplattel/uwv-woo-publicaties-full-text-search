from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

import requests
from bs4 import BeautifulSoup

from src.config import Settings
from src.utils import absolute_url, pdf_slug, publication_slug, sha256_file


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class Publication:
    title: str
    url: str
    date: str
    publication_type: str

    @property
    def page_url(self) -> str:
        return self.url

    @property
    def slug(self) -> str:
        return publication_slug(self.url, self.date)


@dataclass(frozen=True)
class PdfCandidate:
    publication: Publication
    pdf_url: str
    pdf_label: str
    publication_page_url: str

    @property
    def slug(self) -> str:
        return pdf_slug(self.pdf_url, self.publication.date)


@dataclass(frozen=True)
class DownloadedPdf:
    candidate: PdfCandidate
    local_path: Path
    sha256: str


def create_session(settings: Settings) -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Referer": settings.referer,
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
        }
    )
    return session


def fetch_publications(
    session: requests.Session,
    settings: Settings,
    max_pages: int = 1,
) -> list[Publication]:
    publications: list[Publication] = []
    cluster = 1

    while cluster <= max_pages:
        response = session.post(
            settings.overview_url,
            json={"cluster": cluster},
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        results = payload.get("results") or []

        for item in results:
            url = item.get("url") or ""
            if not url:
                continue
            publications.append(
                Publication(
                    title=(item.get("title") or "").strip(),
                    url=absolute_url(settings.host, url),
                    date=(item.get("date") or "").strip(),
                    publication_type=(item.get("type") or "").strip(),
                )
            )

        has_more = bool((payload.get("meta") or {}).get("cluster", {}).get("hasmore"))
        if not has_more or cluster >= max_pages:
            break

        cluster += 1
        time.sleep(settings.request_delay)

    return publications


def _extract_pdf_links(soup: BeautifulSoup, settings: Settings) -> list[tuple[str, str]]:
    links: list[tuple[str, str]] = []

    for element in soup.find_all("bgl-list-link"):
        pdf_url = (element.get("link-url") or "").strip()
        label = (element.get("link-label") or "").strip()
        if pdf_url.lower().endswith(".pdf"):
            links.append((absolute_url(settings.host, pdf_url), label))

    if links:
        return links

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        if href.lower().endswith(".pdf"):
            label = anchor.get_text(" ", strip=True) or Path(href).name
            links.append((absolute_url(settings.host, href), label))

    return links


def fetch_pdf_candidates(
    session: requests.Session,
    settings: Settings,
    publication: Publication,
) -> list[PdfCandidate]:
    response = session.get(publication.page_url, timeout=60)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    candidates: list[PdfCandidate] = []
    for pdf_url, label in _extract_pdf_links(soup, settings):
        candidates.append(
            PdfCandidate(
                publication=publication,
                pdf_url=pdf_url,
                pdf_label=label or pdf_slug(pdf_url, publication.date),
                publication_page_url=publication.page_url,
            )
        )
    return candidates


def download_pdf(
    session: requests.Session,
    candidate: PdfCandidate,
    temp_dir: Path,
) -> DownloadedPdf:
    response = session.get(candidate.pdf_url, timeout=120)
    response.raise_for_status()

    filename = f"{candidate.publication.slug}__{candidate.slug}.pdf"
    local_path = temp_dir / filename
    local_path.write_bytes(response.content)

    return DownloadedPdf(
        candidate=candidate,
        local_path=local_path,
        sha256=sha256_file(local_path),
    )


def iter_new_pdfs(
    session: requests.Session,
    settings: Settings,
    state,
    temp_dir: Path,
    max_pages: int = 1,
) -> Iterator[DownloadedPdf]:
    publications = fetch_publications(session, settings, max_pages=max_pages)

    for publication in publications:
        time.sleep(settings.request_delay)
        try:
            candidates = fetch_pdf_candidates(session, settings, publication)
        except requests.RequestException as exc:
            print(f"Failed to fetch publication page {publication.page_url}: {exc}")
            continue

        for candidate in candidates:
            md_path, json_path = state.output_paths(
                settings.data_dir,
                candidate.publication.slug,
                candidate.slug,
            )
            if state.outputs_match(candidate.pdf_url, md_path, json_path):
                state.register_existing(
                    pdf_url=candidate.pdf_url,
                    publication_slug=candidate.publication.slug,
                    pdf_slug=candidate.slug,
                    md_path=md_path,
                    json_path=json_path,
                )
                state.save()
                print(f"Skipping existing output for {candidate.pdf_url}")
                continue

            try:
                downloaded = download_pdf(session, candidate, temp_dir)
            except requests.RequestException as exc:
                print(f"Failed to download PDF {candidate.pdf_url}: {exc}")
                continue

            if state.should_skip(
                candidate.pdf_url,
                downloaded.sha256,
                md_path,
                json_path,
            ):
                downloaded.local_path.unlink(missing_ok=True)
                print(f"Skipping unchanged PDF {candidate.pdf_url}")
                continue

            yield downloaded
            time.sleep(settings.request_delay)
