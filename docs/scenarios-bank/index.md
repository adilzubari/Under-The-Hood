---
tags:
  - scenarios
  - system-design
---

# Scenarios Bank

System-design problems that span multiple phases. Each scenario walks through:

1. **Situation** — what's being built or changed.
2. **Constraints** — scale, latency, team, money.
3. **Approach** — step-by-step reasoning.
4. **Solution** — concrete components, diagrams, code where useful.
5. **Trade-offs** — what was given up, alternatives considered.

## How to use

1. **Cover the solution with your hand.** Read situation + constraints. Sketch a design on paper.
2. **Compare.** Check the solution. Note what you missed and *why*.
3. **Push back.** What if scale is 10x bigger? 10x smaller? What's the cheapest possible version?

## Worked scenarios

- [**Design a URL Shortener**](design-url-shortener.md) — caching, sharding, ID generation, async click counting *(medium — touches Phases 3, 4, 9, 14, 17)*
- [**Design a Rate Limiter**](design-rate-limiter.md) — fixed vs sliding window vs token bucket, Redis ZSET + Lua, fail-open semantics *(medium — touches Phases 5, 14, 15, 17)*
- [**Design a Notifications Service**](design-notifications-service.md) — multi-channel fan-out, idempotency, preferences, priority queues, provider failover *(hard — touches Phases 3, 12, 14, 16)*

## Add your own

Format: copy an existing scenario (they all follow the same 5-section structure), rename, work through it.

Suggested next scenarios:
- Design a real-time chat system
- Design a video upload + processing pipeline
- Design a leaderboard for a game
- Design a search-as-you-type system
- Design a job queue with priorities
- Design a feature-flag service
- Design a distributed file storage (Dropbox-lite)
- Design a payment system with idempotency
- Design an API gateway
