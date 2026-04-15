---
tags:
  - phase-11
  - testing
  - quality
---

# Phase 11 — Testing & Quality

> **Phase abstract:** Beyond unit tests. Builds on [Phase 1: Testing](../01-programming-fundamentals/testing-frameworks.md). Here: integration, contract, load, and the broader quality apparatus.

📝 **Status: stub.**

## Topics

- [ ] **Unit, integration, end-to-end tests** — the pyramid. What goes in each layer.
- [ ] **Test-driven development (TDD)** — red/green/refactor. When TDD pays.
- [ ] **Behavior-driven development (BDD)** — Gherkin, executable specs (`pytest-bdd`).
- [ ] **Mocking external dependencies** — see [Phase 1](../01-programming-fundamentals/testing-frameworks.md). Here: contract testing as the alternative.
- [ ] **Load testing (Locust, k6, JMeter)** — RPS, p95, soak vs spike. Defining SLOs.
- [ ] **Contract testing (Pact)** — consumer-driven contracts. Avoid integration test combinatorial explosion.
- [ ] **Smoke & regression testing** — post-deploy quick checks. Promotion gating.
- [ ] **API schema validation** — runtime contract enforcement. OpenAPI as source of truth.
- [ ] **Code coverage & static analysis** — `coverage`, `mypy`, `ruff`, `bandit`. Pre-commit hooks.

## Suggested learning order

1. Recap [Phase 1 testing](../01-programming-fundamentals/testing-frameworks.md)
2. Integration tests (the layer most teams under-invest in)
3. Contract testing (the microservice-era win)
4. Load testing + SLOs (perf testing as a capability, not a one-off)
