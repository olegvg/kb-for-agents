# Lint Strategy

## Two operations, not one

The plugin separates **finding drift** from **resolving drift**:

- `/kb-check-drift` — read-only. Surfaces candidates for re-lint. Never modifies `.kb/` or `.kb-state.json`.
- `/kb-lint <path>` — write. Updates summaries and indexes affected by changes in `<path>`. Advances `.kb-state.json` to the current SHA.

Drift stays open until lint is explicitly run. The agent never silently re-lints.

## Why manual, not automated

### Against git-hook lint

Running lint on every commit:
- **Slow path** — lint takes time; pre-commit hooks that take >5 seconds get disabled by contributors.
- **Noisy path** — most commits don't materially change the KB. Re-writing unchanged summaries produces diff churn without information.
- **Wrong path** — lint needs the agent to read code carefully. A hook that greps for filenames and rewrites headers is worse than no lint.

### Against scheduled lint

Running lint on a cron:
- **Timing mismatch** — drift accumulates by commit, not by wall clock. A low-commit week runs lint for nothing; a high-commit week lets drift pile up.
- **Stale trigger** — by the time the schedule fires, the user has moved on from the code that drifted.

### For manual lint with drift surfacing

- **Cheap to check** — `/kb-check-drift` is fast (git diff + heuristic). Run it before a query when you want confidence the KB is current.
- **Explicit gate** — lint only runs when the user decides drift matters. No surprise rewrites.
- **Composable** — the user can invoke `/kb-lint <path>` for just the area they care about, not the whole corpus.

## The drift-checker heuristic

`kb-check-drift` applies the following signals to `git log --stat <last-linted-sha>..HEAD` (plus a scan of `docs/plans/**` for distill candidates):

- New files above a threshold count (default: 5) in a single area → likely new subdomain.
- File renames or moves → index references stale.
- Changes to files referenced by existing indexes → summaries likely stale.
- New top-level directory → area structure may need a new index.
- Migration / schema files → semantic shifts likely; areas touching data are suspect.
- Deleted files referenced in `.kb/` → hard flag.
- Completed plan with no matching decision record in `.kb/decisions/` → recommend `/kb-distill`. Soft flag — not every plan yields a durable decision.

The heuristic is **policy, not code**. It lives in `skills/kb-check-drift/SKILL.md` as a checklist the agent applies. Users tune it by editing that file. That's the intended extension point — no configuration knobs, no YAML schema.

## State file

`.kb-state.json` stores:

```json
{
  "last_linted_sha": "<SHA>",
  "last_linted_at": "<ISO-8601 UTC>",
  "schema_version": 1
}
```

- `/kb-check-drift` reads this but does not write it.
- Only `/kb-lint` writes it, and only after successful lint. A lint that fails halfway must not advance state.
- `schema_version` is loose intentionally — future versions may add per-area lint timestamps.
