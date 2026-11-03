Reading three slots works the same way as reading one. Call `tracker.get_slot()` once per slot inside `run()`.
 
```python
account = tracker.get_slot("account") or ""
amount = tracker.get_slot("amount") or ""
recipient = (tracker.get_slot("recipient") or "")
```
 
