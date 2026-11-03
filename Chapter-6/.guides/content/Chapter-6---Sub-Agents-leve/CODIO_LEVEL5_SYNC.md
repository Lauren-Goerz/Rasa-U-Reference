# Level 5 - Tool Calling: Codio Sync

This folder mirrors Level 5 teaching content (aligned with **`level5/`**) for Codio sync, same pattern as Level 4.

**Pedagogy:** Level 5 content assumes students **extend the Level 4–complete agent** under **`level5/`** (see **Unit 0.1** and **Unit 0.2** in the guides).

**Student working directory:** All steps assume the agent under **`level5/`**. For training and CLI runs, activate the venv at **project root**, then **`cd level5`** before **`python -m rasa …`**. Graded labs use on-disk checks (fill-in-the-blanks and code tests read **`level5/`**); the venv is **not** required to pass Lab 2.1 file checks.

**Lab order** (Level 4 completion → Level 5 done):

1. **Lab 2.0** — Copy **`command_prompt_v3_slot_names.jinja2`** from **`level5/resources/`** to **`level5/data/prompts/`**; set **`prompt_template`** in **`config.yml`**.
2. **Lab 2.1** — Tools package (**`tools/`**, **`banking_tools.py`**).
3. **Lab 3.1** — Register **`tools:`** in **`endpoints.yml`**.
4. **Lab 4.1** — Flow, custom action, domain conditions.
5. **Lab 5.1** — Train.
6. **Lab 5.2** — Completion check.

**Graders:** **Lab 2.0** uses task **`code-output-compare-501020000`**. **Lab 5.1** and **Lab 5.2** still include a **Lab 2.0** check (prompt file + **`prompt_template`**).

**Guide page JSON (`*.json` next to each `.md`):** Pages use **`"path": ["level5"]`** (and **`"layout": "2-panels-tree-guides-left"`** where set) so the IDE tree highlights **`level5/`**, like **`level4/`** in Level 4.

## Structure

- **Chapter:** `Level-5---Tool-Calling-f9e0`
- **Units:** **Unit-0--** through **Unit-6--** (seven units). Unit 0: recap. Unit 1: introduction to tools (pages 1.1, 1.2, 1.3 quiz). Unit 6: summary track (6.1 walkthrough through 6.7 checklist).
- **Labs:** 2.0 (command prompt), 2.1 (tools folder), 3.1 (endpoints), 4.1 (flow + action), 5.1 (train), 5.2 (completion check).
- **Unit 5 sequence:** theory 5.1 → Lab 5.1 → theory 5.2 → Lab 5.2.

Each unit has an `index.json` and each page has a `.md` and `.json`. **IDs use the f9e0/L5 suffix** so they do not collide with other chapters.

## Root index

The main guide index at `.guides/content/index.json` includes `Level-5---Tool-Calling-f9e0` in its `order` array so this chapter appears after Level 4.

## Assessments

- **Task IDs:** **code-output-compare-501020000** (Lab 2.0); **fill-in-the-blanks-501020010** + **code-output-compare-501020001** (Lab 2.1); 501030001 (Lab 3.1); **fill-in-the-blanks-501040010** + **code-output-compare-501040001** (Lab 4.1); 501050001 (Lab 5.1); 501050002 (Lab 5.2). **501050001** / **501050002** graders still include a **Lab 2.0** check (prompt file + **`prompt_template`**).
- **Assessment JSONs:** `.guides/assessments/fill-in-the-blanks-501020010.json`, `fill-in-the-blanks-501040010.json`; `code-output-compare-501020000.json` through `code-output-compare-501050002.json`.
- **Graders:** `.guides/secure/level5_graders/` (lab_2.0_grader.py, lab_2.1_grader.py … lab_5.2_grader.py; lab_*_solution_reference.md for LLM Rubric).
- **Working directory:** `/home/codio/workspace`. Command uses venv Python and grader path, e.g. `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_2.1_grader.py`. Expect output contains `PASS` (substring match).

Lab 2.0 includes `{Check It!|assessment}(code-output-compare-501020000)`. Lab 2.1 includes `{Check It!|assessment}(fill-in-the-blanks-501020010)` then `{Check It!|assessment}(code-output-compare-501020001)`. Lab 4.1 includes `{Check It!|assessment}(fill-in-the-blanks-501040010)` then `{Check It!|assessment}(code-output-compare-501040001)`. Other lab pages use `{Check It!|assessment}(code-output-compare-50XXXXXX)` with the task IDs above.

## Re-import from Git

Re-import or pull the project so Codio picks up the latest `.guides/content/` tree.
