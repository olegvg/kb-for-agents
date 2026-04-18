---
name: kb-query
description: Use when answering a question against a .kb/ knowledge base. Enforces indexes-first navigation — reads _root.md, picks area indexes, descends to summaries. Triggers on "query the kb", "ask the knowledge base", "найди в kb", "спроси базу знаний".
---

# kb-query — Answer via Progressive Disclosure

## When to use

User asks a question about a corpus that has a `.kb/` directory. The knowledge base exists — you're reading it, not building it.

If `.kb/` does not exist, suggest `/kb-ingest` and stop.

## Input

- **Question** — natural language, from the user.

## Workflow (strict order)

### 1. Read `_root.md` first

Open `.kb/indexes/_root.md`. Always. No exceptions on first access to the KB.

This is the indexes-first rule. It's cheap (≤300 tokens) and orients you correctly in one hop. Skipping it to "save time" costs more time when you pick the wrong summaries.

### 2. Pick 1–3 area indexes

Based on `_root.md`, identify which areas are relevant to the question. Read those area indexes (`.kb/indexes/<area>.md`).

Typical count: 1 for focused questions, 2–3 for questions that cross domains. More than 3 means either the question is too broad or the areas are over-segmented.

### 3. Descend to summaries

From the area indexes, pick the specific leaf summaries to read. Read them.

### 4. Follow warm references freely — including into decisions

Once inside a summary, if you see a reference to another summary, or a `## Key decisions` section linking to records in `.kb/decisions/`, you may jump directly without returning to the index level.

This relaxation is intentional — see [docs/navigation-rules.md](../../docs/navigation-rules.md). The indexes earn their keep on cold start; warm references are cheap.

For questions of the form "how does X work now, and why was it built that way?" — expect to navigate summary → decision records linked from the summary's `## Key decisions` section. Both halves of the answer live along one navigation path.

### 5. Answer

Answer the question using what you read. Cite sources (file paths, line numbers) from the summaries. If the summaries point at code or docs in the corpus, you may open those sources — but only after the summary has pointed you there.

## Discipline

- **Always `_root.md` first on cold start.** Observable in traces. If you skipped it, you broke the pattern.
- **Bounded summary reads.** If you find yourself wanting to open 5+ summaries, stop. Either the question is too broad (ask the user to narrow) or an index is pointing at too many leaves (lint candidate).
- **If nothing matches, say so.** Don't hallucinate an answer. "The KB has no coverage for this — the answer isn't here" is valid.

## When to suggest re-lint

If during a query you discover:
- A summary references a file that no longer exists.
- An index points at a summary that's missing.
- The content in a summary contradicts what's in the sources.

…suggest `/kb-check-drift` to the user before trusting the answer.

## References

- Navigation rules: [docs/navigation-rules.md](../../docs/navigation-rules.md)
- Drift check: [skills/kb-check-drift/SKILL.md](../kb-check-drift/SKILL.md)
