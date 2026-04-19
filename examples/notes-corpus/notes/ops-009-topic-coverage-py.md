---
title: Ops recipe: topic coverage py
kind: ops
date: 2025-11-25
---

Essential before handing the corpus to an agent that expects a specific schema.

```python
# Detect cross-cutting topic coverage across kinds
import re
from pathlib import Path

topics = ["context-window-management", "rag-vs-compiled-knowledge", "audit-of-legacy-codebases"]
notes = list(Path("notes").glob("*.md"))

for topic in topics:
    kinds = set()
    for note in notes:
        txt = note.read_text().lower()
        if topic in txt:
            m = re.search(r"^kind:\s*(\S+)", txt, re.M)
            if m:
                kinds.add(m.group(1))
    print(f"{topic}: {sorted(kinds)}")
```
