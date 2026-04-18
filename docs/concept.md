# The Three-Layer Knowledge Base Pattern

This plugin encodes a pattern for giving an agent navigable knowledge of a corpus (codebase, notes archive, docs folder) without blowing its context window.

## The layers

1. **Sources (Layer 1)** — the corpus itself. Code, notes, whatever the agent needs to reason about. Never duplicated inside `.kb/`.
2. **Summaries (Layer 2)** — prose explanations, one topic per file. Freeform size. Optional Mermaid diagrams. Live under `.kb/summaries/<area>/`.
3. **Indexes (Layer 3)** — navigation. Maximum 300 tokens per file. Signposts only, no prose content. Live under `.kb/indexes/`. Entry point is `.kb/indexes/_root.md`.

Alongside the three layers is a **decisions** store — distilled records extracted from completed plans, living under `.kb/decisions/`. Decisions are not a fourth layer: they are referenced from the summaries they affect via a `## Key decisions` section, not surfaced as a top-level area in `_root.md`. The agent finds them by navigating normally (indexes → summary) and following the reference.

## Why three layers

The agent has a finite context window. Naively dumping the corpus blows it. Naively dumping summaries still blows it on any corpus worth documenting. Naively dumping indexes is cheap but fails when the answer requires detail.

Three layers deliver progressive disclosure: the agent reads the map first (indexes), picks the right neighborhood (an area index), then descends to the relevant prose (summaries), and only opens sources if the summary points there. Context stays bounded.

## Why indexes-first

A cold-start agent doesn't know your corpus. If it starts by reading summaries, it reads wrong ones — expensive and slow. `_root.md` costs ≤300 tokens and orients correctly in one hop.

Once the agent is inside a summary and sees a reference to a related summary, it may follow the link without returning to the index level. See [navigation-rules.md](navigation-rules.md).

## Why semantic grouping

Auto-doc tools group by directory. That fails because agents receive questions by task surface, not by filesystem layout. "Where are fees charged?" crosses three directories. The ingest skill groups summaries by **what a user would ask about them**, not by where the files sit on disk.

## Why manual lint

Automatic doc regeneration on every commit produces two failure modes: stale docs (if lint is slow) and irrelevant churn (if lint is eager). Manual, trigger-based lint with a separate read-only drift-checker gives the user explicit control. See [lint-strategy.md](lint-strategy.md).

## Why plans are excluded but decisions are included

Plans (`docs/plans/**` and similar timestamped journals) are operational artifacts: steps, drafts, abandoned branches, debate about alternatives. 90% of a plan's content is noise to anyone who didn't execute it. Ingesting plans into the KB produces muddled summaries that mix current state with historical intent.

But a completed plan contains something that *is* durable knowledge: the decision made and its rationale. `/kb-distill` extracts that 10% — decision, context, rejected alternatives, consequences — into a standalone record in `.kb/decisions/`. Plans stay in `docs/plans/` as a journal; decisions move into the KB as knowledge.

The query "how does X work now, and based on what decisions?" resolves via a single navigation: agent enters via `_root.md`, picks the relevant area index, reads the summary for X, follows the references from the summary's `## Key decisions` section into the decision records. No separate "decisions" area to ambiguate routing — the decision is always reached through the thing it affects.

## The `.kb/` directory lives in the corpus, not in this plugin

Portability claim: a user should be able to copy `.kb/` between machines, check it into git with the code, version it alongside the sources. The plugin is stateless with respect to any specific corpus. This is non-negotiable — it's why the pattern survives the plugin.
