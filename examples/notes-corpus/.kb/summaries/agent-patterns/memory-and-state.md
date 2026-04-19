# Agent Memory Architectures

How agents store, retrieve, and maintain state across turns — and why the architecture matters.

## Types of memory

`notes/tool-016-agent-memory-architectures.md` distinguishes between relying on the model's implicit memory of earlier turns versus explicitly re-injecting key facts into each prompt. The note records a clear failure mode from implicit memory: "over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five." By step four, facts from step one are competing with many tokens of intervening context and may be attended to less reliably.

The remediation is explicit state injection: maintain a small working-state document that is prepended to each prompt, updated after each step. This trades a few hundred tokens per turn for consistent access to key decisions.

## Stateful vs stateless agent calls

Stateless calls (each invocation is independent, no shared mutable state) are easier to parallelize and easier to test. `notes/tool-016` confirms the pattern: single-responsibility subtasks plus explicit state injection enables stateless calls even in a multi-step workflow.

`notes/paper-008-generative-agents-interactive-.md` (Generative Agents) provides the research reference for long-running memory: their architecture uses a memory stream with retrieval — a hybrid of explicit logs and vector retrieval — which is the research-grade version of what practitioners arrive at empirically.

## Practical recommendation

For most practical agent workflows (not long-running simulations), a flat key-value working state document is sufficient. Keep it under 200 tokens. Update it explicitly after each step. Re-inject it at the top of each subsequent prompt.

## References

- Source: `notes/tool-016-agent-memory-architectures.md`
- Paper: `notes/paper-008-generative-agents-interactive-.md`, `notes/paper-010-llm-based-autonomous-agent-sur.md`
- Related: [agent-loop-design](agent-loop-design.md), [context-management/context-window-strategies](../../context-management/context-window-strategies.md)
