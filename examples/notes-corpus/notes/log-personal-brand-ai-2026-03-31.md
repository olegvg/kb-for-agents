---
title: Project log: personal-brand-ai — 2026-03-31
kind: project-log
date: 2026-03-31
---

Writing this mid-session because the insight is too perishable to save for later.

Refactored the core loop to be side-effect-free, which made the agent calls trivially testable.

Discovered that the bottleneck was context-window-management rather than model capability.

Next session: wire up the end-to-end test and do a timing run.
