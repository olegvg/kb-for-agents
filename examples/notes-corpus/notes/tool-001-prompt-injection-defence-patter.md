---
title: Using prompt injection defence patterns: notes and reflections
kind: tool
date: 2025-10-16
---

Picked up prompt injection defence patterns after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Breaking the task into single-responsibility subtasks made each agent invocation predictable. I found that explicit constraints in the prompt outperformed general instructions every time.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. I wasted time when I let the model pick its own tools without providing a bounded tool list. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded.

The setup cost is real, but it pays back on the third use. Probably worth it.
