# T06 — with-kb

**Question:** Based on the project logs, why did the team stop relying on single, large prompts and shift toward breaking agent tasks into smaller subtasks?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/project-experience.md`
3. `examples/notes-corpus/.kb/summaries/project-experience/kb-for-agents-log.md`
4. `examples/notes-corpus/.kb/summaries/project-experience/mcp-telegram-bot-log.md`
5. `examples/notes-corpus/.kb/indexes/agent-patterns.md`
6. `examples/notes-corpus/.kb/summaries/agent-patterns/agent-loop-design.md`

## Tool calls
- Read × 6
- Grep × 0
- Glob × 0

## Tokens read from corpus
~2380  
(_root.md 404 + project-experience index 321 + kb-for-agents-log 554 + mcp-telegram-bot-log 486 + agent-patterns index 339 + agent-loop-design 562)

## Answer

The KB reconstructs a causal chain across log summaries and tool notes. The logs do not record a single explicit decision, but the evidence converges: (1) The tool note `notes/tool-008-mcp-server-setup-and-configurat.md` documents the direct failure mode — "asking for too much in a single prompt consistently led to shallow, generic output." This is the proximate cause: single large prompts produced quality-degraded results requiring follow-up turns, doubling the effective cost. (2) The kb-for-agents log summary records the reframe: "the bottleneck was context-window-management rather than model capability" — once the team recognized context runaway (not model intelligence) as the constraint, subtask decomposition became the obvious structural response. (3) The agent-loop-design summary formalizes this: single-responsibility subtasks make each invocation's output verifiable on its own; mixing concerns produces output that partially satisfies both goals and fully satisfies neither. (4) The cost management note (`tool-019`) adds: "asking for too much in a single prompt led to shallow output that required a follow-up turn — doubling the cost of that step." The shift was driven by both quality degradation and cost doubling in single-prompt approaches.
