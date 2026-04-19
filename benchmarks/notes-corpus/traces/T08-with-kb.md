# T08 — with-kb

**Question:** Have I written anything about designing APIs with GraphQL or gRPC?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/mcp-and-tools.md`
3. `examples/notes-corpus/.kb/summaries/mcp-and-tools/tool-design.md`

## Tool calls
- Read × 3
- Grep × 0
- Glob × 0

## Tokens read from corpus
~1200  
(_root.md 404 + mcp-and-tools index 296 + tool-design summary ~500)

## Answer

No. The KB contains no notes about GraphQL or gRPC API design. The `mcp-and-tools` area is the closest domain — it covers tool JSON schema design for LLM tool calls (the `tool-design` leaf covers JSON schema for tool definitions, few-shot selection, and structured output extraction). This is explicitly distinct from API query languages: tool-call JSON schemas define the interface between an LLM and a callable function, not a client-server query API. GraphQL and gRPC do not appear in any area index or leaf summary. The KB correctly surfaces the distinction between tool-call JSON schemas and API design languages — if the user is asking about designing a machine-readable interface for an LLM tool, `tool-design` is relevant; if they are asking about GraphQL or gRPC, those topics are absent from the corpus.
