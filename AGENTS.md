# AGENTS.md

This repository is a dual-format Claude Code and Codex plugin. Keep both plugin manifests in sync when changing plugin metadata:

- `.claude-plugin/plugin.json` for Claude Code.
- `.codex-plugin/plugin.json` for Codex marketplace packaging.
- `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` for the respective self-hosted marketplace indexes.

## Critical Architectural Invariant

`.kb/` lives inside the user's corpus, never inside this plugin. The plugin is stateless with respect to any specific corpus. A user must be able to copy `.kb/` between machines or check it into their own repo alongside their code. If a change to a skill or template would couple `.kb/` to this plugin's location, that change is wrong.

## Repo Layout

- `skills/<name>/SKILL.md` contains Codex/Claude skills. Preserve YAML frontmatter and English/Russian trigger phrases.
- `commands/<name>.md` contains Claude Code slash-command wrappers. Do not duplicate skill logic into command files.
- `templates/` contains starter shapes for `_root.md`, area indexes, summaries, decisions, and state.
- `docs/` contains pattern rationale. If skill behavior changes, update the corresponding docs.

## Verification

There is no build system or test suite. Verify changes by validating JSON manifests and reading the affected skill/docs paths for consistency.
