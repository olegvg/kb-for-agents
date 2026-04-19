# T06 — without-kb

**Question:** Based on the project logs, why did the team stop relying on single, large prompts and shift toward breaking agent tasks into smaller subtasks?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-008-mcp-server-setup-and-configurat.md`
2. `examples/notes-corpus/notes/tool-043-mcp-server-setup-and-configurat.md`
3. `examples/notes-corpus/notes/tool-009-audit-of-legacy-codebases-with-.md`
4. `examples/notes-corpus/notes/tool-019-cost-management-for-long-agent-.md`
5. `examples/notes-corpus/notes/log-kb-for-agents-2025-11-09.md`
6. `examples/notes-corpus/notes/log-kb-for-agents-2026-04-12.md`

## Tool calls
- Read × 6
- Grep × 2
- Glob × 0

## Tokens read from corpus
~2200  
(grep for "single prompt" returns hits in tool notes; grep for "subtask" returns ~15 hits across tool and log files; agent reads 6 files at ~900 bytes avg ≈ 2200 tokens)

## Answer

Grep for "single prompt" hits `tool-008` which contains the key phrase: "asking for too much in a single prompt consistently led to shallow, generic output." Grep for "subtask" returns many hits across tool and log files, but the log files do not directly state a decision — they record observations. Reading the log files: `log-kb-for-agents-2025-11-09.md` records "discovered that the bottleneck was context-window-management rather than model capability," which is the turning-point reframe. `tool-019` adds that "asking for too much in a single prompt led to shallow output that required a follow-up turn — doubling the cost." Without KB summaries, the agent finds these signals but must connect them manually across multiple raw notes. Risk: the agent focuses on the tool notes' "what didn't work" section and misses the log-based evidence of the implicit decision, or reads only a subset of logs and misses the pattern's recurrence. The answer is reconstructable but requires more reading and risks being less structured than the KB path.
