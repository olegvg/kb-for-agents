# T05 — with-kb

**Question:** What do my notes collectively say about auditing legacy codebases with AI — covering tool experiments, open ideas, and what actually happened in project logs?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/legacy-audits.md`
3. `examples/notes-corpus/.kb/summaries/legacy-audits/audit-workflow.md`
4. `examples/notes-corpus/.kb/summaries/legacy-audits/tdd-with-ai.md`
5. `examples/notes-corpus/.kb/indexes/project-experience.md`
6. `examples/notes-corpus/.kb/summaries/project-experience/kb-for-agents-log.md`

## Tool calls
- Read × 6
- Grep × 0
- Glob × 0

## Tokens read from corpus
~2620  
(_root.md 404 + legacy-audits index 262 + audit-workflow 587 + tdd-with-ai 461 + project-experience index 321 + kb-for-agents-log 554)

## Answer

Three layers of evidence across the notes: (1) Tool experiments (`notes/tool-009-audit-of-legacy-codebases-with-.md`): auditing a legacy module with AI surfaced three undocumented behaviors invisible to grep and text search — the model's ability to reason about intent (unreachable code paths, set-but-never-read variables) is the key differentiator. Breaking the audit into single-responsibility subtasks (one agent invocation per module, one per concern) produced verifiable results; a single-pass full-audit request did not. (2) Open ideas (`notes/idea-002` / `idea-016`): an incremental approach is hypothesized — trigger a focused re-audit whenever a module is modified, with the model seeing the diff plus the existing audit summary for that module. Not yet tested. (3) Project logs (`notes/log-kb-for-agents-2025-11-09.md` and others): the pattern "found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory" recurs across multiple sessions, suggesting the pattern emerges naturally in active development, not just during dedicated audit sessions. The follow-on pattern is TDD: audit findings become formalized test contracts, with diff-based editing (`notes/tool-012`) to implement them precisely.
