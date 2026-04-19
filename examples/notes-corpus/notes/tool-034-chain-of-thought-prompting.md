---
title: Using chain-of-thought prompting: notes and reflections
kind: tool
date: 2026-03-23
---

I kept putting off a proper look at chain-of-thought prompting, but a failing deadline pushed me into it.

What worked: Treating each tool call as a unit test — verify input, verify output — kept drift in check. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

What didn't: Not pinning the model version meant a surprise behavior change after a silent rollout. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.

I spent the last few days experimenting with few-shot example selection strategies and came away with a clearer picture than when I started.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
