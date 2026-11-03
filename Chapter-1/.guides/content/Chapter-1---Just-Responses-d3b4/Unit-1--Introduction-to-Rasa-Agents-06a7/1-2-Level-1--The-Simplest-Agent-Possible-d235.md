The goal of this level (1 of 6 in the developer foundations course) is to build the simplest agent possible. 

We will start by getting to know the **domain file** (`domain/basics.yml`) is the agent's knowledge base. It defines what the agent can say, run, and remember.
 
| Section | Used in | Purpose |
|---|---|---|
| `responses:` | Level 1 | Predefined messages |
| `actions:` | Level 2 | Custom Python code |
| `slots:` | Level 3 | Memory variables |
 
**Level 1 uses only `responses:`.** The other sections exist in the file but are empty.
 
```yaml
version: "3.1"
 
responses:
  # All predefined messages go here
 
slots:
  # Level 3 — empty for now
 
actions:
  # Level 2 — empty for now
```
