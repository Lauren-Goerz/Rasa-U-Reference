**Training** converts your flows, domain, and config into a runnable model file stored in `models/`. Until you train, Rasa has only YAML files,  it cannot run the agent. Retrain whenever you change the domain or flows.
 
When `rasa train` runs:
 
1. Reads all flows from `data/*.yml`
2. Reads the domain from `domain/*.yml`
3. Applies configuration from `config.yml`
4. Saves a timestamped model to `models/` (e.g. `20250112-120817-descent-lard.tar.gz`)
---