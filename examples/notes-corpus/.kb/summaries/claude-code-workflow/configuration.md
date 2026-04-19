# Claude Code Configuration

How to configure the Claude Code environment for a project: instruction files, custom commands, keybindings, and automated hooks.

## CLAUDE.md project instructions

`notes/tool-022-claude-md-project-instructions.md` establishes the value of CLAUDE.md: keeping it up to date with project-specific decisions "saved repeated explanatory preambles." The file functions as persistent context injected at every session start, which means it substitutes for re-stating project conventions each turn.

The key discipline: CLAUDE.md should record decisions, not documentation. "Don't use tool X for Y" is useful; a description of what the project does is not — the model can read the codebase.

## Slash commands

`notes/tool-000-claude-code-slash-commands.md` and its duplicate `notes/tool-035-claude-code-slash-commands.md` cover custom slash commands. The finding: explicit constraints in the slash command body outperformed general instructions — the same principle as in agent prompting applies here. A slash command that specifies exact steps is more reliable than one that describes a goal.

## Keybindings

`notes/tool-002-claude-code-keybindings-customi.md` documents keybinding customization. No major findings beyond confirming it works and reduces friction for frequently-used commands.

## Hook-driven automation

`notes/tool-004-hook-driven-automation-in-claud.md` and its duplicate `notes/tool-039-hook-driven-automation-in-claud.md` cover hooks that fire on events (pre-commit, post-tool-call, etc.). The pattern: hooks make side effects (linting, logging, format checks) automatic rather than optional. The cost is that hook failures can block the workflow unexpectedly — document what each hook does and what causes it to fail.

## References

- Source: `notes/tool-022-claude-md-project-instructions.md`, `notes/tool-000-claude-code-slash-commands.md`, `notes/tool-002-claude-code-keybindings-customi.md`, `notes/tool-004-hook-driven-automation-in-claud.md`
