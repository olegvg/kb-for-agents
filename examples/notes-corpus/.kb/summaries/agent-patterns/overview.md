# Agent Patterns — Overview

This domain covers how to design, orchestrate, and debug multi-step LLM agent systems. It spans agent loop design, subagent dispatching, memory architectures, self-evaluation, error recovery, and the academic literature on autonomous agents.

The corpus includes direct tool notes from practice (`tool-033`, `tool-014`, `tool-015`, `tool-016`, `tool-013`, `tool-003`) and paper readings covering ReAct, Reflexion, cognitive architectures, generative agents, and chain-of-thought prompting (`paper-001`, `paper-003`, `paper-005`, `paper-011`, `paper-017`).

The domain is oriented around a practitioner doing solo development augmented by agents, so patterns are evaluated by whether they reduce review burden and context overhead in real sessions — not just by benchmark performance.

## Leaves in this domain

- **[agent-loop-design](agent-loop-design.md)** — structure of the agent loop: single vs multi-turn, side-effect-free steps, logging.
- **[subagent-orchestration](subagent-orchestration.md)** — dispatching parallel and sequential subagents, context isolation, result aggregation.
- **[memory-and-state](memory-and-state.md)** — agent memory architectures, stateful vs stateless calls, persisting key facts.
- **[self-evaluation](self-evaluation.md)** — reflection prompts, chain-of-thought verification, error recovery patterns.

## References

- Tool notes: `notes/tool-033-agent-loop-design-patterns.md`, `notes/tool-014-parallel-subagent-orchestration.md`, `notes/tool-015-subagent-dispatching-patterns.md`, `notes/tool-016-agent-memory-architectures.md`, `notes/tool-013-error-recovery-in-multi-step-ag.md`, `notes/tool-003-self-evaluation-and-reflection-.md`
- Papers: `notes/paper-001-react-synergizing-reasoning-an.md`, `notes/paper-003-reflexion-language-agents-with.md`, `notes/paper-005-cognitive-architectures-for-la.md`, `notes/paper-010-llm-based-autonomous-agent-sur.md`
