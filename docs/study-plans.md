---
tags:
  - study-plans
  - index
---

# 🗺️ Study Plans

> Pick a plan based on where you're headed. Each plan is a sequenced path through existing topics + scenarios. Don't stress timelines — they're rough guides; some topics will click in a day, others need a week.

## 🎯 Plan A — Mid-level Backend Interview Sprint (4 weeks)

**Goal:** Walk into interviews for senior/mid backend roles confident on fundamentals, design patterns, APIs, and one or two classic system-design scenarios.

**Assumes:** You've shipped production code. You know your language. You want a refresh, not a from-scratch teach.

### Week 1 — Fundamentals refresh
- [OOP & SOLID](01-programming-fundamentals/oop-solid.md) — all 5 principles with a real violation for each
- [Functional Programming](01-programming-fundamentals/functional-programming.md) — pure functions, HOFs, composition
- [Dependency Injection](01-programming-fundamentals/dependency-injection.md) — DI is SOLID's "D" in practice
- [Error Handling](01-programming-fundamentals/error-handling.md) — exception discipline, retries, idempotency

**Daily drill:** 5 questions from the [Interview Bank](interview-bank/by-difficulty.md) — start with 🟢 Easy, move to 🟡 Medium.

### Week 2 — Design patterns
- [All 9 GoF patterns](01-programming-fundamentals/design-patterns/index.md) — one per day is plenty
- Focus on **when to use / when NOT to use**. Interviewers care more about judgment than reciting UML.
- Cross-reference: Strategy ↔ OCP; DI ↔ Singleton alternative; Adapter/Decorator/Proxy intent differences.

### Week 3 — Concurrency + observability
- [Async, Concurrency & Threading](01-programming-fundamentals/async-concurrency.md) — async vs threads vs processes
- [Memory Management & GC](01-programming-fundamentals/memory-management.md) — leak-hunting discipline
- [Logging & Observability](01-programming-fundamentals/logging-observability.md) — structured logs + correlation IDs
- [Testing Frameworks](01-programming-fundamentals/testing-frameworks.md) — pytest, fakes vs mocks

### Week 4 — System design practice
- Read [Design a URL Shortener](scenarios-bank/design-url-shortener.md) once, then re-do from scratch on paper.
- Same for [Design a Rate Limiter](scenarios-bank/design-rate-limiter.md).
- Skim [Design a Notifications Service](scenarios-bank/design-notifications-service.md) — note the 3-stage decomposition pattern.
- Practice: given 30 mins, design 1 system a day. Any prompt. Write it out.

**Final check:** Can you explain SOLID in 60 seconds? Can you explain async vs threads to a junior? Can you design a URL shortener with sharding and caching in 45 minutes?

---

## 🏛️ Plan B — Senior / Staff System-Design Prep (6 weeks)

**Goal:** Staff-level system-design rounds. Trade-off fluency, distributed-systems depth, real-world scale intuition.

**Assumes:** Fundamentals are second nature. You're now optimizing for depth.

### Weeks 1-2 — Architectural literacy
- [Phase 4 — System Design & Architecture](04-system-design-architecture/index.md) — monolith vs microservices, DDD, CQRS, event sourcing, sagas
- [Phase 13 — System-Level Design Patterns](13-design-patterns-system/index.md) — Repository, UoW, Mediator
- [Phase 14 — Resilience & Fault Tolerance](14-resilience-fault-tolerance/index.md) — circuit breaker, bulkhead, retry with backoff
- [Phase 16 — API Lifecycle Management](16-api-lifecycle/index.md) — versioning, deprecation, gateway patterns

### Weeks 3-4 — Distributed systems & data
- [Phase 15 — Distributed Systems](15-distributed-systems/index.md) — CAP, consensus, vector clocks, at-least-once semantics
- [Phase 3 — Database & Storage](03-database-storage/index.md) — sharding, replication, ACID vs BASE, tuning
- [Phase 12 — Data Pipelines & Messaging](12-data-pipelines-messaging/index.md) — Kafka, DLQ, outbox pattern, exactly-once
- [Phase 17 — Caching & Optimization](17-caching-optimization/index.md) — strategies, invalidation, Redis primitives

**Read alongside:** *Designing Data-Intensive Applications* (Kleppmann). Essential for staff rounds.

### Week 5 — Operational depth
- [Phase 10 — DevOps & Observability](10-devops-observability/index.md) — RED method, SLIs/SLOs, blue-green/canary
- [Phase 19 — API Reliability & Observability](19-api-reliability-observability/index.md) — error budgets, burn rate alerts
- [Phase 9 — Scalability & Performance](09-scalability-performance/index.md) — profiling, bottleneck hunting, capacity math
- [Phase 8 — Security](08-security/index.md) — OAuth flows, RBAC, OWASP top 10

### Week 6 — Design practice at depth
- Do every scenario in the [Scenarios Bank](scenarios-bank/index.md) from scratch on paper, then compare.
- Do 3 more unprompted: "design Dropbox", "design Twitter timeline", "design a recommendation system". Write them up.
- Practice the **10x / 1/100x rescaling discussion** — every scenario page shows it; make it reflexive.

**Staff-round expectation:** you drive the interview. Ask the right clarifying questions, propose alternatives, name the trade-offs *before* the interviewer prompts you.

---

## 🧪 Plan C — "Just for Depth" (open-ended)

**Goal:** Not interviewing. Want to actually understand this stuff.

**Assumes:** No deadline. Reading deeply is more valuable than sprinting.

Pick topics that genuinely interest you. Some sequences that compound well:

### The "distributed systems native" path
1. [Async & Concurrency](01-programming-fundamentals/async-concurrency.md)
2. [Observer pattern](01-programming-fundamentals/design-patterns/observer.md) → [Data Pipelines & Messaging](12-data-pipelines-messaging/index.md)
3. [Distributed Systems](15-distributed-systems/index.md)
4. [Resilience & Fault Tolerance](14-resilience-fault-tolerance/index.md)
5. Scenarios: [Notifications](scenarios-bank/design-notifications-service.md), [Rate Limiter](scenarios-bank/design-rate-limiter.md)
6. Book: *Designing Data-Intensive Applications* — Kleppmann

### The "performance-obsessed" path
1. [Memory Management](01-programming-fundamentals/memory-management.md)
2. [Async & Concurrency](01-programming-fundamentals/async-concurrency.md)
3. [Caching & Optimization](17-caching-optimization/index.md)
4. [Scalability & Performance](09-scalability-performance/index.md)
5. Scenarios: [URL Shortener](scenarios-bank/design-url-shortener.md) — focus on scale-out sections
6. Book: *High Performance Python* — Gorelick & Ozsvald

### The "clean code architect" path
1. [OOP & SOLID](01-programming-fundamentals/oop-solid.md)
2. [Functional Programming](01-programming-fundamentals/functional-programming.md)
3. [All design patterns](01-programming-fundamentals/design-patterns/index.md)
4. [Dependency Injection](01-programming-fundamentals/dependency-injection.md)
5. [Testing Frameworks](01-programming-fundamentals/testing-frameworks.md)
6. [System-Level Design Patterns](13-design-patterns-system/index.md) (Repository, UoW, Service Layer)
7. Books: *Clean Architecture* (Martin), *Domain-Driven Design* (Evans)

---

## 📝 How to study, regardless of plan

1. **Read top-down first pass.** Don't stop on unknown terms; just get the shape.
2. **Second pass: try to re-explain.** To a rubber duck, a colleague, or a notebook. If you can't re-explain, you don't understand it.
3. **Interview-Q section is for active recall.** Cover the answer, attempt, reveal.
4. **Spaced repetition.** Download [flashcards.csv](../exports/flashcards.csv) → import into Anki → study offline.
5. **Build something small.** The topic sticks 10x better once you've written code around it.

> [!TIP]
> Don't confuse *progress through topics* with *internalization*. Re-visit topics 1 day / 3 days / 1 week after first reading. The stuff you forgot is where you need to stay.

---

## 🔗 Useful entry points

- [Progress Dashboard](progress.md) — what's written, what's pending
- [Interview Bank](interview-bank/index.md) — Q&A across the corpus
- [Scenarios Bank](scenarios-bank/index.md) — worked system designs
- [Tags](tags.md) — cross-phase topical discovery
- [Glossary](glossary.md) — terminology lookups
