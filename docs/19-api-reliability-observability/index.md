---
tags:
  - phase-19
  - reliability
  - observability
  - slo
---

# Phase 19 — API Reliability & Observability

> **Phase abstract:** Reliability as a measurable property. SLIs, SLOs, SLAs, error budgets — and the observability infrastructure (metrics, traces, dashboards) that makes them real.

📝 **Status: stub.**

## Topics

- [ ] **Metrics: latency, throughput, error rate** — RED method (Rate, Errors, Duration). USE method.
- [ ] **Health checks & probes** — liveness vs readiness vs startup (K8s lens).
- [ ] **Circuit breaker metrics** — see [Phase 14](../14-resilience-fault-tolerance/index.md). State, trips/min.
- [ ] **Request tracing (trace IDs, correlation IDs)** — see [Phase 1: Logging](../01-programming-fundamentals/logging-observability.md).
- [ ] **Logging context propagation** — `contextvars` for async-safe propagation.
- [ ] **Dashboards & SLIs/SLOs/SLAs** — the difference. Error budgets and burn rates.

## Suggested learning order

1. SLI / SLO / SLA definitions (the language of reliability)
2. RED method for service metrics
3. Error budgets (the policy lever)
4. Burn-rate alerting (the modern alert pattern)

## Recommended reading

- *Site Reliability Engineering* — Google SRE book (free online)
- *The Site Reliability Workbook* — practical companion
