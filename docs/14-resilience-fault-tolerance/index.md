---
tags:
  - phase-14
  - resilience
  - fault-tolerance
---

# Phase 14 — Resilience & Fault Tolerance

> **Phase abstract:** Failure is the default state. These patterns let you fail fast, isolate blast radius, recover gracefully, and keep serving traffic when something downstream is sick.

📝 **Status: stub.**

## Topics

- [ ] **Circuit breaker** — closed → open → half-open. Stop hammering a sick service.
- [ ] **Retry with exponential backoff** — see [Phase 1: Error Handling](../01-programming-fundamentals/error-handling.md). Always with jitter.
- [ ] **Bulkhead isolation** — separate thread pools / connection pools per dependency.
- [ ] **Timeout handling** — every call gets a timeout. Always.
- [ ] **Fallback responses** — degraded but useful. Cached values, defaults, partial results.
- [ ] **Graceful degradation** — drop non-essentials when overloaded.
- [ ] **Rate limiting** — see [Phase 5](../05-networking-communication/index.md). Defensive use to protect *yourself*.
- [ ] **Fail-fast & failover** — quickly detect, switch to standby. Active-passive vs active-active.
- [ ] **Health checks & readiness probes** — liveness vs readiness vs startup. K8s semantics.

## Suggested learning order

1. Timeouts + retries + idempotency (the trio)
2. Circuit breaker (the classic)
3. Bulkhead (the often-missed one)
4. Health checks + readiness (K8s-aware)
5. Failover patterns (DR-level)
