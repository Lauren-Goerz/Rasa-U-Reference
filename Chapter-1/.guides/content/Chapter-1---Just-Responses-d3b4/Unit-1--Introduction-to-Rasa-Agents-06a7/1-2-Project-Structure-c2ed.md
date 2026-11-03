The file tree below and to the left shows the **starter** Chapter 1 agent before any labs. As you progress, you will add flows, responses, and eventually actions and sub-agents.
 
```text
chapter1/
├── data/
│   ├── basics/         # User-facing flows
│   │   ├── greet.yml
│   │   ├── help.yml
│   │   └── contact.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml  # Session start, completed, etc.
├── domain/
│   └── basics.yml      # Agent knowledge base (responses)
├── config.yml          # How to build the agent (pipeline, LLMs, policies)
├── credentials.yml     # How to connect (REST, Socket.IO)
├── endpoints.yml       # Where to find actions/LLMs
├── logs/               # Generated when running Inspector
└── models/             # Generated during training (don't edit)
```
 
After `rasa train`, a packaged model appears under `models/`.
 
**How the files connect**
 
```text
User sends message
  ↓
config.yml        (how to process it)
  ↓
data/*.yml        (flows decide what to do)
  ↓
domain/basics.yml (responses define what to say)
  ↓
Agent responds
```
 
| Relationship | Details |
|---|---|
| Flows → Responses | Flows in `data/` reference responses defined in `domain/` |
| Config → Everything | `config.yml` tells Rasa how to process messages |
| System patterns → Lifecycle | `patterns.yml` controls session start, flow completion, and error handling |
 
{Check It!|assessment}(multiple-choice-2989489112)

