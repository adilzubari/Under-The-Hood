---
tags:
  - phase-7
  - cloud
  - infrastructure
---

# Phase 7 — Cloud & Infrastructure

> **Phase abstract:** Where code runs in production. Cloud primitives (compute, storage, networking, IAM), containerization, orchestration, and the IaC + CI/CD layer that automates it all.

📝 **Status: stub.**

## Topics

- [ ] **AWS / GCP / Azure fundamentals** — compute, storage, networking, IAM. Mental model.
- [ ] **AWS Lambda / serverless design** — when serverless wins, cold-start, vendor lock-in trade-offs.
- [ ] **Docker & containerization** — image layers, multi-stage builds, slim images, security scanning.
- [ ] **Kubernetes basics** — Pods, Deployments, Services, ConfigMaps, Secrets, Ingress.
- [ ] **Infrastructure as Code (Terraform, CloudFormation)** — declarative state, modules, drift detection.
- [ ] **CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)** — build → test → deploy. Promotion paths.
- [ ] **Monitoring & alerting (Prometheus, Grafana, CloudWatch)** — pull vs push. Recording rules.
- [ ] **Logging & distributed tracing (ELK, OpenTelemetry)** — see [Phase 1: Logging](../01-programming-fundamentals/logging-observability.md).
- [ ] **Environment configuration (Dev/Staging/Prod)** — config strategy, env-specific overrides.
- [ ] **Secrets management** — AWS Secrets Manager, HashiCorp Vault, sealed secrets.
- [ ] **Service mesh (Istio, Linkerd, AWS App Mesh)** — sidecar proxies. mTLS, traffic shaping.

## Suggested learning order

1. Docker (every modern stack runs containers)
2. K8s basics (Pods → Deployments → Services)
3. CI/CD (GH Actions is the easy entry point)
4. Terraform (own your infra in code)
5. Service mesh — last; only when complexity demands
