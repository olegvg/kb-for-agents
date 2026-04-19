---
title: Using streaming responses in Claude API: notes and reflections
kind: tool
date: 2026-04-18
---

Picked up streaming responses in Claude API after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: I found that explicit constraints in the prompt outperformed general instructions every time. Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Asking for explanations and code in the same response reliably produced worse code. I wasted time when I let the model pick its own tools without providing a bounded tool list.

Picked up chain-of-thought prompting after seeing it mentioned twice in the same week. Decided it warranted a proper try.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
