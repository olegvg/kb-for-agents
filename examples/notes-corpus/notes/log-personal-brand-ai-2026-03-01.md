---
title: Project log: personal-brand-ai — 2026-03-01
kind: project-log
date: 2026-03-01
---

Unblocked this morning after sleeping on the problem.

Discovered that the bottleneck was context-window-management rather than model capability.

Found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory.

The piece that was blocking me turned out to be a wrong assumption about the data shape, not a code bug.

The integration test caught something the unit test missed, which is the right order of events.

Enough for today. The hard part is done.
