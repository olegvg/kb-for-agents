---
title: Using cost management for long agent runs: notes and reflections
kind: tool
date: 2025-11-01
---

I spent the last few days experimenting with cost management for long agent runs and came away with a clearer picture than when I started.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
