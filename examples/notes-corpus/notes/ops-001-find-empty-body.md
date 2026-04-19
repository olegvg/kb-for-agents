---
title: Ops recipe: find empty body
kind: ops
date: 2025-12-13
---

Use this to verify that retrieval indexes are consistent with the source notes.

```bash
# Find notes without a body (only front matter)
awk '/^---/{c++} c==2{body=1} END{if(!body) print FILENAME}' notes/*.md
```
