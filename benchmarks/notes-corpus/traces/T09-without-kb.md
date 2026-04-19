# T09 — without-kb

**Question:** Based on everything in my notes, what's the single most consistently recommended technique for reducing hallucinations when using LLM agents?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-026-prompt-caching-with-the-anthrop.md`
2. `examples/notes-corpus/notes/tool-036-prompt-injection-defence-patter.md`
3. `examples/notes-corpus/notes/tool-021-structured-output-extraction.md`
4. `examples/notes-corpus/notes/tool-039-hook-driven-automation-in-claud.md`
5. `examples/notes-corpus/notes/tool-009-audit-of-legacy-codebases-with-.md`
6. `examples/notes-corpus/notes/tool-007-tool-use-json-schema-design.md`
7. `examples/notes-corpus/notes/tool-005-few-shot-example-selection-stra.md`

## Tool calls
- Read × 7
- Grep × 2
- Glob × 0

## Tokens read from corpus
~4900  
(grep for "hallucin" returns ~15 hits across 150 files; agent reads 7 files; ~19600 bytes / 4 ≈ 4900 tokens)

## Answer

Grep for "hallucin" returns approximately 15 matches scattered across tool, ops, and log notes. Reading the hits: the phrase "giving the model a concrete example before asking for the real thing cut hallucinations significantly" appears in multiple tool notes including `tool-026`, `tool-005`, and `tool-007`. Without the KB's cross-note synthesis, the agent must manually identify this as the convergent pattern — possible but requiring careful reading of all 15 matching files. The risk without the KB is anchoring on the first match (which could be `tool-036` on prompt injection defense, a different anti-hallucination technique) rather than the consensus. A well-executed without-KB pass would read enough notes to recognize the few-shot pattern's recurrence, but would take 7+ file reads versus 6 for the KB path, and risks a less confident single-answer synthesis. Chain-of-thought and self-consistency from paper notes are less likely to be surfaced since grep for "hallucin" does not reliably hit the paper notes that use "error reduction" rather than "hallucination."
