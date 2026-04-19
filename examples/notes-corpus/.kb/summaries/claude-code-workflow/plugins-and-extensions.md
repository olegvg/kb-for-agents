# Plugin Authoring for Claude Code

How to build, package, and distribute plugins (skills) for Claude Code.

## Plugin structure and authoring

`notes/tool-018-plugin-authoring-for-claude-cod.md` documents the authoring experience. The note confirms that explicit constraints in the plugin prompt body outperform general instructions — plugin skills should specify exactly what they do and do not do, including failure conditions.

A plugin that specifies a bounded tool list produces more reliable behavior than one that lets the model choose tools freely. The plugin boundary is also a context boundary: a well-designed plugin holds its own context and returns a compact brief, enabling the parent agent to stay within its own budget.

## MCP integration

MCP servers can be exposed as plugin tools. `notes/tool-018` touches on this interface but the primary MCP coverage is in the [mcp-and-tools domain](../../mcp-and-tools/overview.md). From the Claude Code workflow perspective: MCP tools appear in the tool list and can be invoked inside plugin skill bodies. The same bounded-tool-list principle applies.

## Extended thinking mode

`notes/tool-027-extended-thinking-mode-usage.md` covers extended thinking, which is relevant to plugin design: skills that need deep reasoning can invoke extended thinking mode explicitly, but the cost is a larger context footprint. Recommended only for planning-phase plugins, not for every-turn execution plugins.

## References

- Source: `notes/tool-018-plugin-authoring-for-claude-cod.md`, `notes/tool-027-extended-thinking-mode-usage.md`
- Related: [mcp-and-tools/mcp-setup](../../mcp-and-tools/mcp-setup.md)
