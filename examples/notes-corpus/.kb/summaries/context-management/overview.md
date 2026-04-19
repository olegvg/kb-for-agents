# Context Management — Overview

This domain covers everything related to managing information within an LLM's context window: strategies for staying within limits, the tradeoff between retrieval-at-runtime (RAG) versus pre-compiled summaries, and open research questions about knowledge freshness and staleness.

The corpus contains practical tool notes from direct experimentation (`tool-029`, `tool-031`), academic paper readings on long-context models and RAG (`paper-009`, `paper-016`, `paper-002`), and open-ended idea notes exploring unresolved questions (`idea-000`, `idea-001`, `idea-004`, `idea-005`).

The central tension in this domain: context windows are finite but growing; retrieval is flexible but slow; compiled summaries are fast but stale. No single answer fits all workloads — the notes record first-hand attempts to find the boundary.

## Leaves in this domain

- **[context-window-strategies](context-window-strategies.md)** — practical techniques for staying within limits during long agent sessions.
- **[rag-vs-compiled](rag-vs-compiled.md)** — tradeoff analysis between retrieval-augmented generation and pre-compiled knowledge bases.
- **[open-questions](open-questions.md)** — unresolved ideas about knowledge freshness, confidence scoring, and self-updating corpora.

## References

- Source notes: `notes/tool-029-context-window-management-strat.md`, `notes/tool-031-rag-vs-compiled-knowledge-trade.md`
- Papers: `notes/paper-009-long-context-language-models-a.md`, `notes/paper-016-retrieval-augmented-generation.md`, `notes/paper-002-flare-active-retrieval-augment.md`
- Ideas: `notes/idea-000-i-keep-wondering-whether-compi.md` through `notes/idea-024-haven-t-worked-out-how-to-make.md`
