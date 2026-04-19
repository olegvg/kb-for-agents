---
title: Using audit-of-legacy-codebases with AI assistance: notes and reflections
kind: tool
date: 2026-02-22
---

I kept putting off a proper look at audit-of-legacy-codebases with AI assistance, but a failing deadline pushed me into it.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. Treating each tool call as a unit test — verify input, verify output — kept drift in check. The iteration speed was noticeably faster once I stopped second-guessing the output. Logging every agent turn to a file let me spot the exact step where things went sideways.

What didn't: Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. I wasted time when I let the model pick its own tools without providing a bounded tool list. Asking for explanations and code in the same response reliably produced worse code.

I spent the last few days experimenting with rate-limit handling in agent pipelines and came away with a clearer picture than when I started.

Still forming a verdict. What I have is enough to keep experimenting.
