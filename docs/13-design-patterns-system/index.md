---
tags:
  - phase-13
  - design-patterns
  - architecture
---

# Phase 13 — System-Level Design Patterns

> **Phase abstract:** The patterns that organize *applications*, not *objects*. Where [Phase 1's GoF patterns](../01-programming-fundamentals/design-patterns/index.md) cover object-level reuse, these cover service/layer boundaries within a codebase: Repository, Unit of Work, Service Layer, Mediator, etc.

📝 **Status: stub.**

## Topics

- [ ] **Repository pattern** — abstracts data access. Interface in domain, implementation in infra.
- [ ] **Unit of Work pattern** — atomic transaction boundary. Pairs with Repository.
- [ ] **Service layer pattern** — orchestrates use cases. Domain ↔ infra ↔ presentation seam.
- [ ] **Factory pattern** — see [Phase 1: Factory](../01-programming-fundamentals/design-patterns/factory.md).
- [ ] **Strategy pattern** — see [Phase 1: Strategy](../01-programming-fundamentals/design-patterns/strategy.md).
- [ ] **Observer pattern** — see [Phase 1: Observer](../01-programming-fundamentals/design-patterns/observer.md).
- [ ] **Decorator pattern** — see [Phase 1: Decorator](../01-programming-fundamentals/design-patterns/decorator.md).
- [ ] **Proxy pattern** — see [Phase 1: Proxy](../01-programming-fundamentals/design-patterns/proxy.md).
- [ ] **Adapter pattern** — see [Phase 1: Adapter](../01-programming-fundamentals/design-patterns/adapter.md).
- [ ] **Builder pattern** — see [Phase 1: Builder](../01-programming-fundamentals/design-patterns/builder.md).
- [ ] **Singleton pattern** — see [Phase 1: Singleton](../01-programming-fundamentals/design-patterns/singleton.md).
- [ ] **Chain of Responsibility** — see [Phase 1: CoR](../01-programming-fundamentals/design-patterns/chain-of-responsibility.md).
- [ ] **Mediator pattern** — central hub for N-to-N communication. Reduces coupling between peers.

## Suggested learning order

1. Repository + Unit of Work + Service Layer (the domain-model trio)
2. Cross-reference object patterns from Phase 1
3. Mediator (when the N-to-N problem appears)
