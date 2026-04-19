# RAG vs Compiled Knowledge Tradeoffs

The choice between retrieval-augmented generation (fetching relevant chunks at query time) and pre-compiled summaries (writing distilled knowledge into a static file) shapes every knowledge-heavy agent workflow.

## The core tradeoff

`notes/tool-031-rag-vs-compiled-knowledge-trade.md` documents the first-hand tension: RAG stays fresh but adds latency and retrieval noise; compiled summaries are fast and reliable but go stale. Neither wins in all scenarios.

The note confirms that giving the model a concrete example before the real query cuts hallucinations significantly — this applies to both RAG (the retrieved chunk functions as the example) and compiled KB (the summary section functions as the example). The technique transfers regardless of approach.

`notes/paper-012-rag-vs-fine-tuning-pipelines-t.md` and its duplicate `notes/paper-034-rag-vs-fine-tuning-pipelines-t.md` provide academic grounding: the pipeline architecture (chunking strategy, embedding choice, re-ranking) matters as much as the RAG-vs-finetune decision itself.

## When to prefer RAG

RAG is preferable when the source corpus changes frequently, when exact provenance matters (the retrieved chunk is citable), or when the query set is unpredictable and broad. `notes/paper-016-retrieval-augmented-generation.md` shows RAG's advantage on knowledge-intensive NLP tasks where no static summary could cover the needed breadth.

## When to prefer compiled knowledge

Compiled summaries win when queries are predictable and few, when retrieval latency is unacceptable in the workflow, or when the corpus is stable enough that staleness is not a concern. The `.kb/` structure in this very corpus is an example of compiled knowledge: it is written once and read many times.

## Hybrid approaches

`notes/tool-017-hybrid-rag-pipelines.md` explores combining both: a compiled summary layer for orientation (cheap, fast) and retrieval for specific factual lookups (precise, fresh). See also [rag-and-knowledge domain](../../rag-and-knowledge/overview.md) for implementation patterns.

## References

- Source: `notes/tool-031-rag-vs-compiled-knowledge-trade.md`
- Papers: `notes/paper-012-rag-vs-fine-tuning-pipelines-t.md`, `notes/paper-016-retrieval-augmented-generation.md`
- Related: [rag-and-knowledge/hybrid-pipelines](../../rag-and-knowledge/hybrid-pipelines.md)
