---
title: Project log: mcp-telegram-bot — 2026-02-04
kind: project-log
date: 2026-02-04
---

Checkpoint before switching to a different part of the codebase.

Spent the first hour on setup, which felt wasteful but probably saved three hours of misaligned effort.

The difference between RAG-vs-compiled-knowledge retrieval approaches showed up in latency, not quality.

The integration test caught something the unit test missed, which is the right order of events.

Found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory.

Next session: wire up the end-to-end test and do a timing run.
