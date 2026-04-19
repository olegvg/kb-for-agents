# T03 — without-kb

**Question:** Across all my notes — tool reflections, paper readings, and open ideas — what is the recurring theme around context-window management, and is there consensus on how to handle it automatically?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-029-context-window-management-strat.md`
2. `examples/notes-corpus/notes/tool-064-context-window-management-strat.md` (if present, duplicate)
3. `examples/notes-corpus/notes/paper-031-long-context-language-models-a.md`
4. `examples/notes-corpus/notes/tool-026-prompt-caching-with-the-anthrop.md`
5. `examples/notes-corpus/notes/tool-019-cost-management-for-long-agent-.md`
6. `examples/notes-corpus/notes/tool-033-agent-loop-design-patterns.md`

## Tool calls
- Read × 6
- Grep × 2
- Glob × 0

## Tokens read from corpus
~2800  
(grep returns ~20 hits across 150 files; agent reads 6 most directly relevant files; ~11200 bytes / 4)

## Answer

Grep for "context-window" and "context-window-management" returns approximately 20 hits spanning tool, paper, log, and ops notes. Reading the primary tool note (`tool-029-context-window-management-strat.md`): the recurring theme is that ignoring context limits causes silent truncation that is hard to diagnose — the failure leaves no error signal. The paper note (`paper-031-long-context-language-models-a.md`) adds the theoretical basis: long-context models attend less reliably to middle-window content. Practical consensus on mitigation: single-responsibility subtasks, explicit state re-injection each turn, treating tool calls as unit tests. No consensus on automatic management — the scattered idea notes suggest proposals (freshness scoring, confidence tags) but nothing tested. An agent without the KB would read each file individually and struggle to distinguish the convergent practical finding from the open-hypothesis idea notes without the KB's "open-questions" summary framing the distinction explicitly. Risk: the agent anchors on the first 2–3 tool notes and underweights the unresolved-ness signaled by the idea notes.
