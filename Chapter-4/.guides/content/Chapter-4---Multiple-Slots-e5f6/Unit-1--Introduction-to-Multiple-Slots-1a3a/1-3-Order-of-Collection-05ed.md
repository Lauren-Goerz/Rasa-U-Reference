The order of `collect:` steps is the order the agent asks for values when slots are empty. Rasa can collect multiple memory items at once so if the user provides all the needed information up front, it won't ask for information again. 
 
```yaml
steps:
  - collect: amount
  - collect: recipient
  - collect: account
  - action: action_process_transfer
```
 
Rasa walks the list top to bottom in search of missing values. If a slot already has a value when its step is reached, that step is skipped. The action runs only after all slots have values.