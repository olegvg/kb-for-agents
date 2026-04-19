---
title: Ops recipe: word count dist
kind: ops
date: 2025-08-19
---

Handy for debugging context-window-management issues in long agent sessions.

```bash
# Quick word-count distribution
wc -w notes/*.md | sort -n | tail -20
```
