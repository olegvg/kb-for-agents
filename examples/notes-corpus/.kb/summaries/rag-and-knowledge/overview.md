# RAG and Knowledge Retrieval — Overview

This domain covers the implementation side of retrieval-augmented generation: embeddings, vector search, hybrid pipelines, knowledge graph construction, and codebase summarization for agent use.

Where [context-management](../context-management/overview.md) covers the architectural decision (RAG vs compiled), this domain covers the engineering of retrieval itself: how to embed, index, query, and post-process retrieved content.

## Leaves in this domain

- **[embeddings-and-search](embeddings-and-search.md)** — embedding strategies, semantic search implementation, HyDE and FLARE techniques.
- **[hybrid-pipelines](hybrid-pipelines.md)** — combining dense retrieval with BM25, re-ranking, and structured knowledge.
- **[codebase-summarization](codebase-summarization.md)** — summarizing codebases and note corpora for agent navigation.

## References

- Tool notes: `notes/tool-006-embeddings-for-knowledge-retrie.md`, `notes/tool-028-semantic-search-over-notes-corp.md`, `notes/tool-017-hybrid-rag-pipelines.md`, `notes/tool-025-knowledge-graph-construction-wi.md`, `notes/tool-030-codebase-summarisation-for-agen.md`
- Papers: `notes/paper-002-flare-active-retrieval-augment.md`, `notes/paper-006-hyde-hypothetical-document-emb.md`, `notes/paper-016-retrieval-augmented-generation.md`, `notes/paper-012-rag-vs-fine-tuning-pipelines-t.md`
