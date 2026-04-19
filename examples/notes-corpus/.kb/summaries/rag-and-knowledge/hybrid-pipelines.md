# Hybrid RAG Pipelines

Combining dense vector retrieval with other retrieval signals for higher precision.

## What hybrid means in practice

`notes/tool-017-hybrid-rag-pipelines.md` documents hybrid RAG: combining dense embedding retrieval with sparse BM25 (keyword) retrieval, then re-ranking the merged result set. The practical motivation: pure dense retrieval misses exact-match queries (specific function names, error codes); pure BM25 misses semantic queries (paraphrases, synonyms). Hybrid covers both.

The note confirms that explicit constraints on the retrieval query (providing a concrete, specific question rather than a vague topic) improve precision in both retrieval modes. This is the retrieval-side version of the general "explicit constraints outperform general instructions" finding.

## Knowledge graph construction

`notes/tool-025-knowledge-graph-construction-wi.md` explores a more structured form of hybrid retrieval: building a knowledge graph from the corpus, then querying it alongside vector retrieval. The approach extracts entities and relations from notes and indexes them separately from the dense embedding. The finding: useful for corpora with strong relational structure (who worked with what, which tools are used for which tasks), less useful for loosely-coupled notes.

## RAG vs fine-tuning

`notes/paper-012-rag-vs-fine-tuning-pipelines-t.md` and `notes/paper-034-rag-vs-fine-tuning-pipelines-t.md` provide the benchmark comparison. The headline finding: RAG dominates fine-tuning when the knowledge base changes frequently; fine-tuning wins on tasks requiring parametric internalization of a stable fact set. For a personal notes corpus that grows weekly, RAG is the natural choice.

## References

- Source: `notes/tool-017-hybrid-rag-pipelines.md`, `notes/tool-025-knowledge-graph-construction-wi.md`
- Papers: `notes/paper-012-rag-vs-fine-tuning-pipelines-t.md`
- Related: [embeddings-and-search](embeddings-and-search.md), [context-management/rag-vs-compiled](../../context-management/rag-vs-compiled.md)
