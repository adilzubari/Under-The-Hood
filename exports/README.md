# Exports

Auto-generated study artifacts. Don't hand-edit — rerun
[`.github/scripts/build_anki.py`](../.github/scripts/build_anki.py) instead
(CI does this automatically on push).

## `flashcards.csv` — Anki-compatible deck

**91 flashcards** across 17 topics.

### Import into Anki

1. Open Anki → **File → Import...** → select `flashcards.csv`.
2. In the import dialog:
   - **Field separator:** `Comma`
   - **Allow HTML in fields:** ✅
   - **Fields separated by:** `,`
   - **Field 1:** Front, **Field 2:** Back, **Field 3:** Tags
3. Click **Import**. Done — study anywhere, offline.

### Re-import after updates

Anki dedupes by "Front" text by default. When new questions are added:

1. Re-download `flashcards.csv`.
2. Import again with the same mapping.
3. New cards are added; existing ones are skipped.

### Columns

- **Front** — the question.
- **Back** — the model answer (minimal HTML formatting preserved).
- **Tags** — frontmatter tags + source topic + difficulty. Filter with
  Anki tag-browser.
