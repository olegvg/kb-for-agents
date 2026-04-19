---
title: Project log: kb-for-agents — 2025-11-09
kind: project-log
date: 2025-11-09
---

End-of-day notes on what actually happened.

Discovered that the bottleneck was context-window-management rather than model capability.

The integration test caught something the unit test missed, which is the right order of events.

Found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory.

The schema change rippled further than expected — four files needed touching, not one.

Next session: wire up the end-to-end test and do a timing run.
