---
title: Using hook-driven automation in Claude Code: notes and reflections
kind: tool
date: 2026-01-23
---

After a week of using hook-driven automation in Claude Code in production work, I have notes worth writing down.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Breaking the task into single-responsibility subtasks made each agent invocation predictable. The iteration speed was noticeably faster once I stopped second-guessing the output. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Not pinning the model version meant a surprise behavior change after a silent rollout.

The setup cost is real, but it pays back on the third use. Probably worth it.
