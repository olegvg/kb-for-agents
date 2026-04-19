# Context Management

Strategies for managing information within context windows, tradeoffs between RAG and compiled summaries, and open research questions about knowledge freshness.

## When to enter

- You're asking about techniques for staying within context limits during long sessions.
- You're deciding whether to use retrieval or pre-compiled summaries for a knowledge task.
- You're thinking about how knowledge goes stale and what to do about it.

## Leaves

- **[overview](../summaries/context-management/overview.md)** — orientation and domain map.
- **[context-window-strategies](../summaries/context-management/context-window-strategies.md)** — practical techniques: single-responsibility subtasks, explicit state injection, logging.
- **[rag-vs-compiled](../summaries/context-management/rag-vs-compiled.md)** — when to choose retrieval vs pre-compiled knowledge, and hybrid approaches.
- **[open-questions](../summaries/context-management/open-questions.md)** — unresolved ideas: staleness scoring, confidence tags, self-updating corpora.

## See also

- **[rag-and-knowledge](rag-and-knowledge.md)** — implementation of retrieval (embeddings, pipelines) once you've decided to use RAG.

<!-- Max 300 tokens. Signposts only — no prose content. -->
