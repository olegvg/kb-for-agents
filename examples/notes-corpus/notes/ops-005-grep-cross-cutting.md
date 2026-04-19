---
title: Ops recipe: grep cross cutting
kind: ops
date: 2025-11-28
---

Essential before handing the corpus to an agent that expects a specific schema.

```bash
# Find notes mentioning a cross-cutting topic
grep -li "context-window-management" notes/*.md
```
