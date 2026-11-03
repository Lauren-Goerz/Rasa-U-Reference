
The slot type controls what kind of value the slot accepts.
 
| Type | Stores | Example values |
|---|---|---|
| `text` | Any string | `"1234"`, `"John Doe"`, `"checking"` |
| `bool` | True or false | `true`, `false` |
| `float` | Decimal number | `99.95`, `0.5` |
| `categorical` | One value from a predefined set | `"low"`, `"medium"`, `"high"` |
| `any` | Anything, including dicts | `{"balance": 123.45, "currency": "USD"}` |
 
Chapter 3 uses `text` slots only.
 
**Naming.** Use lowercase with underscores for multi-word slots. `account`, `user_name`, and `transfer_amount` are clear. `a`, `slot1`, and `data` are not.
 
---