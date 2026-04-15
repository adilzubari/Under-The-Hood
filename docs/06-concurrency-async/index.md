---
tags:
  - phase-6
  - concurrency
  - async
---

# Phase 6 — Concurrency & Asynchronous Systems

> **Phase abstract:** How to do more than one thing at a time at the application/system level. Builds on [Phase 1: Async & Concurrency](../01-programming-fundamentals/async-concurrency.md) but extends to job queues, schedulers, distributed locking, and worker patterns.

📝 **Status: stub.**

## Topics

- [ ] **Async I/O (asyncio, event loops)** — see [Phase 1](../01-programming-fundamentals/async-concurrency.md). Here: at-scale patterns.
- [ ] **Multi-threading & multi-processing** — when each fits. The GIL story (and PEP 703).
- [ ] **Task queues (Celery, RQ, Dramatiq)** — broker (Redis, RabbitMQ), worker, result backend.
- [ ] **Job scheduling (APScheduler, cron jobs)** — distributed cron, leader election for single-runner jobs.
- [ ] **Locks, semaphores, race conditions** — primitives. Distributed locks (Redis, Zookeeper).
- [ ] **Thread safety & atomic operations** — what's atomic in Python (GIL helps), what isn't.
- [ ] **Background jobs & worker patterns** — fan-out, work-stealing, priority queues, graceful shutdown.

## Suggested learning order

1. Recap [Phase 1 async](../01-programming-fundamentals/async-concurrency.md)
2. Task queues (Celery is the Python default)
3. Distributed locks + leader election (the hard concurrency problems)
4. Worker patterns (graceful shutdown, retry, DLQ)
