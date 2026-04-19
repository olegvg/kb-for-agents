---
title: Ops recipe: find empty body
kind: ops
date: 2026-01-14
---

Run this before each release to catch any files that drifted out of schema.

```bash
# Find notes without a body (only front matter)
awk '/^---/{c++} c==2{body=1} END{if(!body) print FILENAME}' notes/*.md
```
