---
tags:
  - phase-17
  - caching
  - performance
---

# Phase 17 — Caching & Optimization

> **Phase abstract:** Caches at every layer (application, distributed, CDN), the strategies that govern them, and the hardest problem in CS: invalidation.

📝 **Status: stub.**

## Topics

- [ ] **Caching strategies** — write-through, write-around, write-back, cache-aside (lazy load).
- [ ] **Cache invalidation** — TTL, event-driven, write-through. The "two hard things" half.
- [ ] **Redis data structures** — strings, hashes, sorted sets, streams. Use cases per type.
- [ ] **Distributed cache** — sharding, replication, consistent hashing. Avoiding hot keys.
- [ ] **CDN caching** — see [Phase 5](../05-networking-communication/index.md). Edge vs origin. Cache keys.
- [ ] **Application-level caching (in-memory, decorator-based)** — `functools.lru_cache`, per-process limits.
- [ ] **ETag & HTTP cache headers** — Cache-Control, Vary, conditional requests.

## Suggested learning order

1. Cache-aside (the default for app-DB caching)
2. Invalidation strategies (TTL → event-based → mixed)
3. Redis primitives (sorted sets are interview gold)
4. CDN + ETag (the HTTP layer)
