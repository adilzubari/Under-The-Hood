---
tags:
  - phase-1
  - design-patterns
  - fundamentals
---

# Design Patterns

Reusable solutions to recurring design problems. Most patterns are SOLID applied — they exist because the same constraints crop up over and over.

> **How to study these:** memorize the *intent* and the *forces* (what problem, what trade-off). The exact UML you can re-derive. The Pythonic version often differs from the textbook (Java) version because Python's dynamic features absorb half the boilerplate.

## Patterns covered

### Creational

- [**Singleton**](singleton.md) — exactly one instance, globally accessible.
- [**Factory**](factory.md) — create objects without committing to a concrete class.
- [**Builder**](builder.md) — assemble complex objects step by step.

### Structural

- [**Adapter**](adapter.md) — bridge incompatible interfaces.
- [**Decorator**](decorator.md) — add behavior to objects dynamically.
- [**Proxy**](proxy.md) — stand-in that controls access to a real object.

### Behavioral

- [**Strategy**](strategy.md) — swap algorithms at runtime.
- [**Observer**](observer.md) — broadcast changes to interested parties.
- [**Chain of Responsibility**](chain-of-responsibility.md) — pipeline of handlers.

## Quick decision matrix

| Problem | Pattern |
|---|---|
| "I need to swap *which* algorithm runs" | Strategy |
| "I need to add behavior without touching the class" | Decorator |
| "I need to wrap a 3rd-party class to fit my interface" | Adapter |
| "I need to broadcast events to multiple subscribers" | Observer |
| "I need to control creation logic" | Factory / Builder |
| "I need exactly one instance" | Singleton (or just a module — see the page) |
| "I need to lazy-load or guard access" | Proxy |
| "I need to pass a request through a sequence of handlers" | Chain of Responsibility |

## Anti-pattern alert

If you're reaching for a pattern, ask first: **am I solving a real recurring problem, or am I adding ceremony?** Pythonic code often avoids GoF patterns by leaning on first-class functions, decorators, and modules. Read each pattern's "Pythonic alternative" section.
