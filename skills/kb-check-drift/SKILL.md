---
name: kb-check-drift
description: Use when checking whether .kb/ is out of date with the corpus. Read-only. Applies heuristics to git log since last-linted SHA and returns re-lint candidates. Triggers on "check drift", "is the kb stale", "что устарело в kb", "нужна ли синхронизация".
---

# kb-check-drift — Surface Re-Lint Candidates

## When to use

User wants to know whether the KB is stale without committing to a rewrite. Run this before a query to decide whether to trust the KB, or periodically to spot drift.

**Read-only.** This skill NEVER modifies `.kb/` or `.kb-state.json`. If changes are warranted, emit a list of `/kb-lint <path>` commands for the user to run.

## Input

None beyond the corpus context.

## Workflow

### 1. Read state

Open `.kb/.kb-state.json`. Extract `last_linted_sha` and `last_linted_at`.

If missing: report "no KB state — ingest or lint has never run". Do not proceed.

If `last_linted_sha == "no-git"`: report that drift check requires git. Stop.

### 2. Log the delta

Run:

```bash
git -C <corpus-root> log --stat <last_linted_sha>..HEAD
```

Capture the list of changed files, rename/copy stats, and commit messages.

### 3. Apply the heuristic

The heuristic is a checklist. **Tune it by editing this file.** The checklist below is the default.

For each signal, list the affected areas:

- **New files above threshold** — if a single directory or area saw ≥5 new files since last lint, flag that area.
- **File renames or moves** — any rename under a directory referenced in `.kb/indexes/` is a flag. Index references are stale by definition.
- **Changes to files referenced by existing indexes** — grep `.kb/indexes/` for paths; if any flagged path appears, the index entry is suspect.
- **Changes to files referenced by existing summaries** — grep `.kb/summaries/` for paths; if any flagged path appears, the summary is suspect.
- **New top-level directory** — may mean a new area needs an index.
- **Migration / schema files** (e.g. `migrations/**`, `*.sql`, `schema.*`) — semantic shifts likely; any area touching data is suspect.
- **Deleted files referenced in `.kb/`** — hard flag. The KB points at something that no longer exists.
- **Completed plan with no decision record** — if a plan file under `docs/plans/` (or similar) has a sibling checklist with all items ticked, and no matching file exists in `.kb/decisions/` (match by slug), recommend `/kb-distill <plan-path>`. Soft flag — not every plan yields a durable decision.

### 4. Report

Emit a structured list. Example shape:

```
Drift candidates (KB last linted at <timestamp>, SHA <short-sha>):

Area: billing
  Reason: 7 new files under src/billing/ (above threshold 5)
  Recommendation: /kb-lint src/billing/

Area: auth
  Reason: src/auth/session.ts (referenced by .kb/summaries/auth/session.md) has changed
  Recommendation: /kb-lint src/auth/

Hard flags:
  .kb/summaries/search/indexer.md references src/search/legacy.ts — file no longer exists.
  Recommendation: /kb-lint src/search/

Distill candidates:
  docs/plans/2026-03-19-1400/plan-billing-rewrite.md — checklist ticked, no .kb/decisions/2026-03-billing-rewrite.md.
  Recommendation: /kb-distill docs/plans/2026-03-19-1400/plan-billing-rewrite.md
```

If no signals trip: report "no drift candidates. Last lint at `<timestamp>` is current."

### 5. Do NOT advance state

Do not touch `.kb/.kb-state.json`. Drift remains open until `/kb-lint` resolves it. That separation is the point of this skill.

## Discipline

- **Read-only, always.** If you're about to write to `.kb/`, stop — wrong skill.
- **Report, don't decide.** The user chooses whether to lint. Do not run `/kb-lint` automatically even on a hard flag.
- **Heuristic is policy.** If it's misfiring on the user's corpus, propose an edit to this file.

## References

- Lint strategy rationale: [docs/lint-strategy.md](../../docs/lint-strategy.md)
- Lint command: [skills/kb-lint/SKILL.md](../kb-lint/SKILL.md)
