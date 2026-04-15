---
tags:
  - phase-18
  - search
  - elasticsearch
---

# Phase 18 — Search & Indexing

> **Phase abstract:** When LIKE '%foo%' isn't enough. Inverted indexes, full-text search engines (Elasticsearch / OpenSearch), and the relevance/aggregation layer.

📝 **Status: stub.**

## Topics

- [ ] **Elasticsearch / OpenSearch basics** — cluster, node, index, shard, document.
- [ ] **Full-text search** — analyzers, tokenizers, n-grams. Stemming and language analysis.
- [ ] **Indexing strategies** — bulk indexing, refresh interval, settings for write-heavy vs read-heavy.
- [ ] **Pagination & relevance scoring** — search_after vs from/size. BM25.
- [ ] **Search query optimization** — filters (cached) vs queries (scored). Composite indexes.
- [ ] **Aggregations & filters** — bucket, metric, pipeline aggregations.

## Suggested learning order

1. Inverted index mental model (vs B-tree)
2. Cluster topology (shards, replicas)
3. Analysis chain (tokenizers, filters)
4. Filter vs query (perf differences)
5. Aggregations (the analytics use case)
