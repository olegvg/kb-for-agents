# T02 — without-kb

**Question:** What pitfalls should I watch out for when setting up and configuring an MCP server based on my notes?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-008-mcp-server-setup-and-configurat.md`
2. `examples/notes-corpus/notes/tool-043-mcp-server-setup-and-configurat.md`

## Tool calls
- Read × 2
- Grep × 1
- Glob × 0

## Tokens read from corpus
~514  
(tool-008 920 bytes / 4 ≈ 230 + tool-043 1134 bytes / 4 ≈ 284)

## Answer

Grep for "mcp server" across `notes/` returns two direct matches: `tool-008-mcp-server-setup-and-configurat.md` and `tool-043-mcp-server-setup-and-configurat.md` (a duplicate). Reading both: pitfalls from the "what didn't" sections are — mixing two unrelated concerns in one subagent call muddies output and doubles review time; over-relying on the model's memory of earlier turns produces subtle inconsistencies by step four or five; asking for too much in a single prompt consistently leads to shallow, generic output. Positive countermeasures (what worked): logging every agent turn to a file to spot the exact failure step; keeping CLAUDE.md up to date with project-specific MCP configuration decisions; using explicit constraints rather than general instructions. The setup cost is real but pays back on the third use. Without the KB summary, the agent gets the same answer but must manually parse raw note text rather than reading structured prose — adequate for two files, but would degrade quickly with more hits.
