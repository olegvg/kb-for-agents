# Cost Management and Efficiency in Claude Code

How to control token costs and latency over long Claude Code sessions.

## Prompt caching

`notes/tool-026-prompt-caching-with-the-anthrop.md` covers the Anthropic SDK's prompt caching feature. The practical finding: static prefix content (CLAUDE.md, system prompt, tool definitions) benefits most from caching — these tokens are identical across turns and the cache hit eliminates their cost. Dynamic content (the conversation history) cannot be cached.

The strategy: put all stable context at the top of the prompt, before any dynamic content. This maximizes the cacheable prefix length.

## Cost management for long agent runs

`notes/tool-019-cost-management-for-long-agent-.md` documents cost management in multi-step agent runs. Key findings: not pinning the model version caused a surprise behavior change and wasted investigation time (a latent cost, not a direct token cost). Asking for too much in a single prompt led to shallow output that required a follow-up turn — doubling the cost of that step.

The pattern: model version pinning is a cost-control measure, not just a reproducibility measure. Silent rollouts change behavior.

## PR review automation

`notes/tool-023-pr-review-automation-with-claud.md` covers automating pull request review. The finding: diff-based review (agent sees only the changed lines) is more cost-effective than full-file review, and produces more focused feedback. This is a specific instance of the general principle: constrain the model's view to what's relevant.

## References

- Source: `notes/tool-026-prompt-caching-with-the-anthrop.md`, `notes/tool-019-cost-management-for-long-agent-.md`, `notes/tool-023-pr-review-automation-with-claud.md`
- Related: [configuration](configuration.md)
