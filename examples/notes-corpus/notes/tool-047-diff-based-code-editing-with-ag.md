---
title: Using diff-based code editing with agents: notes and reflections
kind: tool
date: 2026-02-25
---

I tried diff-based code editing with agents on a real project rather than a toy example, which made all the difference.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. Breaking the task into single-responsibility subtasks made each agent invocation predictable. Treating each tool call as a unit test — verify input, verify output — kept drift in check. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

What didn't: I wasted time when I let the model pick its own tools without providing a bounded tool list. Asking for explanations and code in the same response reliably produced worse code.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
