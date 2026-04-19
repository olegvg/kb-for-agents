---
title: Using multi-turn conversation design: notes and reflections
kind: tool
date: 2025-12-06
---

I kept putting off a proper look at multi-turn conversation design, but a failing deadline pushed me into it.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. The iteration speed was noticeably faster once I stopped second-guessing the output.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded.

After a week of using prompt caching with the Anthropic SDK in production work, I have notes worth writing down.

Would recommend to anyone already comfortable with the basics — not a first step.
