
Until now, we've used one `collect:` step to gather a single value. The same pattern scales to multiple slots: the flow collects each value in order, stores them, and passes all of them to the action at the end.
 
```
User:  "I want to transfer money"
Agent: "How much would you like to transfer?"
User:  "50"
Agent: "Who would you like to transfer money to?"
User:  "Alice"
Agent: "What is your account number?"
User:  "1234"
Agent: "Transfer of $50 from account 1234 to Alice processed."
```
 
If the user already checked their balance earlier in the session, and `account` is already set to persist, the flow skips that question and goes straight to `amount`. This is slot persistence working across flows.