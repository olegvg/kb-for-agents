# kb-for-agents Project Log

Session notes from building the kb-for-agents system — the three-layer knowledge base plugin for Claude Code.

## Recurring patterns

Across the nine log entries (`notes/log-kb-for-agents-2025-11-09.md` through `notes/log-kb-for-agents-2026-04-12.md`), several patterns appear repeatedly:

**Context-window-management as the bottleneck.** The earliest log (`2025-11-09`) records: "Discovered that the bottleneck was context-window-management rather than model capability." This reframing — from "the model isn't smart enough" to "I'm not managing context well enough" — is the central lesson of the project.

**Undocumented legacy behaviors.** Multiple logs note "found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory." The kb-for-agents codebase itself has legacy-like accumulation even though it is new — undocumented behaviors emerge quickly when a system grows faster than its documentation.

**Schema changes ripple.** The `2025-11-09` log records: "The schema change rippled further than expected — four files needed touching, not one." This is a recurring cost of iterative development without full test coverage — the audit-find-fix loop is slower than it should be.

**Setup cost amortizes.** The `2026-04-12` log: "Spent the first hour on setup, which felt wasteful but probably saved three hours of misaligned effort." This matches the MCP setup note's finding that the setup cost "pays back on the third use."

## Arc of the project

The logs show a progression from "figure out what's blocking me" (early logs) to "refactor for testability and move to next task" (late logs). The `2026-04-12` entry — "refactored the core loop to be side-effect-free, which made the agent calls trivially testable" — reflects a matured understanding of the architecture.

## References

- Source: `notes/log-kb-for-agents-2025-11-09.md`, `notes/log-kb-for-agents-2026-02-16.md`, `notes/log-kb-for-agents-2026-03-10.md`, `notes/log-kb-for-agents-2026-03-12.md`, `notes/log-kb-for-agents-2026-03-20.md`, `notes/log-kb-for-agents-2026-03-22.md`, `notes/log-kb-for-agents-2026-03-24.md`, `notes/log-kb-for-agents-2026-04-12.md`
