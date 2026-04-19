---
title: Using self-evaluation and reflection prompts: notes and reflections
kind: tool
date: 2025-11-16
---

I tried self-evaluation and reflection prompts on a real project rather than a toy example, which made all the difference.

What worked: Treating each tool call as a unit test — verify input, verify output — kept drift in check. Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

Picked up self-evaluation and reflection prompts after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.

Still forming a verdict. What I have is enough to keep experimenting.
