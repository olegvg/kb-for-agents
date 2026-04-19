# Tool Design for LLM Agents

How to define tools (functions) that agents use reliably: JSON schema, few-shot examples, and selection strategies.

## JSON schema design

`notes/tool-007-tool-use-json-schema-design.md` and its duplicate `notes/tool-042-tool-use-json-schema-design.md` document tool definition via JSON schema. The core finding: schema descriptions are model-facing documentation — vague descriptions produce misuse. Each parameter description should state what valid values look like and what happens with invalid input.

A constrained schema (enum values, pattern matching, required vs optional) outperforms an open schema even when the open schema would technically accept the correct answer. The model is more reliable when the schema narrows the choice space.

## Few-shot example selection

`notes/tool-005-few-shot-example-selection-stra.md` and its duplicate `notes/tool-040-few-shot-example-selection-stra.md` cover selecting few-shot examples for tool-use prompts. Giving the model a concrete example of the tool being called correctly — before presenting the actual task — cuts errors significantly. The example functions as an implicit schema validation: the model can match its output against the demonstrated shape.

## Structured output extraction

`notes/tool-021-structured-output-extraction.md` covers asking the model to return structured output (JSON, XML) rather than prose when the downstream consumer is a program. The key technique: provide the output schema in the prompt and optionally provide a partially-filled example. This is distinct from tool-use (the model is generating data, not calling a function) but the design principles overlap.

`notes/paper-021-toolformer-language-models-can.md` (Toolformer) provides the research context: models can learn to call tools self-supervised if given clear API descriptions. The implication for practitioners: investing in clear API descriptions is the highest-leverage improvement.

## References

- Source: `notes/tool-007-tool-use-json-schema-design.md`, `notes/tool-005-few-shot-example-selection-stra.md`, `notes/tool-021-structured-output-extraction.md`
- Papers: `notes/paper-004-large-language-models-as-tool-.md`, `notes/paper-021-toolformer-language-models-can.md`
