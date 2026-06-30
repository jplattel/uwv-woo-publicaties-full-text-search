const BASE = document.querySelector('meta[name="base-path"]')?.content || "/";

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function highlight(text, terms) {
  if (!terms.length) {
    return escapeHtml(text);
  }
  const pattern = new RegExp(
    `(${terms.map((term) => term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})`,
    "gi",
  );
  return escapeHtml(text).replace(pattern, "<mark>$1</mark>");
}

function formatDate(value) {
  if (!value) {
    return "";
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  return date.toLocaleDateString("nl-NL", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

function snippetAroundMatch(text, terms, radius = 140) {
  const lower = text.toLowerCase();
  let index = -1;
  for (const term of terms) {
    const found = lower.indexOf(term.toLowerCase());
    if (found !== -1) {
      index = found;
      break;
    }
  }
  if (index === -1) {
    return text.slice(0, radius * 2);
  }
  const start = Math.max(0, index - radius);
  const end = Math.min(text.length, index + radius);
  const prefix = start > 0 ? "…" : "";
  const suffix = end < text.length ? "…" : "";
  return `${prefix}${text.slice(start, end)}${suffix}`;
}

async function initSearch() {
  const input = document.querySelector("#search-input");
  const resultsEl = document.querySelector("#results");
  const countEl = document.querySelector("#result-count");
  const suggestionsEl = document.querySelector("#search-suggestions");
  if (!input || !resultsEl || !countEl) {
    return;
  }

  const response = await fetch(`${BASE}search-index.json`);
  const payload = await response.json();
  const documents = payload.documents || [];
  const suggestions = payload.suggestions || [
    "WIA beoordeling",
    "loonsanctie",
    "bezwaar beroep",
    "fraudeonderzoek",
    "Ziektewet",
  ];

  if (suggestionsEl) {
    suggestionsEl.innerHTML = `
      <span class="search-suggestions-label">Suggesties:</span>
      ${suggestions
        .map(
          (term) =>
            `<button type="button" class="suggestion-chip" data-term="${escapeHtml(term)}">${escapeHtml(term)}</button>`,
        )
        .join("")}
    `;
    suggestionsEl.addEventListener("click", (event) => {
      const button = event.target.closest(".suggestion-chip");
      if (!button) {
        return;
      }
      input.value = button.dataset.term || "";
      input.focus();
      renderResults(input.value);
    });
  }

  const miniSearch = new MiniSearch({
    fields: ["publication_title", "pdf_label", "text"],
    storeFields: [
      "publication_title",
      "pdf_label",
      "publication_date",
      "url",
      "source_page_url",
      "pdf_url",
      "text",
    ],
    searchOptions: {
      prefix: true,
      fuzzy: 0.2,
      boost: { publication_title: 2, pdf_label: 1.5 },
    },
  });
  miniSearch.addAll(documents);

  countEl.textContent = `${documents.length} documenten doorzoekbaar`;

  function renderResults(query) {
    if (!query.trim()) {
      resultsEl.innerHTML = `
        <p class="empty-state">Typ een zoekterm om Woo-publicaties te doorzoeken, of kies een suggestie hierboven.</p>
      `;
      countEl.textContent = `${documents.length} documenten doorzoekbaar`;
      return;
    }

    const results = miniSearch.search(query, { combineWith: "AND" });
    countEl.textContent = `${results.length} resultaten voor “${query}”`;

    if (!results.length) {
      resultsEl.innerHTML = `<p class="empty-state">Geen resultaten gevonden.</p>`;
      return;
    }

    const terms = query
      .trim()
      .split(/\s+/)
      .filter(Boolean);

    resultsEl.innerHTML = results
      .map((result) => {
        const snippet = snippetAroundMatch(result.text || "", terms);
        return `
          <article class="result-card">
            <h2><a href="${BASE}${result.url}">${highlight(result.publication_title, terms)}</a></h2>
            <div class="result-meta">${formatDate(result.publication_date)} · ${highlight(result.pdf_label, terms)}</div>
            <div class="result-snippet">${highlight(snippet, terms)}</div>
          </article>
        `;
      })
      .join("");
  }

  input.addEventListener("input", () => renderResults(input.value));
  renderResults("");
}

initSearch().catch((error) => {
  console.error(error);
  const resultsEl = document.querySelector("#results");
  if (resultsEl) {
    resultsEl.innerHTML = `<p class="empty-state">Kon de zoekindex niet laden.</p>`;
  }
});
