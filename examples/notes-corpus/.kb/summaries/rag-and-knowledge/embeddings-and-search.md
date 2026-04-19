# Embeddings and Semantic Search

How to build embedding-based retrieval for a notes corpus or codebase.

## Embedding strategies in practice

`notes/tool-006-embeddings-for-knowledge-retrie.md` documents the first practical use of embeddings for knowledge retrieval. The note confirms that explicit constraints in the query (providing a concrete example before the query) cut hallucination-like retrieval errors significantly — the embedding model's sense of relevance aligns better when the query is specific rather than abstract.

`notes/tool-028-semantic-search-over-notes-corp.md` specifically addresses semantic search over a notes corpus like this one. The key finding: chunking at note boundaries (one embedding per note) outperforms sub-note chunking for this kind of short, atomic note format. The note itself is already the right granularity.

## Advanced retrieval: HyDE and FLARE

`notes/paper-006-hyde-hypothetical-document-emb.md` (HyDE) introduces an approach where the model generates a hypothetical document matching the query, then retrieves based on that hypothetical rather than the raw query. This is useful when queries are short and underspecified — the hypothetical expands them into retrieval space.

`notes/paper-002-flare-active-retrieval-augment.md` (FLARE) covers active retrieval: the model decides when to retrieve rather than retrieving at every step. The practical implication for a notes-corpus agent: retrieval on every turn is wasteful; triggering retrieval only when the model signals uncertainty is more efficient.

## References

- Source: `notes/tool-006-embeddings-for-knowledge-retrie.md`, `notes/tool-028-semantic-search-over-notes-corp.md`
- Papers: `notes/paper-006-hyde-hypothetical-document-emb.md`, `notes/paper-002-flare-active-retrieval-augment.md`, `notes/paper-016-retrieval-augmented-generation.md`
- Related: [hybrid-pipelines](hybrid-pipelines.md)
