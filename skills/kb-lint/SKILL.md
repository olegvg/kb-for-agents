---
name: kb-lint
description: Use when updating .kb/ to reflect recent changes in a given corpus path. Reads git diff since last-linted SHA, updates affected summaries and indexes, advances .kb-state.json. Triggers on "lint the kb", "update knowledge base", "обновить kb", "синхронизировать базу знаний".
---

# kb-lint — Update `.kb/` After Corpus Changes

## When to use

User invokes `/kb-lint <path>` after making changes to the corpus. Manual, targeted operation. Never automatic.

If the user didn't specify a path, ask for one. Do not lint the whole corpus by default — scope keeps the operation fast and reviewable.

## Input

- **Path** — a subdirectory or file within the corpus.

## Workflow

### 1. Read state

Open `.kb/.kb-state.json`. Extract `last_linted_sha`.

If the file doesn't exist: this is first lint. Suggest `/kb-ingest` instead, which builds the KB from scratch.

If `last_linted_sha == "no-git"`: tell the user the corpus is not a git repo and lint cannot run. Stop.

### 2. Diff the path

Run:

```bash
git -C <corpus-root> diff <last_linted_sha>..HEAD -- <path>
```

Read the diff. Identify:
- Changed files (modified content).
- Renamed files (old path → new path).
- Deleted files.
- New files in scope.

### 3. Find affected summaries and indexes

- Grep `.kb/summaries/` for references to each changed file path. Those summaries need review.
- Grep `.kb/indexes/` for references to summaries that are themselves affected. Those indexes may need review.

### 4. Update summaries

For each affected summary:
- Re-read the relevant sources (the changed files).
- Rewrite the summary where content has shifted.
- Keep one-topic-per-file discipline. If a summary's scope has grown past one topic, split it and update the parent index.

### 5. Update indexes

If summaries were split, merged, added, or removed — update the area index. If an entire area disappeared or a new area emerged, update `_root.md`.

Enforce the 300-token index budget. Split or trim if violated.

### 6. Advance state

Rewrite `.kb/.kb-state.json`:

- `last_linted_sha` → current HEAD SHA: `git -C <corpus-root> rev-parse HEAD`.
- `last_linted_at` → current UTC ISO-8601 timestamp: `date -u +"%Y-%m-%dT%H:%M:%SZ"`.
- `schema_version` → unchanged.

### 7. Report

Summarize to the user:
- Files changed in diff scope.
- Summaries updated (with paths).
- Indexes updated (with paths).
- State advanced to SHA `<new-sha>`.

## Discipline

- **Scoped to the path argument.** Do not touch summaries for files outside `<path>`'s diff scope, even if you notice drift there. That's `/kb-check-drift`'s job — it's the user's call whether to lint those next.
- **One commit-worthy change per invocation.** If the lint turns massive, the plan should have been to split the path. Say so and ask the user to narrow scope.
- **State file is sacred.** Only advance `last_linted_sha` after summaries and indexes are actually updated. A lint that fails halfway must not advance state.

## Failure modes

- **`.kb/.kb-state.json` missing** → suggest `/kb-ingest`.
- **`last_linted_sha` not reachable from HEAD** (force-push, history rewrite) → ask the user how to recover. Safest recovery: treat the full history of `<path>` as diff scope, re-read, rewrite. Confirm before proceeding.
- **Merge conflicts in the diff** → the corpus has unresolved state. Ask user to resolve before linting.

## References

- Pattern: [docs/concept.md](../../docs/concept.md)
- Lint rationale: [docs/lint-strategy.md](../../docs/lint-strategy.md)
- Drift-first pass: [skills/kb-check-drift/SKILL.md](../kb-check-drift/SKILL.md)
