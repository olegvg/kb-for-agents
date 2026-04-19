---
title: Using prompt caching with the Anthropic SDK: notes and reflections
kind: tool
date: 2025-11-18
---

I spent the last few days experimenting with prompt caching with the Anthropic SDK and came away with a clearer picture than when I started.

What worked: Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Breaking the task into single-responsibility subtasks made each agent invocation predictable. I found that explicit constraints in the prompt outperformed general instructions every time. The iteration speed was noticeably faster once I stopped second-guessing the output.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
