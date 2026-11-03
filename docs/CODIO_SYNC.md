# Syncing Codio assignments with GitHub

Each **Codio assignment** maps to **one folder** in this repo. The Codio workspace root should contain that folder’s **contents** (not the whole monorepo).

| Codio module | GitHub folder |
|--------------|---------------|
| Setup & Install | `Setup-and-Install/` |
| Chapter 1 | `Chapter-1/` |
| Chapter 2 | `Chapter-2/` |
| Chapter 3 | `Chapter-3/` |
| Chapter 4 | `Chapter-4/` |
| Chapter 5 | `Chapter-5/` |
| Chapter 6 | `Chapter-6/` |

## Golden rules

1. **Edit and push from your laptop** (or CI) in the correct subfolder — e.g. `Chapter-1/`.
2. **In Codio, only pull** using the sync script below. Do **not** run `git push` from a Codio box unless you know exactly why.
3. Pulling into Codio **does not change GitHub**. It only updates files in that one assignment’s workspace.
4. After syncing in Codio, click **Publish** so students see updates.
5. **Never run Codio pull commands from the monorepo root on your laptop.** Partial `cp` commands that copy only `.guides/` into the repo root create duplicate Chapter 5 content. Use `git pull` locally; use the full-chapter sync below only inside a Codio assignment workspace.

## One-time setup (per Codio assignment)

Open the assignment → **Tools → Terminal**:

```bash
cd ~/workspace
mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts 2>/dev/null
chmod 600 ~/.ssh/known_hosts

# Only if this box has no git yet:
git init
git remote add origin git@github.com:RasaHQ/Rasa-University.git 2>/dev/null || \
  git remote set-url origin git@github.com:RasaHQ/Rasa-University.git
git fetch origin
```

Add your Codio **public** SSH key as a deploy key on [RasaHQ/Rasa-University](https://github.com/RasaHQ/Rasa-University/settings/keys) (read-only is enough).

## Pull GitHub → Codio (safe)

Replace `Chapter-1` with the folder for **this** assignment.

```bash
cd ~/workspace
export CHAPTER_DIR=Chapter-1   # <-- change per assignment

git fetch origin
git checkout origin/main -- "$CHAPTER_DIR/"

# Copy only this chapter to workspace root (Codio layout)
if command -v rsync >/dev/null 2>&1; then
  rsync -a "$CHAPTER_DIR"/ ./ --delete
else
  cp -a "$CHAPTER_DIR"/. .
fi

# Remove monorepo folders from workspace (not from GitHub!)
rm -rf Chapter-1 Chapter-2 Chapter-3 Chapter-4 Chapter-5 Chapter-6 Setup-and-Install README.md 2>/dev/null

git add -A
git commit -m "Sync from GitHub $CHAPTER_DIR" || true
```

Then **Publish** the assignment in Codio.

### What this does / does not do

| Action | GitHub repo | This Codio box |
|--------|-------------|----------------|
| `git fetch` + `checkout` + `rsync` | Unchanged — all chapters stay | Only this assignment’s files update |
| `git push` from Codio | **Can be dangerous** — avoid | — |

## Push Codio → GitHub (avoid)

Do **not** use `git push origin main` from Codio. The box only has one chapter at workspace root; a push could try to replace the whole repo history.

**Instead:** edit on your machine:

```bash
cd /path/to/Rasa-University
# edit files under Chapter-1/
git add Chapter-1/
git commit -m "Update Chapter 1 guides"
git push origin main
```

Then run the **Pull GitHub → Codio** steps in the matching Codio assignment.

## Compare before syncing

In Codio (example Chapter 1):

```bash
git fetch origin
git diff --stat HEAD origin/main:Chapter-1/
```

No output (or only a few lines) means you are already aligned.
