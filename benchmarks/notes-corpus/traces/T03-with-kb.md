# T03 — with-kb

**Question:** Across all my notes — tool reflections, paper readings, and open ideas — what is the recurring theme around context-window management, and is there consensus on how to handle it automatically?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/context-management.md`
3. `examples/notes-corpus/.kb/summaries/context-management/context-window-strategies.md`
4. `examples/notes-corpus/.kb/summaries/context-management/open-questions.md`

## Tool calls
- Read × 4
- Grep × 0
- Glob × 0

## Tokens read from corpus
~1650  
(_root.md 404 + context-management index 319 + context-window-strategies 534 + open-questions 531)

## Answer

The recurring theme across tool notes, paper readings, and idea notes is that context-window limits cause silent failures — truncation that corrupts agent state without raising an error — and that the model's attention degrades for content positioned in the middle of the window (documented in `notes/paper-009-long-context-language-models-a.md`). The practical consensus for mitigation is: (1) single-responsibility subtasks so each invocation's context budget is predictable; (2) explicit re-injection of key state at each turn rather than relying on implicit memory; (3) treating each tool call as a unit test to surface truncation early. On automatic management, there is no consensus — the idea notes (`notes/idea-011-there-s-an-open-question-about.md`) explicitly flag this as unresolved: whether context-window limits are a temporary engineering constraint (solved by larger windows) or a permanent architectural signal is an open question. The idea notes also propose freshness scoring (`idea-001`) and confidence tagging (`idea-006`) as potential components of an automatic system, but none have been tested. The honest answer is that manual discipline (subtask decomposition, explicit state injection) is the only validated approach; automatic management remains speculative.
