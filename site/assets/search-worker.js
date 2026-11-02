/* global MiniSearch */
importScripts("https://cdn.jsdelivr.net/npm/minisearch@7.1.0/dist/umd/index.min.js");

const shards = [];
let options = null;
let queue = Promise.resolve();
const DB_NAME = "uwv-woo-search";
const STORE = "shards";

function post(type, payload = {}) {
  self.postMessage({ type, ...payload });
}

function openDb() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, 1);
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains(STORE)) {
        db.createObjectStore(STORE);
      }
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function cacheGet(key) {
  try {
    const db = await openDb();
    return await new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, "readonly");
      const request = tx.objectStore(STORE).get(key);
      request.onsuccess = () => resolve(request.result || null);
      request.onerror = () => reject(request.error);
    });
  } catch {
    return null;
  }
}

async function cacheSet(key, value) {
  try {
    const db = await openDb();
    await new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, "readwrite");
      tx.objectStore(STORE).put(value, key);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
    });
  } catch {
    // Cache is optional; a failed write still leaves the shard in memory.
  }
}

async function cacheKeys() {
  try {
    const db = await openDb();
    return await new Promise((resolve, reject) => {
      const request = db.transaction(STORE, "readonly").objectStore(STORE).getAllKeys();
      request.onsuccess = () => resolve(request.result || []);
      request.onerror = () => reject(request.error);
    });
  } catch {
    return [];
  }
}

async function cacheDelete(key) {
  try {
    const db = await openDb();
    await new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, "readwrite");
      tx.objectStore(STORE).delete(key);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
    });
  } catch {
    // Leaving an old shard behind is harmless; it is no longer addressed.
  }
}

async function pruneCache(shardList) {
  const keep = new Set(shardList.map((shard) => cacheKey(shard)));
  for (const key of await cacheKeys()) {
    if (!keep.has(String(key))) {
      await cacheDelete(key);
    }
  }
}

function cacheKey(shard) {
  return `${shard.year}:${shard.hash || "none"}`;
}

function mountShard(shard, payload) {
  const indexJson =
    typeof payload.index === "string" ? payload.index : JSON.stringify(payload.index);
  const miniSearch = MiniSearch.loadJSON(indexJson, payload.options);
  options = payload.options;
  const existing = shards.findIndex((item) => String(item.year) === String(shard.year));
  const record = { year: String(shard.year), hash: shard.hash || "", miniSearch };
  if (existing === -1) {
    shards.push(record);
  } else {
    shards[existing] = record;
  }
}

function shardUrl(baseUrl, shard) {
  const version = shard.hash ? `?v=${encodeURIComponent(shard.hash)}` : "";
  return `${baseUrl}${shard.path}${version}`;
}

async function fetchShard(baseUrl, shard) {
  const response = await fetch(shardUrl(baseUrl, shard));
  if (!response.ok) {
    throw new Error(`Shard ${shard.year} HTTP ${response.status}`);
  }
  const payload = await response.json();
  if (shard.hash) {
    await cacheSet(cacheKey(shard), payload);
  }
  return payload;
}

async function loadShard(baseUrl, shard) {
  const key = cacheKey(shard);
  const cachedPayload = shard.hash ? await cacheGet(key) : null;
  if (cachedPayload) {
    try {
      mountShard(shard, cachedPayload);
      return { year: String(shard.year), cached: true };
    } catch {
      // Cached JSON can be stale or partial; fall through to the network.
    }
  }

  mountShard(shard, await fetchShard(baseUrl, shard));
  return { year: String(shard.year), cached: false };
}

async function ensureShards(baseUrl, shardList, prune = false) {
  const pending = [];
  for (const shard of shardList) {
    const loaded = shards.find(
      (item) => String(item.year) === String(shard.year) && item.hash === (shard.hash || ""),
    );
    if (!loaded) {
      pending.push(shard);
    }
  }

  for (let index = 0; index < pending.length; index += 1) {
    const result = await loadShard(baseUrl, pending[index]);
    post("shard-loaded", {
      loaded: index + 1,
      total: pending.length,
      year: result.year,
      cached: result.cached,
    });
  }

  if (prune) {
    await pruneCache(shardList);
  }

  post("ready", { shardCount: shards.length, fetched: pending.length });
}

function activeShards(years) {
  if (!years || !years.length) {
    return shards;
  }
  const wanted = new Set(years.map((year) => String(year)));
  return shards.filter((shard) => wanted.has(String(shard.year)));
}

function searchAll(query, years) {
  const merged = new Map();

  for (const { miniSearch } of activeShards(years)) {
    for (const result of miniSearch.search(query, options?.searchOptions || { combineWith: "AND" })) {
      const existing = merged.get(result.id);
      if (!existing || result.score > existing.score) {
        merged.set(result.id, result);
      }
    }
  }

  return [...merged.values()].sort((left, right) => right.score - left.score);
}

function suggestAll(query, years) {
  const merged = new Map();
  const suggestOptions = {
    ...(options?.searchOptions || {}),
    fuzzy: 0.2,
    prefix: true,
  };

  for (const { miniSearch } of activeShards(years)) {
    if (typeof miniSearch.autoSuggest !== "function") {
      continue;
    }
    for (const item of miniSearch.autoSuggest(query, suggestOptions)) {
      const suggestion = (item.suggestion || "").trim();
      if (!suggestion || suggestion.toLowerCase() === query.trim().toLowerCase()) {
        continue;
      }
      const existing = merged.get(suggestion);
      if (!existing || item.score > existing.score) {
        merged.set(suggestion, { suggestion, score: item.score });
      }
    }
  }

  return [...merged.values()]
    .sort((left, right) => right.score - left.score)
    .slice(0, 6)
    .map((item) => item.suggestion);
}

self.onmessage = async (event) => {
  const { type } = event.data;

  try {
    if (type === "load" || type === "ensure") {
      const baseUrl = event.data.baseUrl;
      const shardList = event.data.shards || [];
      queue = queue
        .then(() => ensureShards(baseUrl, shardList, Boolean(event.data.prune)))
        .catch((error) => {
          post("error", { message: error?.message || String(error) });
        });
      return;
    }

    if (type === "search") {
      post("search-results", {
        requestId: event.data.requestId,
        results: searchAll(event.data.query, event.data.years),
      });
      return;
    }

    if (type === "suggest") {
      post("suggest-results", {
        requestId: event.data.requestId,
        suggestions: suggestAll(event.data.query, event.data.years),
      });
    }
  } catch (error) {
    post("error", { message: error?.message || String(error) });
  }
};
