---
tags:
  - phase-15
  - distributed-systems
---

# Phase 15 — Distributed Systems Concepts

> **Phase abstract:** The hard part of computer science. CAP, consensus, consistency models, time and ordering, replication and partition tolerance — the foundations that explain *why* distributed systems are hard.

📝 **Status: stub.** This phase rewards depth — interview gold for senior roles.

## Topics

- [ ] **CAP theorem** — Consistency, Availability, Partition tolerance. Pick 2 (during a partition).
- [ ] **Consistency models** — strong, sequential, causal, eventual, read-your-writes, monotonic.
- [ ] **Leader election** — Raft and Paxos at a high level. Bully algorithm.
- [ ] **Consensus algorithms (Raft, Paxos)** — when needed (replicated state machines, configuration).
- [ ] **Distributed locks** — Redis Redlock, Zookeeper, etcd. The fencing-token problem.
- [ ] **Clock synchronization, NTP, vector clocks** — physical vs logical clocks. Hybrid logical clocks.
- [ ] **Idempotency in distributed systems** — see [Phase 4](../04-system-design-architecture/index.md). Critical for retries.
- [ ] **Data replication** — sync vs async, leader-follower vs leaderless. Quorum.
- [ ] **Message ordering & delivery guarantees** — at-most-once, at-least-once, exactly-once.
- [ ] **Partition tolerance** — what happens during network splits. Split-brain scenarios.
- [ ] **Eventual consistency** — bounded vs unbounded staleness. CRDTs.
- [ ] **Two-phase commit & saga orchestration** — XA's reputation. Sagas as the modern alternative.

## Suggested learning order

1. CAP + consistency models (the foundation)
2. Replication strategies (sync/async, leader/leaderless)
3. Consensus (Raft is more digestible than Paxos)
4. Time & ordering (vector clocks, HLC)
5. Sagas vs 2PC (transactions across services)

## Recommended reading

- *Designing Data-Intensive Applications* — Martin Kleppmann (the bible)
- *Database Internals* — Alex Petrov
- The Raft paper — "In Search of an Understandable Consensus Algorithm"
