---
tags:
  - phase-4
  - system-design
  - architecture
---

# Phase 4 — System Design & Architecture

> **Phase abstract:** The shapes of systems above the single-process level. Architectural styles (monolith, microservices, hexagonal, event-driven), patterns that recur (CQRS, event sourcing, sagas, circuit breakers), and the cross-cutting concerns of any distributed setup.

📝 **Status: stub.** This is the densest phase — most senior interview prep happens here.

## Topics

### Architectural styles
- [ ] **Monolith vs Microservices** — when each wins. The "distributed monolith" anti-pattern.
- [ ] **Domain-Driven Design (DDD)** — bounded contexts, aggregates, ubiquitous language.
- [ ] **Hexagonal / Clean Architecture** — ports & adapters. Domain at the center.
- [ ] **Event-driven architecture** — async by default. Choreography vs orchestration.

### Patterns
- [ ] **CQRS** — separate read and write models. When the complexity pays off.
- [ ] **Event Sourcing** — store events, derive state. Rebuild any view by replay.
- [ ] **API Gateway pattern** — single entry point, auth, rate limiting, fan-out.
- [ ] **Saga pattern** — long-lived workflows across services. Choreography vs orchestration.
- [ ] **Circuit Breaker** — fail fast when dependency is sick. See [Phase 14](../14-resilience-fault-tolerance/index.md).
- [ ] **Bulkhead** — isolate failure domains.
- [ ] **Retry pattern** — exponential backoff, jitter, idempotency.
- [ ] **Idempotency** — safe to repeat. Idempotency keys, dedupe.

### Cross-cutting
- [ ] **Distributed tracing** — see [Phase 1: Logging & Observability](../01-programming-fundamentals/logging-observability.md) and [Phase 19](../19-api-reliability-observability/index.md).
- [ ] **Load balancing** — L4 vs L7, sticky sessions, health checks.
- [ ] **Rate limiting** — token bucket, leaky bucket, fixed/sliding window.
- [ ] **Message queues (RabbitMQ, Kafka, SQS)** — see [Phase 12](../12-data-pipelines-messaging/index.md).
- [ ] **Pub/Sub model** — topic-based fan-out. At-least-once vs at-most-once.
- [ ] **Caching strategies** — write-through, write-back, write-around, invalidation. See [Phase 17](../17-caching-optimization/index.md).
- [ ] **Service discovery** — DNS-based, registry-based (Consul, etcd, k8s services).
- [ ] **Configuration management** — env vars, config services, secrets.
- [ ] **Scalability (vertical vs horizontal)** — see [Phase 9](../09-scalability-performance/index.md).
- [ ] **High availability & fault tolerance** — see [Phase 14](../14-resilience-fault-tolerance/index.md).
- [ ] **Design for resiliency** — graceful degradation. Failure as a first-class concern.
- [ ] **Backpressure & throttling** — protect downstream systems.

## Suggested learning order

1. Monolith vs Microservices (the framing question)
2. Hexagonal Architecture + DDD (the inner-loop discipline)
3. Event-driven + Sagas (the inter-service backbone)
4. Resilience patterns (circuit breaker, retry, bulkhead — interview staples)
5. CQRS + Event Sourcing (advanced — only when complexity demands)
