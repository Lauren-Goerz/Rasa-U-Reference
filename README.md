# Rasa University

Hands-on curriculum for building conversational AI agents with [Rasa](https://rasa.com). Learners work through six chapters on a single banking assistant—from static responses to sub-agents that reason and act autonomously.

**Repository:** [github.com/RasaHQ/Rasa-University](https://github.com/RasaHQ/Rasa-University)
**Video Intro:** - [🎥 Codio/Github/Webflow setup](https://drive.google.com/file/d/1I-Vzb2ydcDEKSxhUsvc6rztIbLYtHIVS/view?usp=sharing)

## Curriculum

Work through the chapters in order. Each folder is a self-contained [Codio](https://www.codio.com/) assignment with guided content, labs, and graders.

| Order | Folder | Codio module | Topic |
|------:|--------|--------------|-------|
| 0 | [`Setup-and-Install/`](Setup-and-Install/) | Setup & Install | Virtual environment, Rasa install, developer license |
| 1 | [`Chapter-1/`](Chapter-1/) | Chapter 1 | Just Responses — flows, domain, configuration |
| 2 | [`Chapter-2/`](Chapter-2/) | Chapter 2 | Custom Actions — Python actions, APIs |
| 3 | [`Chapter-3/`](Chapter-3/) | Chapter 3 | Slot Collection — conversational memory |
| 4 | [`Chapter-4/`](Chapter-4/) | Chapter 4 | Multiple Slots — branching flows |
| 5 | [`Chapter-5/`](Chapter-5/) | Chapter 5 | Enterprise Search (RAG) |
| 6 | [`Chapter-6/`](Chapter-6/) | Chapter 6 | Sub-Agents — MCP, autonomous dialogue |

Estimated total time: **~4 hours**.

## Repository layout

This repo is a **monorepo**: one GitHub project, one folder per Codio assignment.

```
Rasa-University/                 ← GitHub only (not copied into Codio boxes)
├── README.md                    ← GitHub only
├── docs/                        ← GitHub only (maintainer docs)
├── scripts/                     ← GitHub only (optional helpers)
├── Setup-and-Install/           ← maps to Codio “Setup & Install”
└── Chapter-1/ … Chapter-6/      ← maps to Codio Chapters 1–6
    ├── .codio
    ├── .guides/
    └── chapterN/                ← Rasa project (name varies by level)
```

**GitHub:** each module lives in its own folder (`Chapter-1/`, etc.).

**Codio:** each assignment’s workspace root contains **that folder’s contents** (`.codio`, `.guides/`, `chapterN/` at `/home/codio/workspace/`). Students do **not** see the monorepo layout, and this root `README.md` is **not** deployed to Codio.

## Prerequisites

- [Rasa Developer Edition license](https://hellorasa.info/3PpvQsT) (free)
- **OpenAI API key** — required for Chapters 5 and 6 (configure during setup)

## Edit on your machine (source of truth)

Clone the repo and push changes to GitHub. Only add the folder you changed—never `git add .` unless you mean to commit everything.

```bash
git clone git@github.com:RasaHQ/Rasa-University.git
cd Rasa-University

# Example: edit Chapter 1
git add Chapter-1/
git commit -m "Update Chapter 1 lab wording"
git push origin main
```

HTTPS remote:

```bash
git remote set-url origin https://github.com/RasaHQ/Rasa-University.git
```

## Codio sync

The **Rasa University** course on Codio has one assignment per row in the curriculum table. Each assignment pulls from the matching GitHub folder.

### Rules

1. **Edit and push on your laptop** (in `Setup-and-Install/` or `Chapter-N/`).
2. **Pull in Codio** in the matching assignment only (commands below).
3. **Do not `git push` from Codio** — a box only holds one module at workspace root; pushing could damage the monorepo on GitHub.
4. **Do not put this README in Codio** — sync removes `README.md` from the workspace on purpose.
5. After pulling in Codio, click **Publish** so students see updates.

### One-time: SSH access (per Codio account)

1. Codio → **username → Preferences → Applications** → connect GitHub / upload public key.
2. Add the Codio **public** SSH key as a [deploy key](https://github.com/RasaHQ/Rasa-University/settings/keys) on this repo (read-only is enough).
3. In any assignment terminal: `ssh -T git@github.com` → should greet you successfully.

See [Codio: Connect to GitHub](https://docs.codio.com/common/settings/github.html).

### One-time: Git remote (per Codio assignment)

Open the assignment → **Tools → Terminal** (`codio@...`, not your Mac):

```bash
cd ~/workspace
mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts 2>/dev/null
chmod 600 ~/.ssh/known_hosts

git init 2>/dev/null || true
git remote add origin git@github.com:RasaHQ/Rasa-University.git 2>/dev/null || \
  git remote set-url origin git@github.com:RasaHQ/Rasa-University.git
git fetch origin
```

### Pull GitHub → Codio (run in each assignment)

Change `CHAPTER_DIR` to match **this** assignment, then run in **that** assignment’s Codio terminal:

| Codio assignment | `export CHAPTER_DIR=` |
|------------------|------------------------|
| Setup & Install | `Setup-and-Install` |
| Chapter 1 | `Chapter-1` |
| Chapter 2 | `Chapter-2` |
| Chapter 3 | `Chapter-3` |
| Chapter 4 | `Chapter-4` |
| Chapter 5 | `Chapter-5` |
| Chapter 6 | `Chapter-6` |

```bash
cd ~/workspace
export CHAPTER_DIR=Chapter-1   # ← change per assignment

git fetch origin
git checkout origin/main -- "$CHAPTER_DIR/"
cp -a "$CHAPTER_DIR"/. .

# Remove monorepo paths from workspace only (README stays on GitHub)
rm -rf Chapter-1 Chapter-2 Chapter-3 Chapter-4 Chapter-5 Chapter-6 Setup-and-Install README.md 2>/dev/null

git add -A
git commit -m "Sync from GitHub $CHAPTER_DIR" || true
```

Then **Publish** the assignment in Codio.

**Expected workspace after sync (examples):**

- Setup: `.codio`, `.guides/` — no `chapterN/`
- Chapter 1: `.codio`, `.guides/`, `chapter1/`
- Chapter 5: `.codio`, `.guides/`, `chapter5/`, plus `tools/` / `secure/` if present in that folder

More detail: [docs/CODIO_SYNC.md](docs/CODIO_SYNC.md) · helper script: [scripts/codio-pull-chapter.sh](scripts/codio-pull-chapter.sh)

## Learn more

- [Rasa documentation](https://rasa.com/docs/)
- [Codio documentation](https://docs.codio.com/index.html)
- [🎥 See a video overview of Codio/Github/Webflow setup](https://drive.google.com/file/d/1I-Vzb2ydcDEKSxhUsvc6rztIbLYtHIVS/view?usp=sharing)

---

Maintained by [Rasa](https://rasa.com) · [RasaHQ on GitHub](https://github.com/RasaHQ)
