---
title: Using environment variable management in agents: notes and reflections
kind: tool
date: 2025-09-14
---

Picked up environment variable management in agents after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. I found that explicit constraints in the prompt outperformed general instructions every time. Logging every agent turn to a file let me spot the exact step where things went sideways.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. I wasted time when I let the model pick its own tools without providing a bounded tool list.

Still forming a verdict. What I have is enough to keep experimenting.
