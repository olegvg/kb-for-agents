---
title: Using extended thinking mode usage: notes and reflections
kind: tool
date: 2026-02-01
---

I kept putting off a proper look at extended thinking mode usage, but a failing deadline pushed me into it.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Incremental commits kept the feedback loop tight, which prevented runaway context growth. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Asking for too much in a single prompt consistently led to shallow, generic output. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

The setup cost is real, but it pays back on the third use. Probably worth it.
