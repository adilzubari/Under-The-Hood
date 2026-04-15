---
tags:
  - phase-10
  - devops
  - observability
---

# Phase 10 — DevOps & Observability

> **Phase abstract:** How code reliably gets to production and stays observable there. Builds on [Phase 7: Cloud](../07-cloud-infrastructure/index.md) and [Phase 1: Logging](../01-programming-fundamentals/logging-observability.md).

📝 **Status: stub.**

## Topics

- [ ] **CI/CD pipelines & automated testing** — see [Phase 7](../07-cloud-infrastructure/index.md). Here: testing strategy in CI.
- [ ] **Git workflows (GitFlow, trunk-based)** — when each fits. Code review patterns.
- [ ] **Dockerfiles & container optimization** — layer caching, minimal images, security scanning.
- [ ] **Kubernetes manifests & Helm charts** — chart structure, values templating.
- [ ] **Infrastructure as Code** — Terraform best practices, state management.
- [ ] **Monitoring metrics (CPU, memory, latency, throughput)** — RED method, USE method.
- [ ] **Logging (structured logs, correlation IDs)** — see [Phase 1](../01-programming-fundamentals/logging-observability.md).
- [ ] **Tracing (OpenTelemetry, Jaeger)** — see [Phase 1](../01-programming-fundamentals/logging-observability.md). Here: instrumentation patterns.
- [ ] **Alerts & incident management** — alerting on symptoms not causes. Runbooks.
- [ ] **Blue-green / canary deployments** — risk reduction patterns.
- [ ] **Rollbacks & feature flags** — decoupling deploy from release.

## Suggested learning order

1. Git workflow + CI basics (the daily-flow foundation)
2. Dockerfile patterns (layer cache, minimal images)
3. Helm + IaC (declarative deploy)
4. RED method for metrics + good alerts (avoid alert fatigue)
5. Feature flags + canary (advanced delivery)
