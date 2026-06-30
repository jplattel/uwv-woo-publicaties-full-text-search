/* global MiniSearch */
importScripts("https://cdn.jsdelivr.net/npm/minisearch@7.1.0/dist/umd/index.min.js");

const shards = [];
let options = null;
let loadGeneration = 0;

function post(type, payload = {}) {
  self.postMessage({ type, ...payload });
}

async function loadShard(baseUrl, shard, generation) {
  const response = await fetch(`${baseUrl}${shard.path}`);
  if (!response.ok) {
    throw new Error(`Shard ${shard.year} HTTP ${response.status}`);
  }
  const payload = await response.json();
  if (generation !== loadGeneration) {
    return null;
  }

  const indexJson =
    typeof payload.index === "string" ? payload.index : JSON.stringify(payload.index);
  const miniSearch = MiniSearch.loadJSON(indexJson, payload.options);
  options = payload.options;
  shards.push({ year: shard.year, miniSearch });
  return shard.year;
}

async function loadShards(baseUrl, shardList, generation) {
  shards.length = 0;
  options = null;

  for (let index = 0; index < shardList.length; index += 1) {
    const shard = shardList[index];
    const year = await loadShard(baseUrl, shard, generation);
    if (year === null) {
      return;
    }
    post("shard-loaded", {
      loaded: index + 1,
      total: shardList.length,
      year,
    });
  }

  if (generation === loadGeneration) {
    post("ready", { shardCount: shards.length });
  }
}

function searchAll(query) {
  const merged = new Map();

  for (const { miniSearch } of shards) {
    for (const result of miniSearch.search(query, options?.searchOptions || { combineWith: "AND" })) {
      const existing = merged.get(result.id);
      if (!existing || result.score > existing.score) {
        merged.set(result.id, result);
      }
    }
  }

  return [...merged.values()].sort((left, right) => right.score - left.score);
}

self.onmessage = async (event) => {
  const { type } = event.data;

  try {
    if (type === "load") {
      loadGeneration += 1;
      const generation = loadGeneration;
      await loadShards(event.data.baseUrl, event.data.shards, generation);
      return;
    }

    if (type === "search") {
      const results = searchAll(event.data.query);
      post("search-results", {
        requestId: event.data.requestId,
        results,
      });
    }
  } catch (error) {
    post("error", { message: error?.message || String(error) });
  }
};
