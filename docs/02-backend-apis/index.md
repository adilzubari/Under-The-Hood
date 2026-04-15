---
tags:
  - phase-2
  - backend
  - apis
---

# Phase 2 — Backend Frameworks & APIs

> **Phase abstract:** How requests turn into responses. Protocol choices (REST, GraphQL, gRPC), framework mechanics (middleware, validation, DI), and the operational concerns that show up in every API: auth, versioning, pagination, file uploads.

📝 **Status: stub.** Topic checklist below. To start a topic: copy `docs/_templates/topic-template.md` into this folder, fill it out, add to `mkdocs.yml` nav.

## Topics

- [ ] **REST API design principles** — resources, verbs, status codes, HATEOAS (rare in practice). Idempotency.
- [ ] **GraphQL basics** — schemas, queries, mutations, resolvers, N+1 problem, DataLoader.
- [ ] **gRPC and Protocol Buffers** — binary protocol, code generation, streaming RPCs, when to choose over REST.
- [ ] **FastAPI / Django / Flask** — strengths, request lifecycle, ecosystem differences.
- [ ] **API versioning & backward compatibility** — URL vs header vs media type. Deprecation strategy.
- [ ] **Middleware & request/response lifecycle** — where auth/logging/CORS plugs in. ASGI vs WSGI.
- [ ] **Dependency injection (FastAPI `Depends`)** — see [Phase 1: DI](../01-programming-fundamentals/dependency-injection.md).
- [ ] **Authentication & Authorization** — session vs JWT vs OAuth2. When to use which.
- [ ] **API documentation (OpenAPI / Swagger)** — generated from code vs hand-written. Contract-first vs code-first.
- [ ] **Pagination, filtering, sorting** — offset vs cursor pagination. Trade-offs.
- [ ] **Validation (Pydantic / Marshmallow)** — schema-driven validation. Where to validate (DTO, domain).
- [ ] **File upload/download** — multipart, streaming, signed URLs (delegate to S3).

## Suggested learning order

1. REST principles → API versioning (form precedes evolution)
2. Auth (the next thing every API needs)
3. Validation + middleware (request lifecycle in practice)
4. GraphQL & gRPC (alternatives — once you know REST well)
