# T04 — without-kb

**Question:** Based on my reading notes and tool experiments, when should I prefer RAG over a compiled-knowledge layer, and when does the compiled approach win?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/tool-031-rag-vs-compiled-knowledge-trade.md`
2. `examples/notes-corpus/notes/paper-012-rag-vs-fine-tuning-pipelines-t.md`
3. `examples/notes-corpus/notes/idea-014-i-keep-wondering-whether-compi.md`
4. `examples/notes-corpus/notes/idea-004-there-might-be-a-simpler-bound.md`

## Tool calls
- Read × 4
- Grep × 2
- Glob × 0

## Tokens read from corpus
~2100  
(grep for "rag-vs-compiled" returns 2 direct hits; grep for "RAG" returns ~10+ hits; agent reads 4 most relevant files at ~850 bytes avg ≈ 2100 tokens total)

## Answer

Grep for "rag-vs-compiled" returns `tool-031-rag-vs-compiled-knowledge-trade.md` and a handful of idea notes with "compiled knowledge" mentions. Reading `tool-031`: RAG wins on freshness and provenance; compiled knowledge wins on latency and query predictability. Paper note `paper-012` adds academic grounding: chunking strategy and embedding choice matter as much as the RAG-vs-compiled decision itself; RAG dominates when knowledge changes frequently. The idea notes raise the staleness question without resolving it. An agent without the KB would likely anchor on the two exact-match files (`tool-031` and `paper-012`) and produce a correct but narrower answer — missing the corpus-size heuristic from ops notes and the hybrid-pipeline synthesis from `tool-017-hybrid-rag-pipelines.md`. The answer is adequate but incomplete compared to the KB path, which surfaces the hybrid option and the compiled-KB-as-example framing from the rag-vs-compiled summary.
