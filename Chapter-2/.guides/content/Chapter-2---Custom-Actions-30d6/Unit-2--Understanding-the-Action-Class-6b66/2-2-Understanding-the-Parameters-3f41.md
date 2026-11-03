
`run()` always receives the same three arguments from Rasa:
 
**dispatcher** sends messages to the user.
 
```python
dispatcher.utter_message(text="Hello!")
 
# Use a response name from the domain
dispatcher.utter_message(response="utter_greet")
 
# Send more than one message from a single action
dispatcher.utter_message(text="First message.")
dispatcher.utter_message(text="Second message.")
```
 
**tracker** is the state tracker.
 
```python
# Read a slot value
account_number = tracker.get_slot("account_number")
 
# Read the latest message the user sent
user_message = tracker.latest_message.text
```
 
**domain** is the bot's domain.
 
```python
responses = domain.get("responses", {})
```
 
---