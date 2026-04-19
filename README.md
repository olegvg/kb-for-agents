# kb-for-agents

[Русская версия](README.ru.md)

A Claude Code plugin that packages the three-layer knowledge base pattern as installable skills and slash commands. Point it at a codebase or notes archive and get the progressive-disclosure workflow described in [Knowledge Base for Agents](https://www.linkedin.com/posts/ahaidukof_karpathy-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BB-%D1%82%D0%BE-%D1%87%D1%82%D0%BE-%D0%BC%D1%8B-%D0%BD%D0%B0%D1%89%D1%83%D0%BF%D0%B0%D0%BB%D0%B8-activity-7446836637143130112-o920/).

## What's inside

- **Skills** — `kb-ingest`, `kb-query`, `kb-lint`, `kb-check-drift`, `kb-distill`. The pattern codified.
- **Commands** — `/kb-ingest`, `/kb-query`, `/kb-lint`, `/kb-check-drift`, `/kb-distill`. Thin wrappers over the skills.
- **Templates** — starter shapes for indexes, summaries, decisions, `_root.md`, state. See [templates/README.md](templates/README.md) for manual-build steps.
- **Docs** — pattern rationale: [concept](docs/concept.md), [navigation rules](docs/navigation-rules.md), [lint strategy](docs/lint-strategy.md).

## Install

```
/plugin marketplace add olegvg/kb-for-agents
/plugin install kb-for-agents@kb-for-agents
```

## Quickstart

In any Claude Code session opened at your corpus root:

```
/kb-ingest .
/kb-query where are fees charged?
```

After you've made changes to the corpus:

```
/kb-check-drift
/kb-lint src/billing/
```

When a planned piece of work ships and you want its key choices preserved:

```
/kb-distill docs/plans/2026-03-19-1400/plan-billing-rewrite.md
```

## How it works

The plugin builds a `.kb/` directory **inside your corpus** (not inside the plugin). It has three layers plus a decisions store:

1. **Sources** — your corpus itself. Not duplicated.
2. **Summaries** (`.kb/summaries/<area>/*.md`) — prose per topic, one file each.
3. **Indexes** (`.kb/indexes/*.md`) — navigation, ≤300 tokens per file. Entry point is `.kb/indexes/_root.md`.

Alongside: **Decisions** (`.kb/decisions/*.md`) — distilled records extracted from completed plans. Referenced from the summaries they affect via `## Key decisions` sections, not surfaced as a separate top-level area.

The agent reads indexes first on any query, then descends. If the question is "how does X work, and why was it built that way?", the navigation lands on a summary and follows its decision references. Context stays bounded; navigation is observable in traces.

See [docs/concept.md](docs/concept.md) for the full argument.

## What this is

A starter kit: skills, commands, templates, conceptual docs. Patterns codified so you can apply them without re-reading the article.

## What this is not

A runnable benchmark, a bundled example corpus, a RAG library, or a general-purpose agent framework. Proof of effectiveness lives in the surrounding article and posts, not in this repo.

## Requirements

- Claude Code.
- A corpus you want to document. A git-backed corpus is strongly recommended — `/kb-lint` and `/kb-check-drift` both depend on git history.

## License

MIT. See [LICENSE](LICENSE).
