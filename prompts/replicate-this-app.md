# Prompt: replicate the UWV Woo full-text app

Paste everything below the line into a coding agent, in an empty directory. Do not paste this heading.

---

Build a small, reproducible app that crawls public UWV Woo decisions, extracts their text, and publishes a static Dutch search site. Match the behavior below. Prefer a clear layout over a line-by-line copy of any existing repository. The published HTML is a finding aid. The PDF on uwv.nl stays the source of truth.

## Product

UWV publishes Wet open overheid (Woo) decisions as PDFs on a listing page. That listing is not a full-text search engine, and some PDFs are scans with no usable text layer. This app:

1. Discovers new publication pages and their PDF links.
2. Downloads each PDF only long enough to extract text, then deletes the file. Do not commit PDF bytes.
3. Reads an existing text layer with pdfplumber. Runs OCR only for a page whose text layer is too short.
4. Writes one Markdown file and one JSON file per PDF, plus a state file so unchanged PDFs are skipped.
5. Builds a static site that searches the extracts in the browser and links every document back to the UWV publication page and the original PDF.

The interface language is Dutch. The site is not an official UWV site. Say that on the explanatory page.

## Stack

- Python 3.12, managed with uv. Dependencies: requests, beautifulsoup4, lxml, pdfplumber, pdf2image, paddleocr, onnxruntime, PyYAML, markdown.
- System packages for the crawl: poppler-utils, and the libraries PaddleOCR needs (libgl1, libglib2.0-0, libgomp1).
- Node only for the search index. Use MiniSearch 7.1.0.
- Static output goes to `docs/` and is deployed with GitHub Pages. No application server in production.

## Configuration

`config/sources.yml`:

- `host`: `https://www.uwv.nl`
- `overview_api`: `/api/overview/nl/wet-open-overheid/publicaties/woo-publicaties`
- `referer`: `https://www.uwv.nl/nl/wet-open-overheid/publicaties/woo-publicaties`
- `ocr_lang`: `nl` (accept the old Tesseract code `nld` as an alias for `nl`)
- `min_chars_per_page`: `40`
- `request_delay`: `0.5` seconds between publication and PDF requests
- `verify_ssl`: configurable, default `false` because this upstream has failed certificate verification

CLI, `python -m src.main`:

- `--config`, default `config/sources.yml`
- `--data-dir`, default `data`
- `--max-pages`, default `1` (daily run). Higher values backfill overview clusters.
- `--limit`, optional cap on the number of publications, newest first.

## Crawl

Use a normal browser User-Agent and the configured referer. Cache-bust GETs and POSTs with a millisecond query parameter.

1. GET the listing page. Parse the `mdgs-dynamic-list` element. Read `entry-id` and the JSON in `first-results`. Those embedded results are the newest publications. Trust them even when the overview API is stale.
2. POST `{ "cluster": n, "entryId": entry-id }` to `{host}{overview_api}` for cluster 1 through `max-pages`. Stop early when `meta.cluster.hasmore` is false. Deduplicate publications by URL.
3. A publication has title, absolute URL, date, and type. Its slug is `{YYYY-MM-DD}-{slug-of-the-url-basename}`.
4. GET each publication page. Collect PDF links from `bgl-list-link` (`link-url`, `link-label`) first. If that finds nothing, fall back to anchors whose href ends in `.pdf`.
5. A PDF slug is `{YYYY-MM-DD}-{slug-of-the-pdf-filename-stem}`.
6. Skip a PDF when both output files already exist, the JSON `pdf_url` matches, and the SHA-256 matches the downloaded file. If the files exist and match the URL but state is missing, record state and do not re-extract. Reprocess when the SHA-256 changed.
7. Download to a temp directory. On success or failure, delete the temp PDF. One failed publication or PDF must not abort the run. Log it and continue. Exit 0 after a partial run.
8. After each successful PDF, update `data/state.json` immediately. Key it by PDF URL. Store publication slug, pdf slug, sha256, retrieved_at (UTC, seconds), and the md/json paths.

## Extraction

For each page, in order:

- Use pdfplumber `extract_words` (`use_text_flow=True`). Group words on the same line and font size into one block. Record the PDF bounding box, 1-based page number, text, and `source: "text"`.
- Classify a short line as `heading` when it is clearly taller than the average line, or when it is short and fully uppercase. Otherwise `paragraph`. Drop empty blocks.
- If the page has fewer than `min_chars_per_page` characters from the text layer, rasterize with Poppler (pdf2image) and OCR that page with PaddleOCR: Dutch, ONNX Runtime, recognition score threshold 0.5. Drop lines under 0.5. Those blocks use `source: "ocr"`. Set `ocr_used` on the document if any page took this path.
- Do not summarize, translate, or rewrite the text. Do not send the text through a language model. If the PDF text layer is wrong, reproduce that layer. OCR is only a fallback for an empty layer, and it can be wrong.

## Files written per PDF

Directory: `data/{publication-slug}/`.

JSON:

- metadata: source_id (`{publication-slug}/{pdf-slug}`), publication_slug, pdf_slug, source_page_url, pdf_url, publication_title, publication_date, publication_type, pdf_label, retrieved_at, sha256, page_count, ocr_used
- `blocks`: ordered list of `{type, page, bbox, text, source}`

Markdown: the same metadata as YAML frontmatter, blocks as text (`##` for headings), and a footer link:

`Bron: [{publication title}]({source page}) · [{pdf label}]({pdf url})`

## Static site

`python scripts/build_site.py` reads `data/**/*.json` and writes `docs/`. Support `--base-path` and the env var `SITE_BASE_PATH` (GitHub Pages project sites use `/{repo-name}/`).

Pages, all in Dutch:

- Search (`index.html`). Client-side only. MiniSearch in a web worker, one shard per publication year under `search-index/{year}.json`, described by `search-meta.json`. Cache shards in IndexedDB under `year:hash`, and cache-bust with that hash. Filters: year range, publication type, OCR only. Sort by relevance, newest, or oldest. Show a snippet with the query marked. 25 results per page. Debounce input.
- Publications, grouped by year.
- Statistics computed from the extracts.
- About: this is an unofficial finding aid, OCR is imperfect, always check the source PDF.
- Why (`waarom.html`): a page a critic can read. State plainly that the site is not UWV and not the legal text. Explain that pdfplumber reads the PDF text layer (the same characters a PDF reader can select), that OCR runs only under 40 characters and is labeled `ocr`, and that every document links back to the UWV page and the original PDF. The PDF is not stored in the repo.
- One HTML page per document. Show metadata with links labeled “Open bronpagina” and “Download PDF”. Show extracted text in page order with a horizontal rule between pages. Put another “Open de PDF” link on the text panel. Collapse text boxes that cover the same line twice so a word is not printed twice. Do not change the PDF. Do not embed the PDF in an iframe. If the visitor arrived with `?q=`, highlight the query and scroll to the first hit.
- A small internal dashboard at `internal/actueel.html` with `noindex` and `Disallow` in `robots.txt`. Leave it out of the public nav.

Search index fields: publication title, pdf label, and the first 6000 characters of text. Store a 400-character preview. Boost the title over the label over the body. Prefix search and light fuzzy matching.

Build into a staging directory and swap it into `docs/` only when the required pages exist, including the search index. An incremental rebuild keyed by file hashes is welcome, not required for the first working version.

## Automation

Two GitHub Actions workflows:

- Daily crawl at 06:00 UTC, plus manual dispatch with a `max_pages` input. Install poppler and the OCR libraries, `uv sync --frozen`, run `python -m src.main`. Commit and push `data/` only when it changed, as `github-actions[bot]`, message `chore: update Woo PDF extracts`.
- Pages workflow on that commit, and on pushes to `main` that touch data, site, scripts, or the lockfile. Build `docs/` and deploy with `actions/deploy-pages`.

## Tests

Cover at least:

- Listing HTML with `first-results` yields those publications, and later API results do not duplicate them.
- A page with a text layer produces `source: "text"` blocks and does not call OCR.
- A page under 40 characters uses OCR blocks with `source: "ocr"`.
- An unchanged PDF whose JSON `pdf_url` matches is skipped. A changed SHA-256 is not.
- A document page contains the source URL, the PDF URL, no iframe, and the extracted text.
- The public header links to `waarom.html`.

## Done when

- `uv run python -m src.main --max-pages 1 --limit 1` can process a real publication into `data/` and leaves no PDF behind.
- The Markdown footer and the HTML document page both link to the UWV page and the original PDF.
- `uv run python scripts/build_site.py --base-path /` serves a search page from `docs/` that finds a word you know is in an extract.
- OCR is visibly distinguished from the text layer, and the Why page tells a reader to verify OCR against the PDF.
