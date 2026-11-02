const BASE = document.querySelector('meta[name="base-path"]')?.content || "/";
const SEARCH_DEBOUNCE_MS = 300;
const RESULTS_PER_PAGE = 25;

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function escapeAttr(value) {
  return escapeHtml(value).replaceAll("'", "&#39;");
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

function yearFromDate(value) {
  if (!value) {
    return null;
  }
  const match = String(value).match(/^(\d{4})/);
  return match ? Number(match[1]) : null;
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

function debounce(fn, delayMs) {
  let timerId = null;
  return (...args) => {
    if (timerId !== null) {
      clearTimeout(timerId);
    }
    timerId = setTimeout(() => {
      timerId = null;
      fn(...args);
    }, delayMs);
  };
}

function createSearchWorker() {
  let worker = null;
  let ready = false;
  let loadError = null;
  let nextRequestId = 1;
  const pendingSearches = new Map();

  function ensureWorker() {
    if (!worker) {
      worker = new Worker(`${BASE}assets/search-worker.js`);
      worker.onmessage = (event) => {
        const { type } = event.data;
        if (type === "shard-loaded") {
          onShardLoaded?.(event.data);
          return;
        }
        if (type === "ready") {
          ready = true;
          onReady?.();
          return;
        }
        if (type === "search-results" || type === "suggest-results") {
          const pending = pendingSearches.get(event.data.requestId);
          if (pending) {
            pendingSearches.delete(event.data.requestId);
            pending.resolve(
              type === "search-results" ? event.data.results : event.data.suggestions || [],
            );
          }
          return;
        }
        if (type === "error") {
          loadError = new Error(event.data.message || "Zoekindex fout");
          onError?.(loadError);
        }
      };
      worker.onerror = (event) => {
        loadError = new Error(event.message || "Worker fout");
        onError?.(loadError);
      };
    }
    return worker;
  }

  let onShardLoaded = null;
  let onReady = null;
  let onError = null;

  return {
    ensure(shards, callbacks) {
      onShardLoaded = callbacks.onShardLoaded;
      onReady = callbacks.onReady;
      onError = callbacks.onError;
      loadError = null;
      ready = false;
      ensureWorker().postMessage({
        type: "ensure",
        baseUrl: BASE,
        shards,
      });
    },
    async search(query, years) {
      if (loadError) {
        throw loadError;
      }
      if (!ready) {
        throw new Error("Zoekindex is nog niet klaar");
      }
      const requestId = nextRequestId++;
      return new Promise((resolve, reject) => {
        pendingSearches.set(requestId, { resolve, reject });
        ensureWorker().postMessage({ type: "search", query, years, requestId });
      });
    },
    async suggest(query, years) {
      if (loadError || !ready) {
        return [];
      }
      const requestId = nextRequestId++;
      return new Promise((resolve, reject) => {
        pendingSearches.set(requestId, { resolve, reject });
        ensureWorker().postMessage({ type: "suggest", query, years, requestId });
      });
    },
  };
}

function renderSuggestionChips(suggestionsEl, suggestions, indexReady) {
  if (!suggestionsEl || !suggestions.length) {
    return;
  }

  suggestionsEl.setAttribute("aria-busy", indexReady ? "false" : "true");
  suggestionsEl.innerHTML = `
    <span class="search-suggestions-label">Voorbeeldzoekopdrachten:</span>
    ${suggestions
      .map(({ term, count }) => {
        const countLabel =
          typeof count === "number" ? `<span class="suggestion-count">${count}</span>` : "";
        const disabled = indexReady ? "" : " disabled";
        return `<button type="button" class="suggestion-chip"${disabled} data-term="${escapeAttr(term)}">${escapeHtml(term)}${countLabel}</button>`;
      })
      .join("")}
  `;
}

function wireSuggestionClicks(input, suggestionsEl, onSelect) {
  if (!suggestionsEl) {
    return;
  }
  suggestionsEl.addEventListener("click", (event) => {
    const button = event.target.closest(".suggestion-chip");
    if (!button || button.disabled) {
      return;
    }
    input.value = button.dataset.term || button.textContent.trim();
    input.focus();
    onSelect(input.value);
  });
}

function readInitialState() {
  const params = new URLSearchParams(window.location.search);
  return {
    query: (params.get("q") || "").trim(),
    page: Math.max(1, Number.parseInt(params.get("page") || "1", 10) || 1),
    yearFrom: params.get("from") || "",
    yearTo: params.get("to") || "",
    type: params.get("type") || "",
    ocrOnly: params.get("ocr") === "1",
    sort: params.get("sort") || "relevance",
  };
}

function updateUrl(state) {
  const params = new URLSearchParams();
  if (state.query) {
    params.set("q", state.query);
  }
  if (state.page > 1) {
    params.set("page", String(state.page));
  }
  if (state.yearFrom) {
    params.set("from", state.yearFrom);
  }
  if (state.yearTo) {
    params.set("to", state.yearTo);
  }
  if (state.type) {
    params.set("type", state.type);
  }
  if (state.ocrOnly) {
    params.set("ocr", "1");
  }
  if (state.sort && state.sort !== "relevance") {
    params.set("sort", state.sort);
  }
  const next = `${window.location.pathname}${params.toString() ? `?${params}` : ""}`;
  window.history.replaceState(null, "", next);
}

async function initSearch() {
  const input = document.querySelector("#search-input");
  const resultsEl = document.querySelector("#results");
  const countEl = document.querySelector("#result-count");
  const suggestionsEl = document.querySelector("#search-suggestions");
  const filtersEl = document.querySelector("#search-filters");
  const yearFromEl = document.querySelector("#filter-year-from");
  const yearToEl = document.querySelector("#filter-year-to");
  const typeEl = document.querySelector("#filter-type");
  const ocrEl = document.querySelector("#filter-ocr");
  const sortEl = document.querySelector("#sort-by");
  const clearFiltersEl = document.querySelector("#clear-filters");
  const paginationEl = document.querySelector("#pagination");
  const statusEl = document.querySelector("#search-status");
  const statusTextEl = document.querySelector("#search-status-text");
  const spinnerEl = document.querySelector(".search-spinner");
  const pageLoaderEl = document.querySelector("#page-loader");
  const pageLoaderDetailEl = document.querySelector("#page-loader-detail");

  if (!input || !resultsEl || !countEl) {
    return;
  }

  const initialState = readInitialState();
  const searchWorker = createSearchWorker();
  let indexReady = false;
  let documentCount = 0;
  let suggestions = [];
  let shardCatalog = [];
  let loadedShardKeys = new Set();
  let ensurePromise = null;
  let currentPage = initialState.page;
  let lastQuery = "";

  function getFilterState() {
    return {
      query: input.value.trim(),
      page: currentPage,
      yearFrom: yearFromEl?.value || "",
      yearTo: yearToEl?.value || "",
      type: typeEl?.value || "",
      ocrOnly: Boolean(ocrEl?.checked),
      sort: sortEl?.value || "relevance",
    };
  }

  function populateFilters(meta) {
    const filters = meta.filters || {};
    const yearRange = filters.yearRange;
    const types = filters.publicationTypes || [];

    if (yearRange && yearFromEl && yearToEl) {
      const minYear = Number(yearRange.min);
      const maxYear = Number(yearRange.max);
      const years = [];
      for (let year = minYear; year <= maxYear; year += 1) {
        years.push(year);
      }
      const yearOptions = (selected, includeAll) => {
        const allOption = includeAll ? '<option value="">Alle jaren</option>' : "";
        return (
          allOption +
          years
            .map(
              (year) =>
                `<option value="${year}"${String(year) === selected ? " selected" : ""}>${year}</option>`,
            )
            .join("")
        );
      };
      yearFromEl.innerHTML = yearOptions(initialState.yearFrom, true);
      yearToEl.innerHTML = yearOptions(initialState.yearTo, true);
    }

    if (typeEl) {
      typeEl.innerHTML =
        '<option value="">Alle types</option>' +
        types
          .map(
            (type) =>
              `<option value="${escapeAttr(type)}"${type === initialState.type ? " selected" : ""}>${escapeHtml(type)}</option>`,
          )
          .join("");
    }

    if (ocrEl) {
      ocrEl.checked = initialState.ocrOnly;
    }
    if (sortEl) {
      sortEl.value = initialState.sort;
    }
    if (filtersEl) {
      filtersEl.hidden = false;
    }
  }

  function selectedShardYears() {
    const yearFrom = yearFromEl?.value ? Number(yearFromEl.value) : null;
    const yearTo = yearToEl?.value ? Number(yearToEl.value) : null;
    if (yearFrom === null && yearTo === null) {
      return null;
    }
    return shardCatalog
      .filter((shard) => {
        const year = Number(shard.year);
        if (!Number.isFinite(year)) {
          return false;
        }
        if (yearFrom !== null && year < yearFrom) {
          return false;
        }
        if (yearTo !== null && year > yearTo) {
          return false;
        }
        return true;
      })
      .map((shard) => String(shard.year));
  }

  function shardsForSearch() {
    const years = selectedShardYears();
    if (!years) {
      return shardCatalog;
    }
    const wanted = new Set(years);
    return shardCatalog.filter((shard) => wanted.has(String(shard.year)));
  }

  function ensureIndex(shards) {
    const missing = shards.filter((shard) => !loadedShardKeys.has(`${shard.year}:${shard.hash || ""}`));
    if (!missing.length) {
      indexReady = true;
      return Promise.resolve();
    }
    if (ensurePromise) {
      return ensurePromise.then(() => ensureIndex(shards));
    }

    setLoading(true, "Zoekindex laden…");
    setPageLoader(false);

    ensurePromise = new Promise((resolve, reject) => {
      let networkLoads = 0;
      searchWorker.ensure(missing, {
        onShardLoaded({ loaded, total, year, cached }) {
          if (!cached) {
            networkLoads += 1;
          }
          const message = networkLoads
            ? `Index laden (${loaded}/${total}) — ${year}…`
            : `Index uit cache (${loaded}/${total})…`;
          setLoading(true, message);
          setPageLoader(networkLoads > 0, message);
        },
        onReady() {
          for (const shard of missing) {
            loadedShardKeys.add(`${shard.year}:${shard.hash || ""}`);
          }
          indexReady = true;
          input.disabled = false;
          setPageLoader(false);
          resolve();
        },
        onError(error) {
          reject(error);
        },
      });
    }).finally(() => {
      ensurePromise = null;
    });
    return ensurePromise;
  }

  function setPageLoader(isLoading, detail) {
    if (!pageLoaderEl) {
      return;
    }
    pageLoaderEl.classList.toggle("is-visible", isLoading);
    pageLoaderEl.setAttribute("aria-busy", isLoading ? "true" : "false");
    if (pageLoaderDetailEl && detail) {
      pageLoaderDetailEl.textContent = detail;
    }
  }

  function setLoading(isLoading, message) {
    if (statusEl) {
      statusEl.classList.toggle("is-loading", isLoading);
      statusEl.hidden = !isLoading && indexReady;
    }
    if (spinnerEl) {
      spinnerEl.hidden = !isLoading;
    }
    if (statusTextEl) {
      statusTextEl.textContent = isLoading ? message || "Laden…" : "";
    }
  }

  function renderEmptyState() {
    resultsEl.innerHTML = `
      <p class="empty-state">Typ een zoekterm om Woo-publicaties te doorzoeken, of kies een voorbeeld hierboven.</p>
    `;
    if (paginationEl) {
      paginationEl.hidden = true;
      paginationEl.innerHTML = "";
    }
    countEl.textContent = indexReady
      ? `${documentCount.toLocaleString("nl-NL")} documenten doorzoekbaar`
      : "Zoekindex laden…";
  }

  function applyFilters(results) {
    const yearFrom = yearFromEl?.value ? Number(yearFromEl.value) : null;
    const yearTo = yearToEl?.value ? Number(yearToEl.value) : null;
    const type = typeEl?.value || "";
    const ocrOnly = Boolean(ocrEl?.checked);

    return results.filter((result) => {
      const year = yearFromDate(result.publication_date);
      if (yearFrom !== null && (year === null || year < yearFrom)) {
        return false;
      }
      if (yearTo !== null && (year === null || year > yearTo)) {
        return false;
      }
      if (type && result.publication_type !== type) {
        return false;
      }
      if (ocrOnly && !result.ocr_used) {
        return false;
      }
      return true;
    });
  }

  function sortResults(results, sortBy) {
    if (sortBy === "relevance") {
      return results;
    }
    const sorted = [...results];
    sorted.sort((left, right) => {
      const leftDate = Date.parse(left.publication_date || "") || 0;
      const rightDate = Date.parse(right.publication_date || "") || 0;
      return sortBy === "date-asc" ? leftDate - rightDate : rightDate - leftDate;
    });
    return sorted;
  }

  function renderPagination(totalResults, page) {
    if (!paginationEl) {
      return;
    }
    const totalPages = Math.max(1, Math.ceil(totalResults / RESULTS_PER_PAGE));
    currentPage = Math.min(Math.max(1, page), totalPages);

    if (totalPages <= 1) {
      paginationEl.hidden = true;
      paginationEl.innerHTML = "";
      return;
    }

    paginationEl.hidden = false;
    const start = (currentPage - 1) * RESULTS_PER_PAGE + 1;
    const end = Math.min(totalResults, currentPage * RESULTS_PER_PAGE);

    let pagesHtml = "";
    const windowSize = 5;
    let startPage = Math.max(1, currentPage - Math.floor(windowSize / 2));
    let endPage = Math.min(totalPages, startPage + windowSize - 1);
    startPage = Math.max(1, endPage - windowSize + 1);

    for (let pageNumber = startPage; pageNumber <= endPage; pageNumber += 1) {
      const active = pageNumber === currentPage ? " is-active" : "";
      pagesHtml += `<button type="button" class="page-button${active}" data-page="${pageNumber}">${pageNumber}</button>`;
    }

    paginationEl.innerHTML = `
      <button type="button" class="page-button" data-page="${currentPage - 1}"${currentPage <= 1 ? " disabled" : ""}>Vorige</button>
      ${pagesHtml}
      <button type="button" class="page-button" data-page="${currentPage + 1}"${currentPage >= totalPages ? " disabled" : ""}>Volgende</button>
      <span class="pagination-meta">${start.toLocaleString("nl-NL")}–${end.toLocaleString("nl-NL")} van ${totalResults.toLocaleString("nl-NL")}</span>
    `;
  }

  function renderNoResults(query, rawCount) {
    const exampleButtons = suggestions
      .filter((item) => item.term && item.term.toLowerCase() !== query.toLowerCase())
      .slice(0, 6)
      .map(
        ({ term, count }) =>
          `<button type="button" class="suggestion-chip" data-term="${escapeAttr(term)}">${escapeHtml(term)}${
            typeof count === "number" ? `<span class="suggestion-count">${count}</span>` : ""
          }</button>`,
      )
      .join("");
    const filterHint =
      rawCount > 0
        ? `<p>Er zijn ${rawCount.toLocaleString("nl-NL")} treffers, maar de filters verbergen ze.</p>`
        : `<p>Geen resultaten voor “${escapeHtml(query)}”.</p>`;
    resultsEl.innerHTML = `
      <div class="empty-state">
        ${filterHint}
        <p>Probeer een andere term, wis de filters, of blader <a href="${BASE}publications.html">op jaartal</a>.</p>
        <div class="search-suggestions no-result-suggestions">
          <span class="search-suggestions-label">Suggesties:</span>
          <span id="dynamic-suggestions"></span>
          ${exampleButtons}
        </div>
      </div>
    `;
    renderPagination(0, 1);
  }

  async function renderResults(query) {
    lastQuery = query;

    if (!query.trim()) {
      currentPage = 1;
      updateUrl(getFilterState());
      renderEmptyState();
      return;
    }

    const shards = shardsForSearch();
    const years = selectedShardYears();
    try {
      await ensureIndex(shards);
    } catch (error) {
      console.error(error);
      resultsEl.innerHTML = `<p class="empty-state">Kon de zoekindex niet laden.</p>`;
      setLoading(false);
      setPageLoader(false);
      return;
    }

    setLoading(true, "Zoeken…");
    let rawResults;
    try {
      rawResults = await searchWorker.search(query, years);
    } catch (error) {
      console.error(error);
      resultsEl.innerHTML = `<p class="empty-state">Zoeken mislukt.</p>`;
      setLoading(false);
      return;
    }
    setLoading(false);

    const filtered = applyFilters(rawResults);
    const sorted = sortResults(filtered, sortEl?.value || "relevance");
    const totalResults = sorted.length;
    const totalPages = Math.max(1, Math.ceil(totalResults / RESULTS_PER_PAGE));

    if (currentPage > totalPages) {
      currentPage = totalPages;
    }

    updateUrl({ ...getFilterState(), query, page: currentPage });

    const start = (currentPage - 1) * RESULTS_PER_PAGE;
    const pageResults = sorted.slice(start, start + RESULTS_PER_PAGE);
    const filterNote =
      filtered.length !== rawResults.length
        ? ` (${filtered.length.toLocaleString("nl-NL")} na filters)`
        : "";

    countEl.textContent = `${totalResults.toLocaleString("nl-NL")} resultaten voor “${query}”${filterNote}`;

    if (!totalResults) {
      renderNoResults(query, rawResults.length);
      try {
        const dynamic = await searchWorker.suggest(query, years);
        const slot = document.querySelector("#dynamic-suggestions");
        if (slot && dynamic.length) {
          slot.innerHTML = dynamic
            .map(
              (term) =>
                `<button type="button" class="suggestion-chip" data-term="${escapeAttr(term)}">${escapeHtml(term)}</button>`,
            )
            .join("");
        }
      } catch (error) {
        console.error(error);
      }
      return;
    }

    const terms = query
      .trim()
      .split(/\s+/)
      .filter(Boolean);

    resultsEl.innerHTML = pageResults
      .map((result) => {
        const snippet = snippetAroundMatch(result.text_preview || result.text || "", terms);
        const ocrBadge = result.ocr_used ? '<span class="ocr-badge">OCR</span>' : "";
        const href = `${BASE}${result.url}?q=${encodeURIComponent(query)}`;
        return `
          <article class="result-card">
            <h2><a href="${href}">${highlight(result.publication_title, terms)}</a> ${ocrBadge}</h2>
            <div class="result-meta">${formatDate(result.publication_date)} · ${highlight(result.pdf_label, terms)}</div>
            <div class="result-snippet">${highlight(snippet, terms)}</div>
          </article>
        `;
      })
      .join("");

    renderPagination(totalResults, currentPage);
  }

  function filtersAreActive() {
    return Boolean(
      yearFromEl?.value || yearToEl?.value || typeEl?.value || ocrEl?.checked || (sortEl && sortEl.value !== "relevance"),
    );
  }

  function clearFilters() {
    if (yearFromEl) {
      yearFromEl.value = "";
    }
    if (yearToEl) {
      yearToEl.value = "";
    }
    if (typeEl) {
      typeEl.value = "";
    }
    if (ocrEl) {
      ocrEl.checked = false;
    }
    if (sortEl) {
      sortEl.value = "relevance";
    }
    if (clearFiltersEl) {
      clearFiltersEl.hidden = true;
    }
    runSearch(input.value.trim(), 1);
  }

  function runSearch(query, page = 1) {
    currentPage = page;
    if (clearFiltersEl) {
      clearFiltersEl.hidden = !filtersAreActive();
    }
    renderResults(query);
  }

  const debouncedSearch = debounce((query) => runSearch(query, 1), SEARCH_DEBOUNCE_MS);

  wireSuggestionClicks(input, suggestionsEl, (term) => {
    runSearch(term, 1);
  });
  wireSuggestionClicks(input, resultsEl, (term) => {
    runSearch(term, 1);
  });

  input.addEventListener("input", () => {
    const query = input.value;
    if (!query.trim()) {
      debouncedSearch(query);
      return;
    }
    setLoading(true, "Zoeken…");
    debouncedSearch(query);
  });

  for (const control of [yearFromEl, yearToEl, typeEl, ocrEl, sortEl]) {
    control?.addEventListener("change", () => {
      if (clearFiltersEl) {
        clearFiltersEl.hidden = !filtersAreActive();
      }
      if (lastQuery.trim()) {
        runSearch(lastQuery, 1);
      } else {
        updateUrl(getFilterState());
      }
    });
  }

  clearFiltersEl?.addEventListener("click", () => {
    clearFilters();
  });

  paginationEl?.addEventListener("click", (event) => {
    const button = event.target.closest(".page-button");
    if (!button || button.disabled || !lastQuery.trim()) {
      return;
    }
    const page = Number.parseInt(button.dataset.page || "1", 10);
    if (!Number.isFinite(page)) {
      return;
    }
    runSearch(lastQuery, page);
    resultsEl.scrollIntoView({ behavior: "smooth", block: "start" });
  });

  renderEmptyState();
  setLoading(true, "Metadata laden…");
  setPageLoader(false);

  try {
    const metaResponse = await fetch(`${BASE}search-meta.json`);
    if (!metaResponse.ok) {
      throw new Error(`search-meta.json HTTP ${metaResponse.status}`);
    }
    const meta = await metaResponse.json();
    suggestions = meta.exampleSearches || meta.suggestions || [];
    documentCount = Number(meta.documentCount || 0);

    populateFilters(meta);
    shardCatalog = meta.indexShards || [];
    if (!shardCatalog.length) {
      throw new Error("Geen zoekindex shards gevonden — herbouw de site.");
    }

    if (suggestions.length) {
      renderSuggestionChips(suggestionsEl, suggestions, true);
    }
    if (clearFiltersEl) {
      clearFiltersEl.hidden = !filtersAreActive();
    }

    input.disabled = false;
    setLoading(false);
    setPageLoader(false);
    countEl.textContent = `${documentCount.toLocaleString("nl-NL")} documenten doorzoekbaar`;

    if (initialState.query) {
      input.value = initialState.query;
      runSearch(initialState.query, initialState.page);
      return;
    }

    input.focus();
    renderEmptyState();
  } catch (error) {
    console.error(error);
    setLoading(false);
    setPageLoader(false);
    if (suggestionsEl) {
      suggestionsEl.setAttribute("aria-busy", "false");
    }
    resultsEl.innerHTML = `<p class="empty-state">Kon de zoekindex niet laden.</p>`;
    countEl.textContent = "";
  }
}

initSearch();
