---
title: Ops recipe: count by kind
kind: ops
date: 2025-11-04
---

Helps when deciding between RAG-vs-compiled-knowledge for a specific corpus size.

```bash
# Count files by kind (front matter)
grep -rl "^kind:" notes/ | xargs grep -h "^kind:" | sort | uniq -c | sort -rn
```
