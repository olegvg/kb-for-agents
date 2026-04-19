# Operational Concerns for Tool-Using Agents

Streaming, rate limits, environment variable management, and prompt injection defense.

## Streaming responses

`notes/tool-011-streaming-responses-in-claude-a.md` covers streaming. For interactive agent workflows, streaming matters for perceived latency; for batch pipelines, it matters less. The note confirms that explicit constraints in the streaming setup (buffer size, flush triggers) outperformed leaving defaults in place — defaults were optimized for the average case, not for long tool-call responses.

## Rate limit handling

`notes/tool-032-rate-limit-handling-in-agent-pi.md` documents rate limit handling. The practical pattern: exponential backoff with jitter, with a maximum retry count. The note records that not pinning the model version caused unexpected rate limit behavior after a provider-side change. Model version pinning is also a rate-limit control measure.

## Environment variable management

`notes/tool-010-environment-variable-management.md` covers env vars in agent pipelines. The key principle: secrets and configuration should never appear in prompt text — inject them via environment variables and reference them in code. The pattern also applies to MCP server configuration: connection strings in env vars, not in CLAUDE.md.

## Prompt injection defense

`notes/tool-001-prompt-injection-defence-patter.md` and its duplicate `notes/tool-036-prompt-injection-defence-patter.md` document defense against prompt injection: adversarial content in retrieved documents or tool outputs that attempts to hijack the agent's instructions. The primary defense is input sanitization at retrieval time plus an explicit system prompt instruction that retrieved content is untrusted.

`notes/paper-020-prompt-injection-attacks-and-d.md` provides the academic taxonomy of injection attack types and corresponding defenses.

## References

- Source: `notes/tool-011-streaming-responses-in-claude-a.md`, `notes/tool-032-rate-limit-handling-in-agent-pi.md`, `notes/tool-010-environment-variable-management.md`, `notes/tool-001-prompt-injection-defence-patter.md`
- Papers: `notes/paper-020-prompt-injection-attacks-and-d.md`
