#!/usr/bin/env python3
"""
Lab 5.2.1: Add EnterpriseSearchPolicy - Grader Script
Checks config.yml and endpoints.yml in chapter5/.
OpenAI API key setup is verified in a later lab and is not checked here.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
CONFIG_PATH = WORKSPACE_ROOT / "chapter5" / "config.yml"
ENDPOINTS_PATH = WORKSPACE_ROOT / "chapter5" / "endpoints.yml"

score = 0
max_score = 8

print("Running Lab 5.2.1 Assessment Checks...")
print("")

# Check 1: config.yml exists (1 point)
print("Check 1: Verifying config.yml exists...")
if not CONFIG_PATH.exists():
    print("Check 1: FAILED")
    print("Hint: Make sure you are editing the config.yml inside the chapter5/ folder.")
    print("FAIL")
    sys.exit(1)
print("Check 1: PASSED")
print("config.yml found (1 point)")
score += 1
print("")

config = CONFIG_PATH.read_text(encoding="utf-8")

# Check 2: EnterpriseSearchPolicy present in config.yml (1 point)
print("Check 2: Verifying EnterpriseSearchPolicy is in config.yml...")
if re.search(r"EnterpriseSearchPolicy", config):
    print("Check 2: PASSED")
    print("EnterpriseSearchPolicy found (1 point)")
    score += 1
else:
    print("Check 2: FAILED")
    print("Hint: Add EnterpriseSearchPolicy under policies: after FlowPolicy.")
print("")

# Check 3: FAISS vector store configured (1 point)
print("Check 3: Verifying FAISS vector store is configured...")
has_faiss = re.search(r"type:\s*faiss", config)
has_source = re.search(r"source:\s*\./docs", config)
if has_faiss and has_source:
    print("Check 3: PASSED")
    print("FAISS vector store with source: ./docs found (1 point)")
    score += 1
else:
    missing = []
    if not has_faiss:
        missing.append("type: faiss")
    if not has_source:
        missing.append("source: ./docs")
    print("Check 3: FAILED")
    print(f"Missing: {missing}")
    print("Hint: Check the vector_store: block under EnterpriseSearchPolicy in config.yml.")
print("")

# Check 4: model groups referenced in config.yml (2 points)
print("Check 4: Verifying model group references in config.yml...")
has_llm_group = re.search(r"model_group:\s*openai-gpt-5-mini", config)
has_embed_group = re.search(r"model_group:\s*openai-embeddings", config)
missing_groups = []
if not has_llm_group:
    missing_groups.append("openai-gpt-5-mini under llm:")
if not has_embed_group:
    missing_groups.append("openai-embeddings under embeddings:")
if not missing_groups:
    print("Check 4: PASSED")
    print("openai-gpt-5-mini and openai-embeddings referenced (2 points)")
    score += 2
else:
    print("Check 4: FAILED")
    print(f"Missing model group references: {missing_groups}")
    print("Hint: Check that llm: and embeddings: blocks reference the correct model group ids.")
print("")

# Check 5: endpoints.yml exists (1 point)
print("Check 5: Verifying endpoints.yml exists...")
if not ENDPOINTS_PATH.exists():
    print("Check 5: FAILED")
    print("Hint: Make sure you are editing endpoints.yml inside the chapter5/ folder.")
else:
    print("Check 5: PASSED")
    print("endpoints.yml found (1 point)")
    score += 1
print("")

endpoints = ENDPOINTS_PATH.read_text(encoding="utf-8") if ENDPOINTS_PATH.exists() else ""

# Check 6: model groups defined in endpoints.yml (2 points)
print("Check 6: Verifying model groups are defined in endpoints.yml...")
has_gpt_id = re.search(r"id:\s*openai-gpt-5-mini", endpoints)
has_embed_id = re.search(r"id:\s*openai-embeddings", endpoints)
has_embed_model = re.search(r"text-embedding-3-large", endpoints)
missing_endpoint = []
if not has_gpt_id:
    missing_endpoint.append("id: openai-gpt-5-mini")
if not has_embed_id:
    missing_endpoint.append("id: openai-embeddings")
if not has_embed_model:
    missing_endpoint.append("text-embedding-3-large")
if not missing_endpoint:
    print("Check 6: PASSED")
    print("openai-gpt-5-mini and openai-embeddings model groups defined (2 points)")
    score += 2
else:
    print("Check 6: FAILED")
    print(f"Missing from endpoints.yml: {missing_endpoint}")
    print("Hint: Add both model groups to endpoints.yml. Keep the existing rasa_command_generation_model group.")
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f"PASS: Lab 5.2.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (config.yml exists) | Check 2 (EnterpriseSearchPolicy) | "
    "Check 3 (FAISS config) | Check 4 (model group references) | "
    "Check 5 (endpoints.yml exists) | Check 6 (model groups defined)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)