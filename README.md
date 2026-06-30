# UWV Woo PDF crawler

Daily pipeline that crawls [UWV Woo-publicaties](https://www.uwv.nl/nl/wet-open-overheid/publicaties/woo-publicaties), downloads new PDFs, extracts text (with OCR fallback), and commits structured Markdown + JSON back to this repository.

> 🚨 OCR might not be perfect so please always refer to the source! ⚠️

## What it does

1. Fetches the most recent publications from the UWV overview API (first page by default).
2. Visits each publication page and finds all linked PDFs.
3. Skips PDFs already recorded in `data/state.json` (matched by URL + SHA256).
4. Extracts text blocks from each PDF using `pdfplumber`, falling back to Tesseract OCR for scanned pages.
5. Writes paired output files:
   - `data/<publication-slug>/<pdf-slug>.json`
   - `data/<publication-slug>/<pdf-slug>.md`
6. Commits changes via GitHub Actions.

PDFs themselves are not stored in the repo.

## Local setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
```

Install system dependencies:

- macOS: `brew install tesseract tesseract-lang poppler`
- Ubuntu: `sudo apt-get install tesseract-ocr tesseract-ocr-nld poppler-utils`

## Run locally

Daily-style run (first overview page only):

```bash
uv run python -m src.main
```

One-time backfill of all overview pages:

```bash
uv run python -m src.main --max-pages 20
```

## Output format

Each JSON file contains document metadata plus ordered blocks:

```json
{
  "source_page_url": "https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2026/...",
  "pdf_url": "https://www.uwv.nl/assets-kai/files/.../woo-besluit-....pdf",
  "blocks": [
    {
      "type": "heading",
      "page": 1,
      "bbox": [72.0, 90.0, 400.0, 110.0],
      "text": "Woo-besluit",
      "source": "text"
    }
  ]
}
```

Each Markdown file includes the same metadata in YAML frontmatter and backlinks to the original publication page and PDF at the bottom.

## GitHub Actions

Workflow: `.github/workflows/daily-crawl.yml`

- Runs daily at 06:00 UTC
- Can be triggered manually with an optional `max_pages` input
- Commits only when `data/` changes

## GitHub Pages search site

The repository includes a static search site built from the extracted documents.

Build locally:

```bash
uv run python scripts/build_site.py --base-path /
uv run python -m http.server --directory docs 8080
```

Open `http://localhost:8080/`. For a project site base path, pass e.g. `--base-path /uwv-woo-verzoeken/`.

Deploy workflow: `.github/workflows/pages.yml`

- Rebuilds the site when `data/` changes
- Deploys to GitHub Pages via Actions
- Enable in repo settings: **Settings → Pages → Build and deployment → GitHub Actions**

The site provides full-text search across all JSON extracts and links back to the original UWV publication pages and PDFs.
