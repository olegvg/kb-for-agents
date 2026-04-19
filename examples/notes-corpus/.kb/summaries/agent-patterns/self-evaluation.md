# Self-Evaluation and Reflection in Agents

Techniques for agents to assess their own outputs, catch errors before they propagate, and recover from mistakes.

## Reflection prompts

`notes/tool-003-self-evaluation-and-reflection-.md` covers practical reflection prompts: after generating an output, a follow-up prompt asking the model to critique its own response ("What could be wrong? What did I miss?") reliably surfaces issues that a final-answer-only prompt missed. The technique works because the critique prompt shifts the model from generation mode into evaluation mode.

`notes/paper-003-reflexion-language-agents-with.md` (Reflexion) formalizes this into a training signal: verbal reinforcement using the agent's own reflections as feedback. The practical takeaway is that the reflection format matters — a structured critique with specific error categories outperforms an open-ended "was this correct?".

## Chain-of-thought as verification

`notes/tool-034-chain-of-thought-prompting.md` and `notes/paper-000-chain-of-thought-prompting-eli.md` document chain-of-thought prompting: asking the model to reason step-by-step before answering. The corpus notes that explicit constraints in the step-by-step prompt produce better verification than letting the model choose its own reasoning path.

`notes/paper-011-self-consistency-improves-chai.md` adds the self-consistency angle: generating multiple reasoning chains and taking the majority answer reduces errors further, at the cost of more inference calls.

## Error recovery in practice

`notes/tool-013-error-recovery-in-multi-step-ag.md` documents the operational side: when a step fails, the recovery prompt should include the failing step's input, the observed error, and an explicit instruction to diagnose before retrying. Retrying without diagnosis produces the same error.

## References

- Source: `notes/tool-003-self-evaluation-and-reflection-.md`, `notes/tool-013-error-recovery-in-multi-step-ag.md`, `notes/tool-034-chain-of-thought-prompting.md`
- Papers: `notes/paper-003-reflexion-language-agents-with.md`, `notes/paper-000-chain-of-thought-prompting-eli.md`, `notes/paper-011-self-consistency-improves-chai.md`, `notes/paper-017-tree-of-thoughts-deliberate-pr.md`
