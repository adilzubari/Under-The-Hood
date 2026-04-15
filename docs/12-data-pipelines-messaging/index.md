---
tags:
  - phase-12
  - messaging
  - data-pipelines
  - kafka
---

# Phase 12 — Data Pipelines & Messaging

> **Phase abstract:** The async backbone of modern systems. Brokers (Kafka, RabbitMQ, SQS), the patterns that ride on them (DLQ, idempotency, outbox, event replay), and stream-processing frameworks.

📝 **Status: stub.**

## Topics

- [ ] **Kafka basics (producers, consumers, topics)** — partitions, consumer groups, offsets, retention.
- [ ] **RabbitMQ / Celery patterns** — exchanges, queues, routing, prefetch.
- [ ] **Dead letter queues** — when, why, and what to do with them.
- [ ] **Message ordering & deduplication** — single-partition for order, idempotency keys for dedupe.
- [ ] **Event replay** — rewinding offsets. Building new views from old events.
- [ ] **Idempotent consumers** — same event processed twice = same result.
- [ ] **Stream processing (Flink, Spark Streaming)** — windowing, watermarks, exactly-once semantics.
- [ ] **Outbox pattern** — atomic DB write + event publish via a transactional outbox table.

## Suggested learning order

1. Kafka mental model (partitions = parallelism unit)
2. Idempotency + DLQ (the survival pair)
3. Outbox pattern (the atomicity solution for "DB + publish")
4. Stream processing (advanced — once batch processing isn't enough)
