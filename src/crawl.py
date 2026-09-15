from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

import requests
import urllib3
from bs4 import BeautifulSoup

from src.config import Settings
from src.utils import absolute_url, pdf_slug, publication_slug, sha256_file


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
JSON_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}


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
    session.verify = settings.verify_ssl
    if not settings.verify_ssl:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Referer": settings.referer,
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }
    )
    return session


def _cache_bust_params() -> dict[str, str]:
    return {"_": str(int(time.time() * 1000))}


def _publication_from_item(item: dict[str, Any], settings: Settings) -> Publication | None:
    url = (item.get("url") or "").strip()
    if not url:
        return None
    return Publication(
        title=(item.get("title") or "").strip(),
        url=absolute_url(settings.host, url),
        date=(item.get("date") or "").strip(),
        publication_type=(item.get("type") or "").strip(),
    )


def parse_listing_seed(html: str, settings: Settings) -> tuple[list[Publication], str]:
    """Parse newest publications from the SSR listing page.

    The UWV site embeds the first overview page in ``first-results``. GitHub
    Actions runners can otherwise receive a stale cached ``cluster=1`` API
    response that omits those newest items.
    """
    soup = BeautifulSoup(html, "lxml")
    element = soup.find("mdgs-dynamic-list")
    if element is None:
        return [], ""

    entry_id = (element.get("entry-id") or "").strip()
    raw = element.get("first-results") or ""
    if not raw:
        return [], entry_id

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return [], entry_id

    publications: list[Publication] = []
    for item in payload.get("results") or []:
        publication = _publication_from_item(item, settings)
        if publication is not None:
            publications.append(publication)
    return publications, entry_id


def _log_overview(publications: list[Publication], seeded: int) -> None:
    dates = [item.date for item in publications if item.date]
    date_range = f"{min(dates)} .. {max(dates)}" if dates else "unknown"
    print(
        f"Overview: {len(publications)} publication(s) "
        f"({seeded} from listing page), {date_range}"
    )


def fetch_publications(
    session: requests.Session,
    settings: Settings,
    max_pages: int = 1,
) -> list[Publication]:
    publications: list[Publication] = []
    seen_urls: set[str] = set()
    entry_id = ""
    seeded = 0

    try:
        listing_response = session.get(
            settings.referer,
            params=_cache_bust_params(),
            timeout=60,
        )
        listing_response.raise_for_status()
        seed, entry_id = parse_listing_seed(listing_response.text, settings)
        for publication in seed:
            if publication.url in seen_urls:
                continue
            publications.append(publication)
            seen_urls.add(publication.url)
        seeded = len(publications)
    except requests.RequestException as exc:
        print(f"Failed to fetch overview listing page {settings.referer}: {exc}")

    for cluster in range(1, max_pages + 1):
        body: dict[str, Any] = {"cluster": cluster}
        if entry_id:
            body["entryId"] = entry_id
        response = session.post(
            settings.overview_url,
            params=_cache_bust_params(),
            json=body,
            headers=JSON_HEADERS,
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()

        for item in payload.get("results") or []:
            publication = _publication_from_item(item, settings)
            if publication is None or publication.url in seen_urls:
                continue
            publications.append(publication)
            seen_urls.add(publication.url)

        has_more = bool((payload.get("meta") or {}).get("cluster", {}).get("hasmore"))
        if not has_more or cluster == max_pages:
            break
        time.sleep(settings.request_delay)

    _log_overview(publications, seeded)
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

        if not candidates:
            print(f"No PDFs found on {publication.page_url}")
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
