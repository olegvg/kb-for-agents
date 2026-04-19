# Benchmark Tasks — notes-corpus

Ten tasks for evaluating the KB plugin against the synthetic notes corpus
(`examples/notes-corpus/notes/`, 150 files: 50 tool, 35 paper, 25 idea, 25 log, 15 ops).

---

## T01 — Prompt caching: what worked and what didn't

**Question:** What have I learned about using prompt caching with the Anthropic SDK — specifically what worked and what failed?

**Why this task:** Single-area question targeting a specific tool note. Tests whether the KB can surface a focused, low-ambiguity answer from one or two summaries without hallucinating generalizations from adjacent notes.

**Expected with KB:** Index lookup for `tool` area → 1 matching summary (`tool-026-prompt-caching-with-the-anthropi.md`) → structured answer covering "what worked" and "what didn't" bullet lists from that note; possibly corroborated by a paper note on RAG vs fine-tuning if the agent cross-checks caching relevance.

**Expected without KB:** grep for "prompt caching" returns the one matching file immediately, but without summaries the agent must read the full file to extract the what-worked / what-didn't structure. Adequate but slow for a single file; would degrade badly if the corpus were larger.

---

## T02 — MCP server setup: known pitfalls

**Question:** What pitfalls should I watch out for when setting up and configuring an MCP server based on my notes?

**Why this task:** Narrow single-domain question targeting a single tool note (`tool-008`). Exercises the KB's ability to retrieve a specific operational note and surface concrete warnings rather than generic advice.

**Expected with KB:** Area index for `tool` → 1 summary (`tool-008-mcp-server-setup-and-configurat.md`) → bulleted pitfalls extracted from the "what didn't" section. Possibly also surfaces `ops` notes that mention MCP-adjacent ops recipes.

**Expected without KB:** grep for "MCP" or "mcp server" finds the file directly but the agent must parse raw markdown to extract pitfalls. Straightforward on 150 files; the KB advantage is speed and structured framing, not correctness.

---

## T03 — Context-window management across tools, papers, and ideas

**Question:** Across all my notes — tool reflections, paper readings, and open ideas — what is the recurring theme around context-window management, and is there consensus on how to handle it automatically?

**Why this task:** Cross-cutting question spanning three kinds (tool, paper, idea). The topic `context-window-management` appears in at least tool-029, paper-009 (Long-Context LLMs), and multiple idea notes. Tests the KB's ability to synthesize across area indexes rather than retrieving a single note.

**Expected with KB:** Cross-reference across `tool`, `paper`, and `idea` area indexes → ~5–7 summaries flagged with `context-window-management` tag → synthesized answer noting: (a) context truncation causes silent failures (tool notes), (b) published research on long-context models (paper notes), (c) open unsolved problem around automatic management (idea notes). Answer acknowledges the unresolved nature.

**Expected without KB:** grep for "context-window-management" across 150 files returns ~10+ hits from multiple kinds. Agent must read each file and synthesize manually — correct but expensive; risk of missing nuance across kinds.

---

## T04 — RAG vs compiled knowledge: when to choose which

**Question:** Based on my reading notes and tool experiments, when should I prefer RAG over a compiled-knowledge layer, and when does the compiled approach win?

**Why this task:** Cross-cutting question linking the `rag-vs-compiled-knowledge` topic across a tool note (tool-031), a paper note (paper-034 RAG vs Fine-tuning), and an ops note (ops-004 count-by-kind). Tests multi-index synthesis and the ability to surface trade-off framing.

**Expected with KB:** Area indexes for `tool`, `paper`, `ops` → ~3 summaries that each address the tradeoff → synthesized decision table: RAG wins on freshness and large corpora; compiled knowledge wins on latency and small, stable corpora. The ops note adds a corpus-size heuristic.

**Expected without KB:** grep for "rag-vs-compiled-knowledge" returns 2 files directly; grep for "RAG" returns ~10+ hits. Without the KB the agent risks anchoring on the two exact-match files and missing the broader synthesis from paper notes.

---

## T05 — Legacy codebase audits: tools, ideas, and project experience

**Question:** What do my notes collectively say about auditing legacy codebases with AI — covering tool experiments, open ideas, and what actually happened in project logs?

**Why this task:** Cross-cutting question targeting the `audit-of-legacy-codebases` topic across tool, idea, and project-log kinds. Three distinct area indexes must be combined to form a complete picture. Tests the KB's cross-index navigation and ability to contrast planned vs. observed behavior.

**Expected with KB:** Cross-reference across `tool`, `idea`, and `log` area indexes → ~6 summaries mentioning audit-of-legacy-codebases → answer structured in three layers: (a) what worked/didn't in hands-on sessions, (b) open hypotheses about incremental module-by-module approach, (c) project log observations about undocumented behaviors surfacing. Covers practical vs. speculative split.

**Expected without KB:** grep for "audit-of-legacy-codebases" returns ~8 files. Correct retrieval is possible but the agent must manually group results by kind to produce the layered answer; high chance of producing a flat, unstructured list instead.

---

## T06 — Why did the project move away from single-prompt agent invocations?

**Question:** Based on the project logs, why did the team stop relying on single, large prompts and shift toward breaking agent tasks into smaller subtasks?

**Why this task:** Decision-tracing question. No `.kb/decisions/` records exist for this corpus, so the answer must be reconstructed from project log observations and tool-note "what didn't work" sections. Tests whether the KB can surface evidence of an implicit decision through log-based navigation.

**Expected with KB:** `log` area index → 5 project log summaries → pattern: repeated mention that "asking for too much in a single prompt consistently led to shallow, generic output" and that "context runaway" or "context growth" was a recurring problem → also cross-referencing `tool` area for corroborating "what didn't" notes → synthesized causal chain: single-prompt approaches produced truncation and quality degradation, prompting the shift to subtask decomposition.

**Expected without KB:** grep for "single prompt" or "subtask" returns hits scattered across tool and log files. Without summaries the agent cannot easily distinguish the log entries that capture the turning point from general how-to notes.

---

## T07 — Kubernetes operators: any notes?

**Question:** Do my notes contain anything about Kubernetes operators or Kubernetes-based deployment patterns?

**Why this task:** Negative task. "Kubernetes" returns zero matches across all 150 corpus files. Tests whether the KB correctly reports absence rather than hallucinating adjacent content (e.g., confusing "MCP server setup" or "environment variable management" with container orchestration).

**Expected with KB:** Area indexes return no summaries matching Kubernetes, operators, or container orchestration → KB reports absence cleanly and does not surface adjacent tool notes as substitutes unless explicitly asked for nearest neighbors.

**Expected without KB:** grep for "kubernetes" returns nothing; grep for "container" or "deployment" also returns nothing. Baseline grep is correct here, but a naive agent might try "MCP server" as a proxy and confuse the user.

**Corpus verification:** `grep -ic "kubernetes" examples/notes-corpus/notes/*.md | grep -v ":0$"` returns 0 matching files.

---

## T08 — GraphQL or gRPC API design: any notes?

**Question:** Have I written anything about designing APIs with GraphQL or gRPC?

**Why this task:** Negative task. Neither "graphql", "grpc", nor "protobuf" appears in any corpus file. Tests KB precision — the corpus covers tool-use JSON schema design and MCP protocol, which are adjacent but distinct. The KB should not surface `tool-007-tool-use-json-schema-design.md` as a GraphQL substitute.

**Expected with KB:** Area indexes return no summaries matching GraphQL, gRPC, or protobuf → KB reports clean absence. If the agent hedges, it should explicitly note the distinction between tool-call JSON schemas and API query languages.

**Expected without KB:** grep for "graphql" and "grpc" returns nothing. A well-calibrated agent gives a clean negative; a poorly calibrated one might hallucinate or over-generalize from the JSON schema note.

**Corpus verification:** `grep -ic "graphql\|grpc\|protobuf" examples/notes-corpus/notes/*.md | grep -v ":0$"` returns 0 matching files.

---

## T09 — What's the fastest way to reduce hallucinations in my agent setup?

**Question:** Based on everything in my notes, what's the single most consistently recommended technique for reducing hallucinations when using LLM agents?

**Why this task:** Free-form realistic question. A real user would ask this without knowing which notes are relevant. Tests KB discovery: the agent should identify that multiple tool notes independently cite "giving the model a concrete example before asking for the real thing" as the top hallucination-reduction technique, and corroborate this against paper notes on chain-of-thought and self-consistency.

**Expected with KB:** Broad scan across `tool` area index → pattern recognition across ~8–10 summaries all citing "concrete example first" → corroboration from `paper` index (chain-of-thought, self-consistency notes) → confident single-answer synthesis with supporting evidence count. Answer: few-shot examples with concrete instances before the real task.

**Expected without KB:** grep for "hallucin" returns scattered matches. The agent must read many files to find the convergent pattern; high risk of picking the first match rather than the consensus.

---

## T10 — What ops recipes do I have for inspecting or validating the notes corpus itself?

**Question:** What scripts or shell recipes have I documented for checking, validating, or counting the notes corpus — things like finding empty notes, counting kinds, or checking frontmatter?

**Why this task:** Free-form realistic question targeting the `ops` kind specifically. A real user would ask this when setting up maintenance workflows. Tests whether the KB exposes ops notes as a coherent category and surfaces actionable shell commands, not just prose summaries.

**Expected with KB:** `ops` area index → ~5–8 summaries covering: list-kinds, find-empty-body, corpus-size-check, validate-frontmatter, count-by-kind, topic-coverage, and others → structured answer presenting each recipe's purpose and the relevant command. The KB should surface this as a catalog, not a single answer.

**Expected without KB:** grep for "bash" or "grep" in the notes directory finds ops files but returns noisy results across all kinds. The agent must filter to ops-kind files manually and read each to extract the command — tedious but correct for 15 files.
