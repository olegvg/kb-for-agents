# T09 — with-kb

**Question:** Based on everything in my notes, what's the single most consistently recommended technique for reducing hallucinations when using LLM agents?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/mcp-and-tools.md`
3. `examples/notes-corpus/.kb/summaries/mcp-and-tools/tool-design.md`
4. `examples/notes-corpus/.kb/indexes/agent-patterns.md`
5. `examples/notes-corpus/.kb/summaries/agent-patterns/self-evaluation.md`
6. `examples/notes-corpus/.kb/summaries/agent-patterns/agent-loop-design.md`

## Tool calls
- Read × 6
- Grep × 0
- Glob × 0

## Tokens read from corpus
~2540  
(_root.md 404 + mcp-and-tools index 296 + tool-design summary 622 + agent-patterns index 339 + self-evaluation 561 + agent-loop-design 562)

## Answer

The single most consistently recommended technique is: give the model a concrete example before asking for the real thing (few-shot exemplar). This pattern appears independently across multiple note types: `notes/tool-005-few-shot-example-selection-stra.md` documents it as cutting hallucinations significantly in tool-use contexts; `notes/tool-026-prompt-caching-with-the-anthrop.md` confirms the same finding in prompt caching experiments; `notes/tool-007-tool-use-json-schema-design.md` applies it to schema design (a demonstrated call shape reduces misuse). The technique functions as an implicit schema validation — the model matches its output against the demonstrated shape rather than generating unconstrained. Secondary corroboration from paper notes: `notes/paper-000-chain-of-thought-prompting-eli.md` shows that reasoning step-by-step before answering reduces errors; `notes/paper-011-self-consistency-improves-chai.md` shows that generating multiple reasoning chains and taking the majority answer reduces errors further. These are complementary, not competing — the consensus answer is "concrete example first, with chain-of-thought reasoning as a secondary technique." The few-shot exemplar pattern appears in more notes than any other single technique.
