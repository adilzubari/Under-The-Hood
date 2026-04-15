# Under The Hood

> A personal software engineering knowledge base — concepts, deep dives, and **interactive interview prep** organized as 20 phases. Browse it on GitHub or run the MkDocs site locally.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) but every page is plain markdown — Q&A blocks use HTML `<details>` so they're collapsible **directly on github.com** without needing to clone or run anything.

---

## Two ways to read it

| | On GitHub | Locally with MkDocs |
|---|---|---|
| **Cost** | Free, zero setup | One-time `pip install` |
| **Search** | Repo-wide search | Full-text search box, instant |
| **Q&A reveal** | ✅ Native `<details>` | ✅ Material styling |
| **Mermaid diagrams** | ✅ Native | ✅ Plugin |
| **Dark mode** | ✅ GitHub setting | ✅ Toggle in header |
| **Best for** | Quick reference, mobile | Long study sessions |

### Browse on GitHub
Just click into the folders below — every file renders cleanly.

### Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```
Then open <http://127.0.0.1:8000>.

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

Each phase index lists its planned topics with a checklist and learning order:

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

- 🎯 **[Interview Bank](docs/interview-bank/index.md)** — every Q&A indexed [by difficulty](docs/interview-bank/by-difficulty.md) and [by topic](docs/interview-bank/by-topic.md).
- 🏗️ **[Scenarios Bank](docs/scenarios-bank/index.md)** — system-design problems that span multiple phases. Worked example: [Design a URL Shortener](docs/scenarios-bank/design-url-shortener.md).
- 📖 **[Glossary](docs/glossary.md)** — quick definitions linked to deep dives.

---

## 🧠 How to use this for interview prep

1. **Pick a topic page.** Skim TL;DR + Concept Overview.
2. **Skip to the bottom: Interview Questions section.** Each question is collapsed.
3. **Read the question. Try to answer in your head or out loud.**
4. **Click to reveal the model answer.** Compare. Mark topics you didn't nail to revisit.
5. **For system design:** work through the [Scenarios Bank](docs/scenarios-bank/index.md). Cover the solution. Sketch your own. Compare.

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

## ✍️ Adding a new topic

1. Copy [`docs/_templates/topic-template.md`](docs/_templates/topic-template.md) into the right phase folder.
2. Fill in the sections in order: TL;DR → Concept Overview → Deep Dive → Trade-offs → Interview Q&A → Scenarios → Related → References.
3. Add the file to `nav:` in `mkdocs.yml`.
4. Replace the `[ ]` checkbox in the phase's `index.md` with `[x]`.
5. Add the new Q&A links to [`docs/interview-bank/by-difficulty.md`](docs/interview-bank/by-difficulty.md) and [`by-topic.md`](docs/interview-bank/by-topic.md).
6. Run `mkdocs build --strict` locally to catch broken links and warnings.

---

## 🤝 Contributing & commit conventions

- **Short, focused commits.** One logical change per commit (e.g., "convert Q&A syntax", "add caching topic"). Avoid bundled commits.
- **Imperative subject lines** (e.g., "Add Singleton pattern", not "Added").
- **Body explains *why*, not *what*.** The diff shows what.
- **Verify before committing:** `mkdocs build --strict` should pass.
- Don't push to `main` directly for substantive content additions — branch + PR.

### Q&A blocks must use `<details>`, not `???`

GitHub doesn't render MkDocs admonition syntax (`??? question "..."`). Use HTML:

```markdown
<details>
<summary><strong>Q1: How does X work?</strong></summary>

Answer text. **Blank line above is required** for markdown to render inside.

</details>
```

This works in both GitHub and MkDocs Material.

### Notes / callouts use GitHub Alert blockquotes

```markdown
> [!NOTE]
> A note that styles nicely on GitHub and falls back to a plain blockquote in MkDocs.
```

Other types: `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`.

---

## 🛠️ Conventions

- **Code language:** Python primary; add Go/JS/Java tabs only when the comparison is illuminating.
- **Diagrams:** Mermaid (` ```mermaid ` fences) — renders natively on GitHub and in MkDocs.
- **Frontmatter:** YAML at the top of each topic file with `tags`, `difficulty`, `status`. Used by Material's tags plugin; harmless on GitHub.

---

## 📦 Repository layout

```
.
├── README.md                 ← you are here
├── mkdocs.yml                ← MkDocs Material config
├── requirements.txt          ← mkdocs-material, mkdocs-mermaid2-plugin, …
├── .gitignore
└── docs/
    ├── index.md              ← landing page (also the MkDocs home)
    ├── _templates/
    │   └── topic-template.md ← copy when starting a new topic
    ├── stylesheets/extra.css
    ├── 01-programming-fundamentals/    ← Phase 1 (written)
    ├── 02-backend-apis/                ← Phase 2 (stub)
    ├── …
    ├── 20-soft-skills-system-design/   ← Phase 20 (stub)
    ├── interview-bank/                 ← cross-cutting Q&A index
    ├── scenarios-bank/                 ← system-design scenarios
    └── glossary.md
```

---

## 📜 License

Personal knowledge base — content is for educational reference. Code snippets are illustrative; use them freely.
