# Level 4 - Multiple Slots: Codio Sync

This folder mirrors the Level 4 content from `level4/` (unit content and lab content) so it can be synced to Codio the same way as Level 3 (Slot Collection).

**Pedagogy:** Level 4 content assumes students **extend the baseline banking agent** under `level4/` (see Unit 0.1 / Unit 0.2 in the guides).

## Structure

- **Chapter:** Level-4---Multiple-Slots-e5f6
- **Units:** Unit 0 (Recap - What you built in Level 3) through Unit 6 (Summary and Next Steps) — 7 units total. Folder names are **Unit-0--** through **Unit-6--** so the table of contents shows in order. **Unit 0** has **0.1** (Your Level 3 agent), **0.2** (What Level 4 adds — includes full Level 3 → 1.4 checklist), and **Lab 0.1** (pipeline: fill-in-the-blanks + paste `config.yml` / `endpoints.yml` + code test). Unit 1 has four pages (1.1–1.4, including Test Your Knowledge); Unit 6 has seven pages (6.1–6.7, including Knowledge Check, Limitations, Level 5 Preview, Course Completion Checklist).
- **Labs:** Lab 0.1 (pipeline), Lab 2.1 (domain), Lab 3.1 (action), Lab 4.1 (flow), Lab 5.1 (training), Lab 5.2 (completion check + optional Inspector testing — no separate Unit 5 “5.1” or “5.2” concept pages)

Each unit has an `index.json` (section title and order of pages) and each page has a content file and a `.json` (page metadata: title, type page, contentType markdown).

**Page order and naming:** Section `order` arrays list pages in teaching order (concept pages before labs where applicable). Content filenames use a **`U-M-`** prefix matching **unit** `U` and subsection `M` (e.g. Unit 2 → `2-1-…`, `Lab-2-1-…`). **Unit 5** has only **`Lab-5-1-…`** (training) and **`Lab-5-2-…`** (completion check + Inspector instructions); there are no separate `5-1` or `5-2` concept pages. Avoid reusing the next unit’s index (e.g. `6-1` under Unit 5).

**File tree:** Every **page** `.json` uses **`layout`: `2-panels-tree-guides-left`**, **`files`** (open panel 1), and **`path`: [`level4`]** so the workspace tree opens on the **`level4`** folder for all Level 4 pages (Units 0–6).

**Terminal:** Pages whose markdown expects CLI use (training, Inspector, `cd level4`, **Check It!** code assessments, etc.) also set **`files`** to open **`#terminal`** on **panel 1** (right-hand stack with guide on the left). Repo script: `.guides/scripts/patch_guide_terminal_panels.py` (run from project root after adding lab/training pages).

**IDs must be unique across the whole guide.** Level 4 section and page ids use an `e5f6` suffix so they do not collide with Level 3 (which shares similar unit names and previously caused the TOC to merge or show wrong content). Do not reuse section or page ids from Level 3 when adding or editing Level 4 content.

## Root index

The main guide index at `.guides/content/index.json` includes `Level-4---Multiple-Slots-e5f6` in its `order` array so this chapter appears after Level 3 when the project is loaded or re-imported from Git in Codio.

## Assessments

Graders and solution references live in `.guides/secure/level4_graders/` (lab_0.1_grader.py, lab_2.1_grader.py, lab_3.1_grader.py, lab_4.1_grader.py, lab_5.1_grader.py, lab_5.2_grader.py and corresponding solution_reference.md files). Assessment JSONs live in `.guides/assessments/` (e.g. **Lab 0.1** uses `fill-in-the-blanks-401010010` then `code-output-compare-401010001`; **Lab 3.1** uses `fill-in-the-blanks-401030010` then `code-output-compare-401030001`). Fill-in-the-blanks `tokens.text` uses the same pattern as the slot-action lab (`fill-in-the-blanks-2346557111.json`): literal `0` for each blank (sequential), not `0..n` indices. Configure each lab in Codio using the **assessment setup materials** under `level4/` (Option A: LLM Rubric, Option B: Standard Code Test with substring match for PASS).

## Re-import from Git

To refresh the guide in Codio (including Level 4), re-import or update the project from Git so Codio loads the current `.guides/content/` tree.
