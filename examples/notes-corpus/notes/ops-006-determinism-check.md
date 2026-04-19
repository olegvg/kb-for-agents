---
title: Ops recipe: determinism check
kind: ops
date: 2025-10-25
---

Pairs well with a pre-commit hook to keep the notes directory clean.

```bash
# Git diff to verify determinism after re-running generator
python3 generate.py && git diff --stat notes/
```
