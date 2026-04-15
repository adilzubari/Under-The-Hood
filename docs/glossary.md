# Glossary

Quick definitions, linked to deep dives where they exist.

> [!NOTE]
> This glossary grows as topics are written. Add a term here when you first introduce it elsewhere.

## A

**ACID** — Atomicity, Consistency, Isolation, Durability. The transaction guarantees offered by traditional relational databases. Contrast with [BASE](#b).

**Adapter pattern** — Wraps an incompatible interface to make it usable. See [Adapter](01-programming-fundamentals/design-patterns/adapter.md).

**Async** — Non-blocking execution model where a single thread can interleave many I/O-bound tasks via an event loop. See [Async & Concurrency](01-programming-fundamentals/async-concurrency.md).

## B

**BASE** — Basically Available, Soft state, Eventual consistency. The relaxed guarantees offered by many NoSQL/distributed systems.

**Backpressure** — Slowing producers when consumers can't keep up.

## C

**CAP theorem** — In a partitioned distributed system, you can have at most two of: Consistency, Availability, Partition tolerance.

**Circuit breaker** — Pattern that stops calling a failing service after a threshold and gives it time to recover.

**Concurrency** — Doing many things in overlapping time windows. Distinct from parallelism (doing many things *simultaneously*).

## D

**Dependency Injection** — Passing dependencies into an object rather than having it construct them. See [Dependency Injection](01-programming-fundamentals/dependency-injection.md).

## E

**Eventual consistency** — All replicas converge to the same value given no further updates, but may disagree at any moment.

## G

**GIL** — Global Interpreter Lock. Python's mechanism that allows only one thread to execute Python bytecode at a time. See [Async & Concurrency](01-programming-fundamentals/async-concurrency.md).

## I

**Idempotency** — An operation produces the same result whether applied once or many times. Critical for safe retries.

## L

**Liskov Substitution Principle** — Subtypes must be substitutable for their base types without breaking behavior. The "L" in SOLID.

## R

**Race condition** — Outcome depends on unpredictable timing of concurrent operations.

## S

**SOLID** — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. See [OOP & SOLID](01-programming-fundamentals/oop-solid.md).
