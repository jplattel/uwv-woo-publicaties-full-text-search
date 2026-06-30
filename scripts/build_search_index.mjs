#!/usr/bin/env node
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import MiniSearch from "minisearch";

const TEXT_INDEX_LENGTH = 6000;
const TEXT_PREVIEW_LENGTH = 400;

export const SEARCH_OPTIONS = {
  fields: ["publication_title", "pdf_label", "text"],
  storeFields: [
    "publication_title",
    "pdf_label",
    "publication_date",
    "publication_type",
    "ocr_used",
    "publication_slug",
    "url",
    "text_preview",
  ],
  searchOptions: {
    prefix: true,
    fuzzy: 0.2,
    boost: { publication_title: 2, pdf_label: 1.5 },
  },
};

const inputPath = process.argv[2];
const outputDir = process.argv[3];
const onlyYears = process.argv[4] ? new Set(process.argv[4].split(",")) : null;

if (!inputPath || !outputDir) {
  console.error("Usage: build_search_index.mjs <documents.json> <output-dir/> [years]");
  process.exit(1);
}

function yearFromDate(value) {
  const match = String(value || "").match(/^(\d{4})/);
  return match ? match[1] : "unknown";
}

function prepareDocument(document) {
  const fullText = document.text || "";
  return {
    id: document.id,
    publication_slug: document.publication_slug,
    publication_title: document.publication_title || "",
    pdf_label: document.pdf_label || "",
    publication_date: document.publication_date || "",
    publication_type: document.publication_type || "",
    ocr_used: Boolean(document.ocr_used),
    url: document.url || "",
    text: fullText.slice(0, TEXT_INDEX_LENGTH),
    text_preview: fullText.slice(0, TEXT_PREVIEW_LENGTH),
  };
}

const rawDocuments = JSON.parse(readFileSync(inputPath, "utf8"));
const byYear = new Map();

for (const document of rawDocuments) {
  const prepared = prepareDocument(document);
  const year = yearFromDate(prepared.publication_date);
  if (!byYear.has(year)) {
    byYear.set(year, []);
  }
  byYear.get(year).push(prepared);
}

mkdirSync(outputDir, { recursive: true });

const shards = [];
let totalBytes = 0;

for (const year of [...byYear.keys()].sort()) {
  if (onlyYears && !onlyYears.has(year)) {
    continue;
  }
  const documents = byYear.get(year);
  const miniSearch = new MiniSearch(SEARCH_OPTIONS);
  miniSearch.addAll(documents);

  const filename = `${year}.json`;
  const outputPath = join(outputDir, filename);
  const payload = JSON.stringify({
    year,
    count: documents.length,
    index: miniSearch.toJSON(),
    options: SEARCH_OPTIONS,
  });

  writeFileSync(outputPath, payload);
  totalBytes += payload.length;
  shards.push({ year, path: filename, count: documents.length });
  console.log(`  shard ${year}: ${documents.length} docs, ${(payload.length / 1024 / 1024).toFixed(1)} MB`);
}

if (!onlyYears) {
  writeFileSync(
    join(outputDir, "manifest.json"),
    JSON.stringify({
      version: 1,
      documentCount: rawDocuments.length,
      options: SEARCH_OPTIONS,
      shards,
    }),
  );
}

console.log(
  onlyYears
    ? `Indexed ${shards.length} shard(s) for ${[...onlyYears].join(", ")}`
    : `Indexed ${rawDocuments.length} documents in ${shards.length} shards (${(totalBytes / 1024 / 1024).toFixed(1)} MB total)`,
);
