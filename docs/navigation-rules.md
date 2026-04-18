# Navigation Rules

## Cold-start rule: indexes-first

On the first access to the KB in a given task or query, the agent MUST read `.kb/indexes/_root.md` before reading anything else in `.kb/`.

This is enforced in the `kb-query` skill and observable in traces: every first-touch on a summary file should be preceded by reads on `_root.md` plus one or more area indexes.

## Warm-reference relaxation

Once the agent is working inside a summary (Layer 2), it may follow direct references to other summaries **or to decision records in `.kb/decisions/`** without returning to the index level.

Examples:
- Reading `summaries/auth/session.md` and finding a link to `summaries/billing/refunds.md` — the agent may jump straight there.
- Reading `summaries/billing/fee-calculation.md` and finding a `## Key decisions` section linking to `decisions/2026-03-fee-calculation-rewrite.md` — the agent may follow the link directly.

This relaxation is intentional. Strict indexes-only navigation would require the agent to re-enter through `_root.md` for every related concept — expensive and pedantic. The indexes earn their keep on cold start; once warm, references between summaries (and from summaries into decisions) are cheap.

This is how the query "how does X work now, and why was it built that way?" resolves: indexes → area index → summary for X → decision records linked from the summary. Current state and historical rationale along one navigation path.

## What the rules buy

- **Predictable context usage** — the upper bound on a cold-start query is `_root.md` + 1–3 area indexes (each ≤300 tokens) + a bounded number of summaries.
- **Debuggable navigation** — if the agent answers wrong, the trace shows whether it entered through `_root.md`, which areas it picked, which summaries it read. Fixing a bad answer often means fixing an index, not a summary.
- **Portable discipline** — the rules are stated, not implied. A new contributor can follow them without re-reading the full article.

## Anti-patterns

- **Dumping the whole `.kb/`** as initial context — defeats the point.
- **Skipping `_root.md` because "I know this corpus"** — the agent doesn't. Write for the agent.
- **Putting prose content in indexes** — indexes are signposts. If you catch yourself writing prose in an index file, it belongs in a summary.
