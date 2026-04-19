# MCP Server Setup and Configuration

How to set up and connect MCP servers to a Claude agent environment.

## Setup experience

`notes/tool-008-mcp-server-setup-and-configurat.md` and its duplicate `notes/tool-043-mcp-server-setup-and-configurat.md` document the MCP server setup process. The finding: logging every agent turn to a file was essential for diagnosing configuration issues — the exact failure step was only visible in the logs. Keeping CLAUDE.md up to date with project-specific MCP configuration decisions saved repeated re-explanation.

The setup cost is real ("the setup cost is real, but it pays back on the third use"). The break-even point is roughly three uses of the same MCP server in a session.

## Connection and auth

The note confirms that explicit constraints in the MCP server configuration (what endpoints are available, what auth is required) outperformed leaving the agent to discover capabilities dynamically. Providing a bounded capability description upfront avoids the model wasting calls probing for what's available.

## From the mcp-telegram-bot project

Project logs for `mcp-telegram-bot` (`notes/log-mcp-telegram-bot-2026-01-16.md` through `notes/log-mcp-telegram-bot-2026-04-09.md`) document a production MCP server build. The recurring pattern: undocumented behaviors in the MCP protocol itself surface as unexpected responses that the agent cannot automatically recover from. Document these in CLAUDE.md as "known quirks."

## References

- Source: `notes/tool-008-mcp-server-setup-and-configurat.md`
- Project logs: `notes/log-mcp-telegram-bot-2026-01-16.md` through `notes/log-mcp-telegram-bot-2026-04-09.md`
- Related: [claude-code-workflow/plugins-and-extensions](../../claude-code-workflow/plugins-and-extensions.md)
