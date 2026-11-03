The **domain file** is a Rasa agent's knowledge base. It defines everything the agent "knows":
- What it can **say** (responses)
- What code it can **run** (actions) - introduced in Chapter 2
- What it can **remember** (slots) - introduced in Chapter 3

**File Location**: `domain/basics.yml`

**Analogy**: The domain is like a dictionary that defines all the words (responses) the agent can use.

#### Domain Structure

The domain file has three main sections (but Chapter 1 only uses `responses:`):

```yaml
version: "3.1"        # Rasa YAML schema version (always "3.1")

responses:            # ← Chapter 1: We use this section
                      # All predefined messages go here

slots:                # ← Chapter 3: Memory variables (not used in Chapter 1)
                      # Memory variables go here

actions:              # ← Chapter 2: Names of available actions (not used in Chapter 1)
                      # Custom Python code goes in actions/
```

⚠️ **For Chapter 1**: We only use the `responses:` section. The `slots:` and `actions:` sections are empty (we'll learn about them in later chapters).

---
