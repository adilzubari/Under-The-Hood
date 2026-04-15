---
tags:
  - phase-5
  - networking
  - protocols
---

# Phase 5 — Networking & Communication

> **Phase abstract:** What happens between the wire and your code. HTTP/TCP basics, alternative transports (gRPC, WebSockets), edge concerns (DNS, CDN, reverse proxy), and the resilience patterns that any cross-network call needs.

📝 **Status: stub.**

## Topics

- [ ] **HTTP/HTTPS protocol** — methods, status codes, headers, HTTP/2 vs HTTP/3 (QUIC).
- [ ] **TCP/IP basics** — handshake, slow-start, congestion control. Why it matters for tail latency.
- [ ] **WebSockets** — bidirectional persistent connection. When vs SSE vs polling.
- [ ] **DNS & load balancing concepts** — A/AAAA/CNAME, TTLs, geo-DNS, round-robin DNS limits.
- [ ] **gRPC & binary communication** — protobuf, streaming, when faster than JSON+HTTP/1.1.
- [ ] **REST vs RPC** — semantics differ: resources vs actions. When each fits.
- [ ] **Reverse proxy (Nginx, Envoy)** — termination, routing, observability hooks.
- [ ] **CDN concepts** — edge caching, origin shield, cache keys, invalidation.
- [ ] **API rate limiting & throttling** — algorithms (token, leaky, sliding). Per-user vs per-IP.
- [ ] **Circuit breaker (pybreaker)** — see [Phase 14](../14-resilience-fault-tolerance/index.md).
- [ ] **Retries & exponential backoff** — see [Phase 1: Error Handling](../01-programming-fundamentals/error-handling.md).

## Suggested learning order

1. HTTP basics + HTTP/2 differences
2. TCP fundamentals (handshake, retransmission — ties to tail latency)
3. Reverse proxy + CDN (edge architecture)
4. Rate limiting + retries (the resilience pair)
