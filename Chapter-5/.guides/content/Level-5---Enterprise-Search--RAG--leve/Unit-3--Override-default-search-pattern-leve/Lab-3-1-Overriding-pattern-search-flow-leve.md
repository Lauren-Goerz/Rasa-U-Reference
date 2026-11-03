<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add `pattern_search` to override out of the agent pattern for knowledge questions.

Rasa ships with built-in patterns that handle common conversational situations by default: `pattern_search`, `pattern_clarification`, `pattern_cannot_handle`, `pattern_correct`, and others. No configuration required.

To override a pattern, create a flow file with the same `id`. Rasa will then use your version instead of the built-in one. The id must match exactly. This works for any default pattern, not just `pattern_search`. The Rasa Docs list [common pattern customizations](https://rasa.com/docs/reference/primitives/patterns/).

When the command generator emits a `KnowledgeAnswerCommand`, Rasa runs `pattern_search`. Out of the box, this system flow is configured to call `utter_no_knowledge_base`, because there is no search backend configured.

To wire in Enterprise Search, override `pattern_search` with a single step: `action_trigger_search`. This action is added automatically by `EnterpriseSearchPolicy` (no need to register it in `domain`) and handles retrieval and response generation.

Create `chapter5/data/basics/pattern_search.yml`:


```yaml
flows:
  pattern_search:
    name: pattern search
    description: Answers knowledge questions using the enterprise search index.
    steps:
      - action: action_trigger_search
```
 
`action_trigger_search` is a Rasa default action and does not need to be registered in `domain/*.yml`.
 
 {Check It!|assessment}(code-output-compare-3129967275)
