---
title: Using few-shot example selection strategies: notes and reflections
kind: tool
date: 2025-10-23
---

After a week of using few-shot example selection strategies in production work, I have notes worth writing down.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

I tried agent memory architectures on a real project rather than a toy example, which made all the difference.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Not pinning the model version meant a surprise behavior change after a silent rollout.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
