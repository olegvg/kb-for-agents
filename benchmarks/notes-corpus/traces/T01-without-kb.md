# T01 — without-kb

**Question:** What have I learned about using prompt caching with the Anthropic SDK — specifically what worked and what failed?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-026-prompt-caching-with-the-anthrop.md`
2. `examples/notes-corpus/notes/tool-024-multi-turn-conversation-design.md`

## Tool calls
- Read × 2
- Grep × 1
- Glob × 0

## Tokens read from corpus
~460  
(tool-026 1027 bytes / 4 ≈ 257 tokens + tool-024 809 bytes / 4 ≈ 202 tokens)

## Answer

Grep for "prompt caching" across `notes/` returns two matches: `tool-026-prompt-caching-with-the-anthrop.md` (2 hits — the primary source) and `tool-024-multi-turn-conversation-design.md` (1 hit — passing mention). Reading tool-026 directly: what worked — giving the model a concrete example before asking for the real thing cut hallucinations significantly; breaking tasks into single-responsibility subtasks made each invocation predictable; explicit constraints outperformed general instructions; iteration speed improved once second-guessing stopped. What did not work: asking for explanations and code in the same response produced worse code; mixing unrelated concerns in one subagent call muddied output and doubled review time; ignoring context-window limits caused silent truncation that was hard to diagnose. The multi-turn note (tool-024) adds no additional caching-specific content. This grep path finds the answer correctly but requires reading the full raw note rather than a pre-digested summary.
