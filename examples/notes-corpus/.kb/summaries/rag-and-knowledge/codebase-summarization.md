# Codebase Summarization for Agents

How to produce agent-readable summaries of large codebases or note corpora.

## The summarization challenge

`notes/tool-030-codebase-summarisation-for-agen.md` documents the core challenge: a codebase is too large to fit in context, but an agent needs enough understanding to navigate it. Naive summarization (summarize each file independently) loses cross-file relationships. The finding: summarizing by semantic domain (grouping files that answer the same class of question) produces summaries agents can navigate, versus summaries that mirror the directory tree.

This is the same principle underlying the three-layer KB structure: group by what a user would ask, not by where things sit in the filesystem.

## Connection to this corpus

The notes corpus itself is a small-scale version of this problem. The `.kb/` structure being built is an answer to the question: how do you make 150 notes navigable without reading all 150? The answer is the same: domain grouping → summary → index.

## Structured output in summarization

`notes/tool-021-structured-output-extraction.md` is relevant here: when an agent produces summaries, asking for structured output (JSON schema with explicit fields for domain, leaf topics, source citations) produces more consistent, machine-parseable results than asking for free-form prose. The downstream index-writing step becomes more reliable when summaries have a predictable shape.

## References

- Source: `notes/tool-030-codebase-summarisation-for-agen.md`, `notes/tool-021-structured-output-extraction.md`
- Related: [context-management/rag-vs-compiled](../../context-management/rag-vs-compiled.md)
