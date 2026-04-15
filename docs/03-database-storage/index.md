---
tags:
  - phase-3
  - database
  - storage
---

# Phase 3 — Database & Storage

> **Phase abstract:** Where data lives and how to query it well. SQL fundamentals through to distributed-DB trade-offs (CAP, ACID vs BASE, sharding). The ORM layer that bridges code and SQL. Caching as a first-class storage tier.

📝 **Status: stub.** Topic checklist below.

## Topics

- [ ] **SQL fundamentals** — SELECT/JOIN/GROUP BY, indexes, transactions, isolation levels.
- [ ] **Relational databases (PostgreSQL, MySQL)** — when to pick which. PG-specific (JSONB, partial indexes, CTEs).
- [ ] **NoSQL databases (MongoDB, DynamoDB, Cassandra)** — document, key-value, wide-column. Modeling for access patterns.
- [ ] **ORMs (SQLAlchemy, Django ORM)** — pros/cons. The N+1 problem. When to drop to raw SQL.
- [ ] **Connection pooling** — PgBouncer, sqlalchemy pool, sizing.
- [ ] **Database migrations (Alembic, Liquibase)** — forward-only, zero-downtime, online schema change patterns.
- [ ] **Query optimization & indexing strategies** — EXPLAIN ANALYZE, covering indexes, partial indexes, when an index hurts.
- [ ] **Caching layers (Redis, Memcached)** — see [Phase 17: Caching](../17-caching-optimization/index.md).
- [ ] **Data modeling & normalization** — 1NF/2NF/3NF, when to denormalize.
- [ ] **CAP theorem** — pick 2 of 3 (during a partition). Real-world C/A/P preferences.
- [ ] **ACID vs BASE** — transactional consistency vs eventual.
- [ ] **Sharding, replication, partitioning** — horizontal scale strategies. Hot keys.
- [ ] **Distributed transactions** — 2PC, sagas, outbox pattern.

## Suggested learning order

1. SQL fundamentals → Indexing (the 80/20 of DB perf)
2. ORMs + N+1 (every Python web dev hits this)
3. Migrations (zero-downtime patterns are interview gold)
4. CAP / ACID / replication (distributed-systems territory)
