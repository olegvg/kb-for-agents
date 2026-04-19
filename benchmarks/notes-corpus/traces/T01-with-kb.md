# T01 — with-kb

**Question:** What have I learned about using prompt caching with the Anthropic SDK — specifically what worked and what failed?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/claude-code-workflow.md`
3. `examples/notes-corpus/.kb/summaries/claude-code-workflow/cost-and-efficiency.md`

## Tool calls
- Read × 3
- Grep × 0
- Glob × 0

## Tokens read from corpus
~1118  
(_root.md 404 + claude-code-workflow index 290 + cost-and-efficiency summary 448)

## Answer

Based on the KB, prompt caching experience is documented in `notes/tool-026-prompt-caching-with-the-anthrop.md` and surfaced in the cost-and-efficiency summary. What worked: placing static prefix content (CLAUDE.md, system prompt, tool definitions) at the top of the prompt maximizes the cacheable prefix — these tokens are identical across turns and a cache hit eliminates their cost entirely. Giving the model a concrete example before asking for the real task cut hallucinations significantly. Breaking the work into single-responsibility subtasks made each invocation predictable. What failed: asking for explanations and code in the same response reliably produced worse code; mixing two unrelated concerns in one subagent call doubled review time. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Dynamic content (conversation history) cannot be cached, so the strategy is to maximize the stable prefix and keep dynamic content minimal.
