---
tags:
  - interview
---

# Interview Bank

Every Q&A across the repo, indexed three ways. These pages are **auto-generated** from the `<details>`/`<summary>` blocks inside each topic file — add questions to a topic, push, CI regenerates these indexes.

## Browse

- **[By Difficulty](by-difficulty.md)** — grouped easy / medium / hard. Warm up, then stretch.
- **[By Topic](by-topic.md)** — grouped by phase and topic. Targeted refresh before a specific interview.
- **[All Questions (flat)](all-questions.md)** — numbered list of every Q. Useful for random-study mode or <kbd>Ctrl+F</kbd> across the full corpus.

## How to study

The most useful study mode is **active recall**. Pick a question from any index, follow the link, **try to answer before clicking** to reveal the model answer.

1. **Don't read answers first.** The reveal mechanic is the whole point.
2. **Speak answers aloud.** Surfaces gaps.
3. **Spaced repetition.** Revisit 1 day / 3 days / 1 week later.
4. **Generate scenarios.** "Where would this crop up in production?" Then check the [Scenarios Bank](../scenarios-bank/index.md).

## How it's built

[`.github/scripts/build_qa_bank.py`](../../.github/scripts/build_qa_bank.py) walks every topic file, extracts `<details>/<summary>` pairs, and emits these three indexes. Difficulty comes from the topic's frontmatter (`difficulty: easy|medium|hard`). The bot regenerates on push to `main` when any `docs/**/*.md` changes.
