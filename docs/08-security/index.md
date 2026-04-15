---
tags:
  - phase-8
  - security
---

# Phase 8 — Security

> **Phase abstract:** The defensive mindset. OWASP top 10 categories, the auth/authz stack, transport security, and the operational hygiene (rotation, audit, redaction) that separates secure systems from secure-on-paper systems.

📝 **Status: stub.**

## Topics

- [ ] **HTTPS, TLS/SSL** — handshake, cert chains, certificate pinning, Let's Encrypt.
- [ ] **Authentication & Authorization (OAuth2, JWT)** — flows, JWT structure, refresh tokens.
- [ ] **Role-Based Access Control (RBAC)** — vs ABAC. Permission models in practice.
- [ ] **CORS** — preflight, what's allowed, common misconfigurations.
- [ ] **CSRF, XSS, SQLi, SSRF prevention** — concrete defenses for each. CSP headers, parameterized queries.
- [ ] **Input validation & sanitization** — at boundaries. Trust nothing.
- [ ] **Secure password storage (bcrypt, Argon2)** — why not SHA-256. Cost factors.
- [ ] **Rate limiting & brute-force prevention** — see [Phase 5](../05-networking-communication/index.md).
- [ ] **Data encryption at rest and in transit** — KMS, envelope encryption.
- [ ] **Security headers (CSP, HSTS)** — what each one does. Sane defaults.
- [ ] **API key & token management** — rotation, scoping, revocation.
- [ ] **Auditing & logging security events** — auth failures, privilege escalations, config changes.

## Suggested learning order

1. OAuth2 + JWT (every modern API)
2. OWASP top 10 (XSS, SQLi, CSRF — interview classics)
3. Password storage (bcrypt vs argon2 — small but important)
4. Encryption at rest/transit (KMS basics)
5. Audit/logging (the operational closing of the loop)
