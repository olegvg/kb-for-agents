# T04 — with-kb

**Question:** Based on my reading notes and tool experiments, when should I prefer RAG over a compiled-knowledge layer, and when does the compiled approach win?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/context-management.md`
3. `examples/notes-corpus/.kb/summaries/context-management/rag-vs-compiled.md`
4. `examples/notes-corpus/.kb/indexes/rag-and-knowledge.md`
5. `examples/notes-corpus/.kb/summaries/rag-and-knowledge/hybrid-pipelines.md`

## Tool calls
- Read × 5
- Grep × 0
- Glob × 0

## Tokens read from corpus
~1870  
(_root.md 404 + context-management index 319 + rag-vs-compiled 596 + rag-and-knowledge index 314 + hybrid-pipelines 518)

## Answer

The decision framework from `notes/tool-031-rag-vs-compiled-knowledge-trade.md`, corroborated by `notes/paper-012-rag-vs-fine-tuning-pipelines-t.md` and `notes/paper-016-retrieval-augmented-generation.md`: prefer RAG when the source corpus changes frequently (weekly or more), when exact provenance matters (retrieved chunks are citable), or when queries are unpredictable and broad — RAG wins on knowledge-intensive tasks where no static summary could cover the needed breadth. Prefer compiled knowledge when queries are predictable and few, when retrieval latency is unacceptable in the workflow, or when the corpus is stable enough that staleness is not a concern — the `.kb/` structure in this very corpus is an example of compiled knowledge written once and read many times. A hybrid approach (`notes/tool-017-hybrid-rag-pipelines.md`) combines both: a compiled summary layer for orientation (cheap, fast, predictable) plus retrieval for specific factual lookups (precise, fresh). The corpus-size heuristic from `notes/ops-004-count-by-kind.md` is implicit: a small, balanced corpus (150 files, well-tagged) is well-suited to compiled summaries; a large or rapidly-growing corpus tips the balance toward RAG.
