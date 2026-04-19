---
title: Ops recipe: validate frontmatter
kind: ops
date: 2026-03-29
---

Part of my standard audit-of-legacy-codebases checklist.

```bash
# Validate YAML front matter has required fields
for f in notes/*.md; do
  python3 -c "
import sys, re
txt = open('$f').read()
fm = re.search(r'^---\n(.*?)\n---', txt, re.S)
if not fm: sys.exit('missing front matter: $f')
block = fm.group(1)
for field in ('title', 'kind', 'date'):
    if field + ':' not in block:
        sys.exit(f'missing {field}: $f')
"
done && echo "all ok"
```
