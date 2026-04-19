---
title: Ops recipe: list kinds
kind: ops
date: 2025-10-27
---

Useful when the notes directory has grown beyond what a single grep can survey cleanly.

```bash
# List all unique kind values
grep -h "^kind:" notes/*.md | sort -u
```
