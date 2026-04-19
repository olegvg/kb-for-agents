# AI-Assisted Legacy Codebase Audit Workflow

How to use LLMs to systematically audit a legacy codebase that lacks documentation.

## What the audit surfaces

`notes/tool-009-audit-of-legacy-codebases-with-.md` documents first-hand experience: auditing a legacy module with AI assistance surfaced "three undocumented behaviors" that had been invisible to grep and text search. The model's ability to reason about intent (not just pattern-match) is what makes it useful here — it can identify that a code path exists but is unreachable, or that a variable is set but never read.

The note confirms that breaking the audit into single-responsibility subtasks (one agent invocation per module, one per concern) produced better results than asking for a full audit in one pass. Each subtask's output was verifiable on its own.

`notes/paper-018-audit-of-legacy-codebases-usin.md` provides the research context: the paper combines static analysis (precise but shallow) with LLM reasoning (fuzzy but deep) to cover the gap each approach leaves. The evaluation methodology in the paper is worth borrowing even if the specific tools are not available — the idea of categorizing findings by "undocumented behavior", "dead code", and "schema drift" transfers directly to manual agent-assisted audits.

## Incremental audit approach

`notes/idea-002-what-if-audit-of-legacy-codeba.md` / `notes/idea-016-what-if-audit-of-legacy-codeba.md` propose an incremental approach: rather than one large audit session, trigger a focused re-audit whenever a module is modified. The model sees the diff plus the existing audit summary for that module, and updates the findings. Not yet tested — still an open hypothesis.

## Connection to project experience

Project logs for `kb-for-agents` (`notes/log-kb-for-agents-2025-11-09.md`, `notes/log-kb-for-agents-2026-04-12.md`) repeatedly note "classic audit-of-legacy-codebases territory" when undocumented behaviors surface. This suggests the pattern recurs in active development, not just during dedicated audit sessions.

## References

- Source: `notes/tool-009-audit-of-legacy-codebases-with-.md`
- Papers: `notes/paper-018-audit-of-legacy-codebases-usin.md`, `notes/paper-019-software-engineering-with-larg.md`
- Ideas: `notes/idea-002-what-if-audit-of-legacy-codeba.md`
- Related: [tdd-with-ai](tdd-with-ai.md)
