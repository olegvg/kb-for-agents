---
title: Project log: mcp-telegram-bot — 2026-02-21
kind: project-log
date: 2026-02-21
---

Checkpoint before switching to a different part of the codebase.

I leaned on the agent more than planned and it held up, which was a pleasant surprise.

The integration test caught something the unit test missed, which is the right order of events.

Refactored the core loop to be side-effect-free, which made the agent calls trivially testable.

Spent the first hour on setup, which felt wasteful but probably saved three hours of misaligned effort.

Enough for today. The hard part is done.
