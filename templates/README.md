# Templates — Manual Build

If you want to build `.kb/` by hand instead of running `/kb-ingest`, copy from here.

## Minimum viable layout

```
<your-corpus>/.kb/
├── indexes/
│   └── _root.md
├── summaries/
├── decisions/           ← populated by /kb-distill, not by hand
└── .kb-state.json
```

## Steps

1. Copy `_root.template.md` to `.kb/indexes/_root.md`. Replace the placeholder areas with the real areas in your corpus.
2. For each area: copy `index.template.md` to `.kb/indexes/<area>.md`. Fill in the "when to enter" and leaves.
3. For each leaf: copy `summary.template.md` to `.kb/summaries/<area>/<leaf>.md`. Write the prose.
4. Create an empty `.kb/decisions/` directory. Decision records land here when you run `/kb-distill` against a completed plan. You can also hand-author them using `decision.template.md`, but the skill is the expected path.
5. Copy `.kb-state.template.json` to `.kb/.kb-state.json`. Set `last_linted_sha` to your current git SHA: `git rev-parse HEAD`. Set `last_linted_at` to the current UTC ISO-8601 timestamp.

## Rules

- Index files are ≤300 tokens. Signposts, not content.
- Summary files: one topic per file. No size limit, but split if you're mixing unrelated concerns.
- `_root.md` is the agent's first read on any query. Keep it honest — if an area disappears, remove it from `_root.md`.
- `decisions/` is never referenced from `_root.md`. Decision records are discovered via `## Key decisions` sections inside summaries that they affect.
