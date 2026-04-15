---
tags:
  - phase-9
  - scalability
  - performance
---

# Phase 9 — Scalability & Performance

> **Phase abstract:** The art of making things faster *and* bigger. Vertical vs horizontal scaling, the toolkit of caches and async, profiling discipline, and the bottleneck-finding mindset.

📝 **Status: stub.**

## Topics

- [ ] **Horizontal vs vertical scaling** — when each is right. The shared-nothing principle.
- [ ] **Load balancing strategies** — round-robin, least-conn, consistent hashing.
- [ ] **CDN & edge caching** — see [Phase 5](../05-networking-communication/index.md) and [Phase 17](../17-caching-optimization/index.md).
- [ ] **Database replication & sharding** — read replicas, primary-replica lag, cross-shard queries.
- [ ] **Async processing & queues** — see [Phase 6](../06-concurrency-async/index.md).
- [ ] **Caching optimization (Redis)** — see [Phase 17](../17-caching-optimization/index.md).
- [ ] **Profiling & performance testing** — `cProfile`, `py-spy`, `pyinstrument`. Flame graphs.
- [ ] **Bottleneck identification** — the bottleneck moves; methodology to find it.
- [ ] **Lazy loading & batching** — paginate, prefetch, DataLoader patterns.
- [ ] **Connection pooling optimization** — size for the bottleneck (DB, not app).
- [ ] **Query optimization & indexing** — see [Phase 3](../03-database-storage/index.md).

## Suggested learning order

1. Profiling discipline (measure before optimize)
2. Bottleneck mental model
3. Caching + indexing (the 80/20 wins)
4. Sharding / replication (the harder wins)
5. CDN + async (architectural wins)
