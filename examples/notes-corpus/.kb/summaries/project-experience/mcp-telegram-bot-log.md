# mcp-telegram-bot Project Log

Session notes from building a production Telegram bot backed by an MCP server.

## Project nature

Eight log entries spanning `2026-01-16` through `2026-04-09`. The mcp-telegram-bot project is distinct from kb-for-agents: it is a production-facing service (real users, real messages) rather than a developer tooling project.

## Key patterns

**Unexpected protocol behaviors.** Multiple logs record discovering undocumented behaviors in the MCP protocol or the Telegram API — the same "legacy audit" pattern that appears in kb-for-agents, but here in an external dependency rather than owned code. The remediation was the same: document findings in CLAUDE.md as known quirks.

**Agent reliability in production.** The `2026-04-09` log: "I leaned on the agent more than planned and it held up, which was a pleasant surprise." This is evidence that agent-assisted development transfers from toy projects to production contexts — but "more than planned" suggests the project scope grew.

**Wrong assumption, not a code bug.** Twice across the logs, the blocking issue turned out to be "a wrong assumption about the data shape, not a code bug." This is a pattern worth flagging: when a bug is hard to find, the hypothesis should be "my mental model of the data shape is wrong" before "there is a bug in the code."

## Connection to MCP domain

The practical insights from this project feed into [mcp-and-tools/mcp-setup](../../mcp-and-tools/mcp-setup.md) — particularly the "known quirks" pattern and the value of logging every turn.

## References

- Source: `notes/log-mcp-telegram-bot-2026-01-16.md`, `notes/log-mcp-telegram-bot-2026-01-18.md`, `notes/log-mcp-telegram-bot-2026-01-25.md`, `notes/log-mcp-telegram-bot-2026-02-03.md`, `notes/log-mcp-telegram-bot-2026-02-04.md`, `notes/log-mcp-telegram-bot-2026-02-07.md`, `notes/log-mcp-telegram-bot-2026-02-21.md`, `notes/log-mcp-telegram-bot-2026-04-09.md`
