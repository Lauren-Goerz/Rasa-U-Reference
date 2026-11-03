Create a virtual environment in the **project root**, install Rasa at version `3.17.0`, configure `RASA_LICENSE`, and confirm everything works. Complete this before any other lab.

> **Create `.venv` in the project root** — the folder that contains every `chapter/` folder. Activate from the root, then `cd` into the chapter you are working on.

---

**1. Check Python and pip**

```bash
python --version
pip --version
```

Expect Python 3.10+ and pip. If Python is missing:

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

If pip is missing but Python is present:

```bash
python3.11 -m ensurepip --upgrade
```

**2. Create and activate the virtual environment**

Confirm you are in the project root (`pwd` should not end in `chapter1`), then:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Your prompt should show `(.venv)`.

**3. Install Rasa**

```bash
pip install --no-cache-dir rasa-pro==3.17.0
```

Takes 2–5 minutes.

**4. Create `.env` with your Rasa Developer Edition license key**

If you haven't yet, request your free Rasa Developer Edition license [here](https://hellorasa.info/3PpvQsT). 

Stay in the project root. Replace `YOUR_LICENSE_KEY` with your actual key:

```bash
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```

This creates `.env` next to `chapter1/`. The Check It! grader reads this file and never prints your key.

**5. Add your OpenAI API key**

You will need this for Chapters 5 and 6. Adding it to `.env` now keeps it out of your code and means you never have to paste it into a file again.

Replace `YOUR_OPENAI_KEY` with your actual key — it starts with `sk-`:

```bash
echo 'OPENAI_API_KEY=YOUR_OPENAI_KEY' >> .env
```

Note the `>>` — this **appends** to the file. Using `>` would overwrite your Rasa license key.

Your `.env` should now contain both lines:

```text
RASA_LICENSE=...
OPENAI_API_KEY=sk-...
```

> Never paste API keys directly into code files, and never commit `.env` to version control. It stays local and is never submitted or shared by the grader.

**6. Verify installation**

```bash
set -a
source .env
set +a
rasa --version
```

> The Check It! grader reads `.env` from the project root and never prints your key. Make sure the file exists before clicking Check It!.

{Check It!|assessment}(code-output-compare-3333363688)

