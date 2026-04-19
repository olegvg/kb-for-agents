---
title: Project log: kb-for-agents — 2025-12-07
kind: project-log
date: 2025-12-07
---

Short entry — context is fresher than it will be tomorrow.

Refactored the core loop to be side-effect-free, which made the agent calls trivially testable.

The schema change rippled further than expected — four files needed touching, not one.

Discovered that the bottleneck was context-window-management rather than model capability.

Found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory.

Enough for today. The hard part is done.
