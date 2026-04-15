---
tags:
  - phase-1
  - fundamentals
---

# Phase 1 — Programming & Language Fundamentals

The base layer. Everything else stacks on these — design patterns inform architecture, async concepts inform distributed systems, testing discipline informs CI/CD. Get this right and the rest is easier.

> **Phase abstract:** Core programming paradigms, the design patterns library, dependency injection, concurrency primitives, memory model, error handling, observability fundamentals, and testing. Python-first examples.

## Topics

- [x] [**OOP & SOLID**](oop-solid.md) — pillars + each SOLID principle with before/after Python.
- [x] [**Functional Programming**](functional-programming.md) — pure functions, immutability, HOFs, `functools`, currying.
- [x] **Design Patterns** — see [folder](design-patterns/index.md). One file per pattern: Singleton, Factory, Strategy, Observer, Decorator, Adapter, Proxy, Builder, Chain of Responsibility.
- [x] [**Dependency Injection**](dependency-injection.md) — manual DI, containers, FastAPI's `Depends`, testability.
- [x] [**Async / Concurrency / Threading**](async-concurrency.md) — `asyncio`, threads, processes, the GIL, when each fits.
- [x] [**Memory Management & GC**](memory-management.md) — refcounting, generational GC, leaks, `__slots__`, `weakref`.
- [x] [**Error Handling**](error-handling.md) — exception hierarchy, EAFP vs LBYL, custom exceptions, retries.
- [x] [**Logging & Observability**](logging-observability.md) — structured logs, correlation IDs, log levels, OpenTelemetry intro.
- [x] [**Testing Frameworks**](testing-frameworks.md) — pytest fixtures, parametrize, mocking, coverage.

## Suggested learning order

1. **OOP & SOLID** → **Design Patterns** (patterns make sense once SOLID clicks)
2. **Functional Programming** (orthogonal to OOP — strengthens both)
3. **Dependency Injection** (where SOLID's "D" lives in practice)
4. **Async / Concurrency** (the model under every web framework)
5. **Memory Management** (debugging-heavy — read after you've felt a leak)
6. **Error Handling**, **Logging**, **Testing** (the operational triad)
