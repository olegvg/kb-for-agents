---
title: Using environment variable management in agents: notes and reflections
kind: tool
date: 2026-02-02
---

I tried environment variable management in agents on a real project rather than a toy example, which made all the difference.

What worked: I found that explicit constraints in the prompt outperformed general instructions every time. Breaking the task into single-responsibility subtasks made each agent invocation predictable. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
