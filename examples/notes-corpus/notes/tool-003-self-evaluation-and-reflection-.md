---
title: Using self-evaluation and reflection prompts: notes and reflections
kind: tool
date: 2025-12-18
---

I spent the last few days experimenting with self-evaluation and reflection prompts and came away with a clearer picture than when I started.

What worked: I found that explicit constraints in the prompt outperformed general instructions every time. The iteration speed was noticeably faster once I stopped second-guessing the output. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
