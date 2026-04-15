# Under The Hood

<p align="center">
  <b>A free, community-built software engineering knowledge base.</b><br>
  Concepts, deep dives, interactive interview Q&A, and worked system-design scenarios — organized as 20 phases. Read directly on GitHub. No setup, no paywall, no signup.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/adilzubari/Under-The-Hood?color=brightgreen"></a>
  <a href="https://github.com/adilzubari/Under-The-Hood/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/adilzubari/Under-The-Hood?style=social"></a>
  <a href="https://github.com/adilzubari/Under-The-Hood/fork"><img alt="GitHub forks" src="https://img.shields.io/github/forks/adilzubari/Under-The-Hood?style=social"></a>
  <a href="https://github.com/adilzubari/Under-The-Hood/pulls"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/adilzubari/Under-The-Hood">
</p>

<p align="center">
  <a href="#-full-table-of-contents">Contents</a> •
  <a href="#-how-to-use-this-for-interview-prep">How to Study</a> •
  <a href="docs/scenarios-bank/index.md">Scenarios</a> •
  <a href="docs/interview-bank/index.md">Interview Q&A</a> •
  <a href="docs/study-plans.md">Study Plans</a> •
  <a href="CONTRIBUTING.md">Contribute</a> •
  <a href="SUPPORT.md">Support</a>
</p>

> [!TIP]
> **If this helps you, please [⭐ star the repo](https://github.com/adilzubari/Under-The-Hood/stargazers).** It's the single most effective way to help others find this. Costs nothing; means a lot.

---

## 🎁 What's inside

- **20 phases** of SE concepts — from OOP/SOLID to distributed systems to soft skills.
- **17 fully-written topics** in Phase 1 (Programming Fundamentals), with the rest scaffolded and filled in as I go.
- **91+ interview questions** with model answers, collapsed so you can self-quiz.
- **5 worked system-design scenarios** (URL shortener, rate limiter, notifications, real-time chat, priority job queue) — each with a full walkthrough, trade-off table, and 10x / 1÷100x scaling discussion.
- **Anki-ready flashcard export** for offline study on any device.
- **Curated study plans** for different paths (mid-level sprint, senior system design, depth-first).
- Pure markdown — everything renders natively on GitHub. No build. No install. No server.

Built mostly for interview prep and personal reference, but works well as a shared team resource or a teaching aid.

---

## 📚 Full Table of Contents

### Phase 1 — Programming Fundamentals ✅ *Fully written*

- [Overview](docs/01-programming-fundamentals/index.md)
- [OOP & SOLID](docs/01-programming-fundamentals/oop-solid.md)
- [Functional Programming](docs/01-programming-fundamentals/functional-programming.md)
- **Design Patterns** — [overview](docs/01-programming-fundamentals/design-patterns/index.md)
  - Creational: [Singleton](docs/01-programming-fundamentals/design-patterns/singleton.md) · [Factory](docs/01-programming-fundamentals/design-patterns/factory.md) · [Builder](docs/01-programming-fundamentals/design-patterns/builder.md)
  - Structural: [Adapter](docs/01-programming-fundamentals/design-patterns/adapter.md) · [Decorator](docs/01-programming-fundamentals/design-patterns/decorator.md) · [Proxy](docs/01-programming-fundamentals/design-patterns/proxy.md)
  - Behavioral: [Strategy](docs/01-programming-fundamentals/design-patterns/strategy.md) · [Observer](docs/01-programming-fundamentals/design-patterns/observer.md) · [Chain of Responsibility](docs/01-programming-fundamentals/design-patterns/chain-of-responsibility.md)
- [Dependency Injection](docs/01-programming-fundamentals/dependency-injection.md)
- [Async, Concurrency & Threading](docs/01-programming-fundamentals/async-concurrency.md)
- [Memory Management & GC](docs/01-programming-fundamentals/memory-management.md)
- [Error Handling](docs/01-programming-fundamentals/error-handling.md)
- [Logging & Observability](docs/01-programming-fundamentals/logging-observability.md)
- [Testing Frameworks](docs/01-programming-fundamentals/testing-frameworks.md)

### Phases 2-20 — 📝 *Scaffolded; topics fill in incrementally*

Each phase index lists its planned topics with a checklist and learning order. Live progress: [**Progress Dashboard**](docs/progress.md).

| # | Phase |
|---|---|
| 2 | [Backend & APIs](docs/02-backend-apis/index.md) |
| 3 | [Database & Storage](docs/03-database-storage/index.md) |
| 4 | [System Design & Architecture](docs/04-system-design-architecture/index.md) |
| 5 | [Networking & Communication](docs/05-networking-communication/index.md) |
| 6 | [Concurrency & Async Systems](docs/06-concurrency-async/index.md) |
| 7 | [Cloud & Infrastructure](docs/07-cloud-infrastructure/index.md) |
| 8 | [Security](docs/08-security/index.md) |
| 9 | [Scalability & Performance](docs/09-scalability-performance/index.md) |
| 10 | [DevOps & Observability](docs/10-devops-observability/index.md) |
| 11 | [Testing & Quality](docs/11-testing-quality/index.md) |
| 12 | [Data Pipelines & Messaging](docs/12-data-pipelines-messaging/index.md) |
| 13 | [System-Level Design Patterns](docs/13-design-patterns-system/index.md) |
| 14 | [Resilience & Fault Tolerance](docs/14-resilience-fault-tolerance/index.md) |
| 15 | [Distributed Systems](docs/15-distributed-systems/index.md) |
| 16 | [API Lifecycle Management](docs/16-api-lifecycle/index.md) |
| 17 | [Caching & Optimization](docs/17-caching-optimization/index.md) |
| 18 | [Search & Indexing](docs/18-search-indexing/index.md) |
| 19 | [API Reliability & Observability](docs/19-api-reliability-observability/index.md) |
| 20 | [Soft Skills & System Design](docs/20-soft-skills-system-design/index.md) |

### Cross-cutting

- 🎯 **[Interview Bank](docs/interview-bank/index.md)** — every Q&A indexed [by difficulty](docs/interview-bank/by-difficulty.md) and [by topic](docs/interview-bank/by-topic.md). Auto-generated from every `<details>` block across the repo.
- 🏗️ **[Scenarios Bank](docs/scenarios-bank/index.md)** — system-design problems that span multiple phases. Worked examples: [URL Shortener](docs/scenarios-bank/design-url-shortener.md), [Rate Limiter](docs/scenarios-bank/design-rate-limiter.md), [Notifications Service](docs/scenarios-bank/design-notifications-service.md), [Real-Time Chat](docs/scenarios-bank/design-real-time-chat.md), [Priority Job Queue](docs/scenarios-bank/design-priority-job-queue.md).
- 🗺️ **[Study Plans](docs/study-plans.md)** — curated sequenced tracks (mid-level sprint, senior system design, depth-first).
- 📖 **[Glossary](docs/glossary.md)** — quick definitions linked to deep dives.
- 🏷️ **[Tags](docs/tags.md)** — cross-phase discovery by topic tag.
- 📊 **[Progress](docs/progress.md)** — phase completion dashboard.
- 🃏 **[Flashcards](exports/flashcards.csv)** — Anki-ready CSV of every Q&A. Download, import into Anki, study offline.

---

## 🧠 How to use this for interview prep

1. **Pick a topic page.** Skim TL;DR + Concept Overview.
2. **Skip to the bottom: Interview Questions section.** Each question is collapsed.
3. **Read the question. Try to answer in your head or out loud.**
4. **Click to reveal the model answer.** Compare. Mark topics you didn't nail.
5. **For system design:** work through the [Scenarios Bank](docs/scenarios-bank/index.md). Cover the solution, sketch your own, then compare.

> [!TIP]
> For repo-wide search, press <kbd>/</kbd> or <kbd>t</kbd> anywhere on GitHub. Searches across every file instantly — no separate search tool needed.

For curated learning paths by goal (mid-level interview sprint / senior system design / depth-first), see **[Study Plans](docs/study-plans.md)**.

---

## 📐 Per-topic format

Every page follows the same skeleton so you always know where to look:

| Section | Purpose |
|---|---|
| **TL;DR** | One-paragraph elevator pitch you could give in an interview |
| **Concept Overview** | The abstract — what it is, when it matters, why it exists |
| **Deep Dive** | The details: code, diagrams, comparisons, edge cases |
| **Trade-offs & Pitfalls** | When to use, when not to, common mistakes |
| **Interview Questions** | Collapsible Q&A — try answering before clicking to reveal |
| **Scenarios** | Realistic problem statements with worked solutions |
| **Related Topics** | Cross-links to connected concepts |
| **References** | Books, articles, official docs |

---

## ✍️ Contributing

**PRs genuinely welcome.** See **[CONTRIBUTING.md](CONTRIBUTING.md)** for:

- The **short-commits rule** (one logical change per commit)
- The **per-topic template** and writing conventions
- The **Q&A syntax** (HTML `<details>` — works on GitHub)
- The **GitHub Alert** callout syntax
- How to add a new topic (no local setup required — just edit markdown)

Good first contributions:
- **Fix a typo or broken link** — low risk, high appreciation
- **Add an Interview Question** to an existing topic
- **Write a scenario** from the [suggested list](docs/scenarios-bank/index.md#add-your-own)
- **Fill in a Phase 2-20 topic** — each phase's `index.md` has a checklist

---

## 🧡 Support this project

**This is a free gift to the community.** MIT-licensed, no paywall, no ads, no tracking.

The most valuable support costs you nothing:

- ⭐ **[Star the repo](https://github.com/adilzubari/Under-The-Hood/stargazers)** — helps others discover it
- 🔁 **Share it** on LinkedIn / X / Reddit / your team Slack
- ✍️ **Contribute** — typos, corrections, new topics, scenarios
- 💬 **[Open an issue](https://github.com/adilzubari/Under-The-Hood/issues/new/choose)** with feedback

If the content has materially helped you (landed an offer, passed a round, replaced a paid course) and you want to buy me a coffee, see **[SUPPORT.md](SUPPORT.md)** for sponsor options including Pakistan-compatible channels (GitHub Sponsors, Buy Me a Coffee, Ko-fi, Patreon, direct transfer).

> [!NOTE]
> All financial support is **strictly optional** and has **zero effect on content access**. The content will always be free.

---

## 📦 Repository layout

```
.
├── README.md                 ← you are here
├── CONTRIBUTING.md           ← conventions and how to add topics
├── SUPPORT.md                ← ways to support + sponsor links
├── LICENSE                   ← MIT
├── .github/
│   ├── FUNDING.yml           ← sponsor button config
│   ├── workflows/            ← CI for link checks + auto-generated docs
│   └── scripts/              ← Python helpers (Q&A scraper, etc.)
├── exports/
│   └── flashcards.csv        ← auto-generated Anki deck
└── docs/
    ├── index.md              ← landing page
    ├── progress.md           ← phase completion dashboard (auto-generated)
    ├── tags.md               ← tag index (auto-generated)
    ├── study-plans.md        ← curated learning tracks
    ├── glossary.md
    ├── _templates/
    │   └── topic-template.md ← copy when starting a new topic
    ├── 01-programming-fundamentals/    ← Phase 1 (written)
    ├── 02-backend-apis/                ← Phase 2 (stub)
    ├── …
    ├── 20-soft-skills-system-design/   ← Phase 20 (stub)
    ├── interview-bank/                 ← cross-cutting Q&A index (auto-generated)
    └── scenarios-bank/                 ← system-design scenarios
```

---

## 📜 License

[MIT](LICENSE). Use the content freely — for study, for teaching, for internal team docs. Attribution is appreciated but not required.

---

<p align="center">
  <sub>Built with 🧡 by <a href="https://github.com/adilzubari">Muhammad Adil</a>. Free forever.<br>
  If this helped you, <a href="https://github.com/adilzubari/Under-The-Hood/stargazers">star the repo</a> and share it with someone who's studying.</sub>
</p>
