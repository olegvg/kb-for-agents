# T05 — without-kb

**Question:** What do my notes collectively say about auditing legacy codebases with AI — covering tool experiments, open ideas, and what actually happened in project logs?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-009-audit-of-legacy-codebases-with-.md`
2. `examples/notes-corpus/notes/paper-018-audit-of-legacy-codebases-usin.md`
3. `examples/notes-corpus/notes/log-kb-for-agents-2026-03-12.md`
4. `examples/notes-corpus/notes/log-kb-for-agents-2026-03-22.md`
5. `examples/notes-corpus/notes/log-mcp-telegram-bot-2026-01-18.md`
6. `examples/notes-corpus/notes/log-mcp-telegram-bot-2026-02-07.md`
7. `examples/notes-corpus/notes/idea-002-what-if-audit-of-legacy-codeba.md`
8. `examples/notes-corpus/notes/idea-016-what-if-audit-of-legacy-codeba.md`

## Tool calls
- Read × 8
- Grep × 2
- Glob × 0

## Tokens read from corpus
~4200  
(grep for "audit-of-legacy" returns ~13 hits; agent reads 8 most relevant files; ~16800 bytes / 4 ≈ 4200 tokens)

## Answer

Grep for "audit-of-legacy-codebases" returns approximately 13 hits across tool, paper, log, and idea files. Reading the primary tool note (`tool-009`): AI auditing surfaced undocumented behaviors that grep missed; single-responsibility subtasks per module produced better results than full-pass requests. The paper note (`paper-018`) describes combining static analysis with LLM reasoning and provides a finding taxonomy (undocumented behavior, dead code, schema drift) worth borrowing. Multiple log files (kb-for-agents and mcp-telegram-bot) repeat the phrase "classic audit-of-legacy-codebases territory" when unexpected behaviors surface. Idea notes (`idea-002`, `idea-016`) propose an incremental re-audit triggered by diffs. Without the KB's layered structure, the agent correctly retrieves all relevant files but produces a flat list rather than the three-layer (tool experiments / open ideas / project observations) synthesis. High risk of missing the TDD follow-on pattern documented in `tool-020` and `tool-012`, which are not directly tagged with the audit keyword.
