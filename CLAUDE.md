# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Claude Code plugin — **markdown only, no build system, no test suite, no package manager**. The deliverable is a set of skills, commands, templates, and docs. "Running" this repo means installing it as a plugin and invoking its slash commands against a target corpus.

Install locally to dogfood changes:

```
/plugin marketplace add olegvg/kb-for-agents
/plugin install kb-for-agents@kb-for-agents
```

## Critical architectural invariant

**`.kb/` lives inside the user's corpus, never inside this plugin.** The plugin is stateless with respect to any specific corpus. A user must be able to copy `.kb/` between machines or check it into their own repo alongside their code. If a change to a skill or template would couple `.kb/` to this plugin's location, that change is wrong. This is non-negotiable — it's what makes the pattern survive the plugin.

## The three-layer pattern this plugin encodes

1. **Sources** — the corpus itself. Never duplicated.
2. **Summaries** (`.kb/summaries/<area>/*.md`) — prose, one topic per file, freeform size.
3. **Indexes** (`.kb/indexes/*.md`) — navigation, **≤300 tokens per file**, signposts only, no prose. Entry point `.kb/indexes/_root.md`.

Plus **decisions** (`.kb/decisions/*.md`) — distilled records from completed plans. Decisions are NOT a fourth layer: they are referenced from the summaries they affect via `## Key decisions` sections, never listed as a top-level area in `_root.md`. The agent reaches a decision by navigating indexes → summary → following a reference.

Why three layers: progressive disclosure. See [docs/concept.md](docs/concept.md).

## Repo layout

- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` — plugin and self-hosted marketplace manifests. Version bumps go here.
- `skills/<name>/SKILL.md` — each skill is a single markdown file with YAML frontmatter (`name`, `description`). The `description` field is what Claude Code matches against to auto-invoke the skill; it must include trigger phrases (English + Russian in this repo).
- `commands/<name>.md` — thin slash-command wrappers. Each one is essentially `Invoke the <name> skill with $ARGUMENTS`. Do not duplicate skill logic into the command file.
- `templates/` — starter shapes for `_root.md`, area indexes, summaries, decisions. Referenced by the skills. Users can also hand-copy them (see [templates/README.md](templates/README.md)).
- `docs/` — pattern rationale. [concept.md](docs/concept.md), [navigation-rules.md](docs/navigation-rules.md), [lint-strategy.md](docs/lint-strategy.md). These drive the skills, not the reverse — if you change a skill's behavior, check whether the corresponding doc still holds, and update the doc if not.

## The five skills and how they relate

| Skill | Mode | Writes `.kb/`? | Writes `.kb-state.json`? |
|---|---|---|---|
| `kb-ingest` | one-shot, fresh build | yes (creates) | yes (initializes) |
| `kb-query` | read-only | no | no |
| `kb-lint` | scoped, manual | yes (updates) | yes (advances `last_linted_sha`) |
| `kb-check-drift` | read-only | **no** | **no** |
| `kb-distill` | manual, post-plan | yes (adds decision + updates summaries) | no |

The `kb-check-drift` / `kb-lint` split is deliberate — drift detection is read-only and reports candidates; only `kb-lint` mutates and advances state. Never collapse them. See [docs/lint-strategy.md](docs/lint-strategy.md).

`kb-ingest` uses a strict three-pass workflow (survey → parallel subagent deep-ingest → main-agent index assembly). The main agent never reads full file bodies in passes 1 or 3 — that is the context-window guarantee of the pattern. Do not collapse the passes even on small corpora.

## When editing skills

- Preserve the YAML frontmatter shape. `name` must match the directory, `description` drives auto-invocation.
- Keep the trigger-phrase list in `description` (English + Russian). Removing triggers breaks auto-invocation for existing users.
- The **300-token index budget is a hard limit**, not a suggestion. If you relax it in a skill, update [docs/concept.md](docs/concept.md) and [docs/navigation-rules.md](docs/navigation-rules.md) too.
- The `kb-check-drift` heuristic is policy, not code — it lives as a checklist in [skills/kb-check-drift/SKILL.md](skills/kb-check-drift/SKILL.md). That's the intended extension point. Do not add config files or YAML schemas for it.

## When adding a new skill

1. Create `skills/<name>/SKILL.md` with frontmatter (`name`, `description` with trigger phrases).
2. Create `commands/<name>.md` as a thin wrapper invoking the skill with `$ARGUMENTS`.
3. Update the "What's inside" and "Quickstart" sections in [README.md](README.md).
4. If the skill represents a new pattern concept, add rationale to `docs/` — don't bury it only in the skill file.

## Verifying changes

No automated tests. Verification is by reading:
- Do the skill files still match the rationale in `docs/`?
- Do the commands still one-line-wrap the skills?
- Does the README's Quickstart still work against a throwaway corpus?

For behavior changes, dogfood against a real corpus via `/plugin install` before committing.
