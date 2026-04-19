# Agent Patterns

Design, orchestration, and debugging of multi-step LLM agent systems: loops, subagents, memory, and self-evaluation.

## When to enter

- You're designing a multi-step agent workflow and want structural patterns.
- You're debugging an agent loop that drifts or produces inconsistent output.
- You're deciding how to dispatch and collect results from subagents.
- You need the agent to verify its own outputs before proceeding.

## Leaves

- **[overview](../summaries/agent-patterns/overview.md)** — orientation and domain map.
- **[agent-loop-design](../summaries/agent-patterns/agent-loop-design.md)** — loop structure, single-responsibility steps, logging, failure modes.
- **[subagent-orchestration](../summaries/agent-patterns/subagent-orchestration.md)** — parallel vs sequential dispatch, context isolation, result aggregation.
- **[memory-and-state](../summaries/agent-patterns/memory-and-state.md)** — stateful vs stateless calls, explicit state injection, working-state documents.
- **[self-evaluation](../summaries/agent-patterns/self-evaluation.md)** — reflection prompts, chain-of-thought verification, error recovery.

## See also

- **[context-management](context-management.md)** — context limits are the primary constraint on agent loop design.

<!-- Max 300 tokens. Signposts only — no prose content. -->
