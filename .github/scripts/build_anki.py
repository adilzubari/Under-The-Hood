#!/usr/bin/env python3
"""Scrape every <details>/<summary>...</summary>...</details> block across docs/
and emit exports/flashcards.csv ready for Anki import.

CSV columns (Anki import schema):
  Front | Back | Tags

Front = the question text (from <summary>).
Back  = the answer (the markdown inside <details>, rendered to HTML so Anki
        shows formatted text).
Tags  = space-separated frontmatter tags plus the source topic title.

Usage in Anki:
  File → Import → select flashcards.csv
  Field separator: Comma
  Allow HTML in fields: YES
  First field: Front, second: Back, third: Tags
"""
from __future__ import annotations

import csv
import html as html_escape_mod
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS = REPO_ROOT / "docs"
EXPORTS = REPO_ROOT / "exports"

SKIP_DIRS = {"_templates", "interview-bank"}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TAGS_BLOCK_RE = re.compile(r"^tags:\n((?:  - .+\n)+)", re.MULTILINE)
TAG_ITEM_RE = re.compile(r"^  - (.+)$", re.MULTILINE)
DIFFICULTY_RE = re.compile(r"^difficulty:\s*(\S+)", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

# Whole Q&A block — non-greedy content between <details>...</details>.
QA_RE = re.compile(
    r"<details>\s*<summary>(.*?)</summary>\s*(.*?)\s*</details>",
    re.DOTALL,
)
STRIP_TAGS_RE = re.compile(r"</?(strong|em|code|b|i)>", re.IGNORECASE)


def parse_frontmatter(text: str) -> tuple[list[str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return [], "unknown"
    block = m.group(1)
    tm = TAGS_BLOCK_RE.search(block + "\n")
    tags = TAG_ITEM_RE.findall(tm.group(1)) if tm else []
    dm = DIFFICULTY_RE.search(block)
    difficulty = dm.group(1).strip() if dm else "unknown"
    return tags, difficulty


def extract_title(text: str) -> str:
    m = H1_RE.search(text)
    return m.group(1).strip() if m else "(untitled)"


def markdown_to_basic_html(md: str) -> str:
    """Convert a small subset of markdown to HTML for Anki.

    We intentionally keep this minimal — Anki's renderer is limited and most
    answers are short. Code blocks, inline code, bold/italic, and paragraph
    breaks are the 95% case.
    """
    md = md.strip()

    # Fenced code blocks ```lang\n...\n```  → <pre><code>...</code></pre>
    def _fence(m):
        code = html_escape_mod.escape(m.group(2))
        return f"<pre><code>{code}</code></pre>"
    md = re.sub(r"```(\w*)\n(.*?)```", _fence, md, flags=re.DOTALL)

    # Inline code `x` → <code>x</code>
    md = re.sub(
        r"`([^`]+)`",
        lambda m: f"<code>{html_escape_mod.escape(m.group(1))}</code>",
        md,
    )

    # Bold **x** → <b>x</b>
    md = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", md)
    # Italic *x* → <i>x</i>  (after bold to avoid conflict)
    md = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", md)

    # Bullets - foo → •  foo (Anki doesn't always render <ul> cleanly)
    md = re.sub(r"^- ", "• ", md, flags=re.MULTILINE)

    # Paragraph breaks
    md = md.replace("\n\n", "<br><br>")
    md = md.replace("\n", " ")

    return md.strip()


def strip_inline_tags(s: str) -> str:
    return STRIP_TAGS_RE.sub("", s).strip()


def main():
    rows = []
    topic_count = 0

    for md_path in sorted(DOCS.rglob("*.md")):
        rel_parts = md_path.relative_to(DOCS).parts
        if any(p in SKIP_DIRS for p in rel_parts):
            continue
        if md_path.name == "index.md":
            continue
        text = md_path.read_text()
        tags, difficulty = parse_frontmatter(text)
        title = extract_title(text)

        matches = list(QA_RE.finditer(text))
        if not matches:
            continue
        topic_count += 1

        tag_str = " ".join(tags + [f"topic-{md_path.stem}", f"diff-{difficulty}"])

        for m in matches:
            summary_raw = m.group(1).strip()
            body_md = m.group(2).strip()

            front = strip_inline_tags(summary_raw)
            back = markdown_to_basic_html(body_md)
            # Always include the source topic on the back so the card stays
            # self-contained if you study it out of context.
            back += f"<br><br><i>Source: {html_escape_mod.escape(title)}</i>"

            rows.append({"Front": front, "Back": back, "Tags": tag_str})

    EXPORTS.mkdir(exist_ok=True)
    out = EXPORTS / "flashcards.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Front", "Back", "Tags"])
        w.writeheader()
        w.writerows(rows)

    # Also write a README so users know how to import.
    (EXPORTS / "README.md").write_text(f"""# Exports

Auto-generated study artifacts. Don't hand-edit — rerun
[`.github/scripts/build_anki.py`](../.github/scripts/build_anki.py) instead
(CI does this automatically on push).

## `flashcards.csv` — Anki-compatible deck

**{len(rows)} flashcards** across {topic_count} topics.

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
""")

    print(f"Wrote {out.relative_to(REPO_ROOT)}")
    print(f"  {len(rows)} flashcards across {topic_count} topics")


if __name__ == "__main__":
    main()
