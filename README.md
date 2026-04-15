# SE Docs

A personal software engineering knowledge base — concepts, deep dives, and interactive interview prep.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Pure markdown content; the site adds search, dark mode, collapsible Q&A blocks for self-quizzing, and Mermaid diagrams.

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Structure

- `docs/01-programming-fundamentals/` … `docs/20-soft-skills-system-design/` — the 20 phases
- `docs/interview-bank/` — cross-cutting Q&A (by difficulty, by topic)
- `docs/scenarios-bank/` — system-design scenarios that span multiple phases
- `docs/glossary.md` — quick-reference definitions
- `docs/_templates/topic-template.md` — copy this when starting a new topic

## Adding a new topic

1. Copy `docs/_templates/topic-template.md` into the right phase folder.
2. Fill in the sections in order: TL;DR → Concept Overview → Deep Dive → Trade-offs → Interview Q&A → Scenarios → Related → References.
3. Add the file to `nav:` in `mkdocs.yml`.
4. Replace the `📝 stub` checkbox in the phase's `index.md` with `✅ written`.

## Per-topic format

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

## Status

| Phase | Status |
|---|---|
| 01 — Programming Fundamentals | ✅ Written |
| 02–20 | 📝 Stubs (filled in incrementally) |

## Conventions

- **Code language:** Python primary; add Go/JS/Java tabs only when the comparison is illuminating.
- **Diagrams:** Mermaid for everything — sequence, flow, class, ER.
- **Q&A reveal:** use `??? question "Q: ..."` admonitions so answers are hidden by default.
