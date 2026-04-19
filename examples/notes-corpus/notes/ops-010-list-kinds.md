---
title: Ops recipe: list kinds
kind: ops
date: 2026-03-28
---

Run this before each release to catch any files that drifted out of schema.

```bash
# List all unique kind values
grep -h "^kind:" notes/*.md | sort -u
```
