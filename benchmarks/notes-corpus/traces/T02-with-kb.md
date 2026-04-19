# T02 — with-kb

**Question:** What pitfalls should I watch out for when setting up and configuring an MCP server based on my notes?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/mcp-and-tools.md`
3. `examples/notes-corpus/.kb/summaries/mcp-and-tools/mcp-setup.md`

## Tool calls
- Read × 3
- Grep × 0
- Glob × 0

## Tokens read from corpus
~1100  
(_root.md 404 + mcp-and-tools index 296 + mcp-setup summary 443)

## Answer

The KB surfaces pitfalls from `notes/tool-008-mcp-server-setup-and-configurat.md` and the mcp-telegram-bot project logs. Key pitfalls to watch: (1) Skipping structured logging — without logging every agent turn to a file, the exact step where configuration fails is invisible from the final output alone; (2) Leaving the capability description open-ended — allowing the agent to discover capabilities dynamically wastes calls and produces unfocused results; explicit constraints on what endpoints and auth are required must be provided upfront; (3) Underestimating setup cost — the MCP setup cost is real, but amortizes by the third use in a session; (4) Not documenting known protocol quirks in CLAUDE.md — undocumented MCP behaviors surface as unexpected responses the agent cannot automatically recover from; recording these as "known quirks" prevents repeated debugging; (5) Mixing two concerns in one subagent call — reliably muddies output and doubles review time. The break-even for investing in setup is approximately three uses of the same MCP server in a session.
