---
title: Ops recipe: rebuild title index
kind: ops
date: 2025-10-01
---

Useful when the notes directory has grown beyond what a single grep can survey cleanly.

```bash
# Rebuild index of note titles
grep -h "^title:" notes/*.md | sed 's/^title: //' | sort > /tmp/note-titles.txt
wc -l /tmp/note-titles.txt
```
