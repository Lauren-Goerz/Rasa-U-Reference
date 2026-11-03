Custom actions you want Rasa to use need to be listed in the domain under `actions:`. Having a Python file in `actions/` is not enough on its own, the action name also needs to appear in the domain so Rasa knows to call it.
 
> In Rasa, an `action:` step in a flow can refer to either a custom action name or a response name. Both are valid step targets. This section covers listing custom actions in the domain.
 
---