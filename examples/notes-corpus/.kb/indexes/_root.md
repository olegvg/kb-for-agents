# Notes Corpus — Knowledge Base

Top-level map. Entry point for all KB navigation. Read this first on any query.

## Areas

- **[context-management](context-management.md)** — context window strategies, RAG vs compiled knowledge tradeoffs, open questions about staleness and freshness.
- **[agent-patterns](agent-patterns.md)** — agent loop design, subagent orchestration, memory architectures, self-evaluation and error recovery.
- **[claude-code-workflow](claude-code-workflow.md)** — CLAUDE.md configuration, slash commands, hooks, plugin authoring, cost and efficiency patterns.
- **[rag-and-knowledge](rag-and-knowledge.md)** — embedding-based retrieval, hybrid pipelines, knowledge graphs, codebase summarization for agents.
- **[legacy-audits](legacy-audits.md)** — AI-assisted legacy codebase auditing and test-driven development as follow-on.
- **[mcp-and-tools](mcp-and-tools.md)** — MCP server setup, tool JSON schema design, streaming, rate limits, prompt injection defense.
- **[project-experience](project-experience.md)** — session logs from three projects (kb-for-agents, mcp-telegram-bot, personal-brand-ai) and corpus maintenance recipes.

## Navigation rules

- First access to the KB: always read this file, then pick 1–3 area indexes.
- Once inside a summary, you may follow direct references between summaries without returning here.
- If none of the areas match your question, the answer isn't in the KB — fall back to reading sources directly in `notes/`.

<!-- Keep this file under 300 tokens. If it grows, an area probably needs its own sub-root — split and link. -->
