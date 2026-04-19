---
title: Using tool-use JSON schema design: notes and reflections
kind: tool
date: 2026-03-01
---

After a week of using tool-use JSON schema design in production work, I have notes worth writing down.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Incremental commits kept the feedback loop tight, which prevented runaway context growth. Treating each tool call as a unit test — verify input, verify output — kept drift in check. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

Picked up audit-of-legacy-codebases with AI assistance after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What didn't: Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Asking for explanations and code in the same response reliably produced worse code.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
