---
title: Ops recipe: corpus size check
kind: ops
date: 2026-02-18
---

Handy for debugging context-window-management issues in long agent sessions.

```bash
# Check corpus size
ls notes/*.md | wc -l
```
