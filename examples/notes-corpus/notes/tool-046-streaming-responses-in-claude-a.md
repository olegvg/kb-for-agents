---
title: Using streaming responses in Claude API: notes and reflections
kind: tool
date: 2026-01-10
---

I spent the last few days experimenting with streaming responses in Claude API and came away with a clearer picture than when I started.

What worked: Treating each tool call as a unit test — verify input, verify output — kept drift in check. Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
