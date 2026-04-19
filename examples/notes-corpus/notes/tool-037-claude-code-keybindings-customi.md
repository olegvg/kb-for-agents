---
title: Using Claude Code keybindings customisation: notes and reflections
kind: tool
date: 2025-09-25
---

Three hours in with Claude Code keybindings customisation and I already had opinions. Here's what I found.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. Logging every agent turn to a file let me spot the exact step where things went sideways.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Asking for too much in a single prompt consistently led to shallow, generic output. I wasted time when I let the model pick its own tools without providing a bounded tool list.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
