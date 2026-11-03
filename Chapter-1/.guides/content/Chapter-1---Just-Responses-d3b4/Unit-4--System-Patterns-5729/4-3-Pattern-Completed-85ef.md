`pattern_completed` runs when a flow finishes and there is nothing else to do.
 
```yaml
flows:
  pattern_completed:
    description: A flow has been completed and there is nothing else to be done
    steps:
      - noop: true
        next: END
```
 
`noop` means no operation. The agent takes no action and returns to a ready state, waiting for the next user message.
 
---