#!/usr/bin/env python3
"""
Lab 0.1: Create Virtual Environment and Install Rasa Pro - Grader Script
Runs from workspace root. Checks: venv in root, Rasa Pro installed, RASA_LICENSE.
"""

import json
import os
import re
import sys
import subprocess
from pathlib import Path
from typing import Optional

EXPECTED_RASA_PRO_VERSION = "3.17.0"


def _version_from_pip_list_json(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    """Machine-readable pip list; most reliable across pip/Codio layouts."""
    try:
        result = subprocess.run(
            [str(venv_python), "-m", "pip", "list", "--format=json"],
            capture_output=True, text=True, timeout=30,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None
        data = json.loads(result.stdout)
        for entry in data:
            name = (entry.get("name") or "").replace("_", "-").lower()
            if name == "rasa-pro":
                ver = (entry.get("version") or "").strip()
                if ver:
                    return ver
    except Exception:
        pass
    return None


def _version_from_dist_info_folder(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    script = r"""
import os, re, site, sys
pat = re.compile(r"(?i)^rasa[-_]pro-(.+)\.dist-info$")
candidates = []
try:
    candidates.extend(site.getsitepackages())
except Exception:
    pass
bindir = os.path.dirname(sys.executable)
candidates.append(
    os.path.join(bindir, "..", "lib", "python%d.%d" % sys.version_info[:2], "site-packages")
)
seen = set()
for raw in candidates:
    root = os.path.abspath(os.path.normpath(raw))
    if root in seen or not os.path.isdir(root):
        continue
    seen.add(root)
    try:
        for name in os.listdir(root):
            m = pat.match(name)
            if m:
                v = m.group(1).split("+", 1)[0]
                print(v)
                raise SystemExit(0)
    except OSError:
        pass
raise SystemExit(1)
"""
    try:
        result = subprocess.run(
            [str(venv_python), "-c", script],
            capture_output=True, text=True, timeout=15,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


def _normalize_version_for_compare(v: str) -> str:
    v = (v or "").strip()
    m = re.match(r"^(\d+\.\d+\.\d+)", v)
    if m:
        return m.group(1)
    return v


def _version_from_venv_dist_info_fs(workspace: Path) -> Optional[str]:
    venv = workspace / ".venv"
    if not venv.is_dir():
        return None
    pat = re.compile(r"(?i)^rasa[-_]pro-(.+)\.dist-info$")

    def _parse_metadata(meta_path: Path) -> Optional[str]:
        try:
            text = meta_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if not line.startswith("Name: "):
                continue
            n = line.split(":", 1)[1].strip().replace("_", "-").lower()
            if n != "rasa-pro":
                continue
            for j in range(i + 1, min(i + 40, len(lines))):
                if lines[j].startswith("Version: "):
                    return lines[j].split(":", 1)[1].strip().split("+", 1)[0]
        return None

    try:
        for d in venv.rglob("*.dist-info"):
            if not d.is_dir():
                continue
            m = pat.match(d.name)
            if m:
                return m.group(1).strip().split("+", 1)[0]
            mv = _parse_metadata(d / "METADATA")
            if mv:
                return mv
    except OSError:
        pass
    return None


def _version_from_pip_show(venv_python: Path, env: dict, workspace: Path, package: str) -> Optional[str]:
    try:
        result = subprocess.run(
            [str(venv_python), "-m", "pip", "show", package],
            capture_output=True, text=True, timeout=15,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if line.startswith("Version:"):
                    return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return None


def _version_from_pip_list(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            [str(venv_python), "-m", "pip", "list"],
            capture_output=True, text=True, timeout=20,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode != 0:
            return None
        for raw in result.stdout.splitlines():
            line = raw.strip()
            if not line or line.lower().startswith("package"):
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            if parts[0].replace("_", "-").lower() == "rasa-pro":
                return parts[1].strip()
    except Exception:
        pass
    return None


def _version_from_pip_freeze(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            [str(venv_python), "-m", "pip", "freeze"],
            capture_output=True, text=True, timeout=25,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode != 0:
            return None
        for raw in result.stdout.splitlines():
            line = raw.strip()
            for prefix in ("rasa-pro==", "Rasa-Pro==", "rasa_pro=="):
                if line.startswith(prefix):
                    return line.split("==", 1)[1].strip()
    except Exception:
        pass
    return None


def _version_from_importlib(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    script = (
        "from importlib.metadata import PackageNotFoundError, version\n"
        "for d in ('rasa-pro', 'rasa_pro', 'Rasa-Pro'):\n"
        "    try:\n"
        "        print(version(d))\n"
        "        break\n"
        "    except PackageNotFoundError:\n"
        "        pass\n"
        "else:\n"
        "    raise SystemExit(1)\n"
    )
    try:
        result = subprocess.run(
            [str(venv_python), "-c", script],
            capture_output=True, text=True, timeout=10,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


def _version_from_rasa_module(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            [str(venv_python), "-c", "import rasa; print(rasa.__version__)"],
            capture_output=True, text=True, timeout=10,
            cwd=str(workspace), env=env, stdin=subprocess.DEVNULL,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


def _rasa_pro_package_version(venv_python: Path, env: dict, workspace: Path) -> Optional[str]:
    v = _version_from_venv_dist_info_fs(workspace)
    if v: return v
    v = _version_from_pip_list_json(venv_python, env, workspace)
    if v: return v
    for pkg in ("rasa-pro", "rasa_pro"):
        v = _version_from_pip_show(venv_python, env, workspace, pkg)
        if v: return v
    v = _version_from_pip_list(venv_python, env, workspace)
    if v: return v
    v = _version_from_pip_freeze(venv_python, env, workspace)
    if v: return v
    v = _version_from_dist_info_folder(venv_python, env, workspace)
    if v: return v
    v = _version_from_importlib(venv_python, env, workspace)
    if v: return v
    return _version_from_rasa_module(venv_python, env, workspace)


_LICENSE_PLACEHOLDERS = frozenset({"rasaxxx-your-license-here", "your-license-here", ""})


def _license_value_is_valid(value: str) -> bool:
    v = (value or "").strip()
    return bool(v) and v.lower() not in _LICENSE_PLACEHOLDERS


def _parse_rasa_license_from_dotenv_file(env_path: Path) -> str:
    if not env_path.is_file():
        return ""
    try:
        text = env_path.read_text(encoding="utf-8")
    except OSError:
        return ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "RASA_LICENSE=" in line:
            val = line.split("RASA_LICENSE=", 1)[-1].strip()
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            return val
    return ""


# ── Setup ──────────────────────────────────────────────────────────────────
WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
VENV_DIR = WORKSPACE_ROOT / ".venv"

score = 0
max_score = 6

if (VENV_DIR / "bin" / "python").exists():
    VENV_PYTHON = (VENV_DIR / "bin" / "python").resolve()
elif (VENV_DIR / "Scripts" / "python.exe").exists():
    VENV_PYTHON = (VENV_DIR / "Scripts" / "python.exe").resolve()
else:
    VENV_PYTHON = None

print("Running Lab 0.1 Assessment Checks...")
print("")

# ── Step 1: Virtual environment (2 points) ────────────────────────────────
print("Step 1: Verifying virtual environment in project root...")
if not VENV_DIR.is_dir():
    print("❌ Step 1: FAILED - .venv not found in project root (0 points)")
    print("Hint: From the project root run 'python3.11 -m venv .venv' then 'source .venv/bin/activate'")
    print("FAIL")
    sys.exit(1)
if VENV_PYTHON is None or not VENV_PYTHON.exists():
    print("❌ Step 1: FAILED - Virtual environment incomplete (no python found) (0 points)")
    print("FAIL")
    sys.exit(1)
print("✅ Step 1: PASSED - Virtual environment found in project root (2 points)")
score += 2
print("")

try:
    subprocess.run(
        [str(VENV_PYTHON), "--version"],
        capture_output=True, text=True, timeout=5, cwd=str(WORKSPACE_ROOT),
    )
except Exception as e:
    print(f"⚠️  Warning: Could not verify venv Python: {e}")

# ── Step 2: Rasa Pro installed (3 points) ─────────────────────────────────
print("Step 2: Verifying Rasa Pro installation...")
rasa_found = False
version_info = ""

venv_bin = str(VENV_DIR / "bin")
venv_scripts = str(VENV_DIR / "Scripts")
env = os.environ.copy()
env["PATH"] = os.pathsep.join([venv_bin, venv_scripts, env.get("PATH", "")])

# Method 0: Filesystem check
for py_ver in ("3.11", "3.10", "3.9", ""):
    site_pkg = VENV_DIR / "lib" / (f"python{py_ver}" if py_ver else "site-packages") / ("site-packages" if py_ver else "")
    rasa_pkg = site_pkg / "rasa"
    if rasa_pkg.exists() and rasa_pkg.is_dir() and (rasa_pkg / "__init__.py").exists():
        version_info = "Rasa Pro (package found)"
        rasa_found = True
        break

# Method 1: pip list
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-m", "pip", "list"],
            capture_output=True, text=True, timeout=10,
            cwd=str(WORKSPACE_ROOT), env=env,
        )
        if result.returncode == 0:
            for line in result.stdout.split("\n"):
                if "rasa-pro" in line.lower() or "rasa pro" in line.lower():
                    parts = line.split()
                    if len(parts) >= 2:
                        version_info = f"Rasa Pro {parts[1]}"
                        rasa_found = True
                        break
    except Exception:
        pass

# Method 2: bash activate + rasa --version
if not rasa_found:
    try:
        activate_script = VENV_DIR / "bin" / "activate"
        if activate_script.exists():
            result = subprocess.run(
                ["bash", "-c", f"source {activate_script} && rasa --version"],
                capture_output=True, text=True, timeout=10,
                cwd=str(WORKSPACE_ROOT), env=env,
            )
            if result.returncode == 0:
                output = result.stdout or result.stderr or ""
                if "rasa" in output.lower():
                    version_info = output.strip().split("\n")[0]
                    rasa_found = True
    except Exception:
        pass

# Method 3: python -m rasa --version
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-m", "rasa", "--version"],
            capture_output=True, text=True, timeout=10,
            cwd=str(WORKSPACE_ROOT), env=env,
        )
        if result.returncode == 0 and "rasa" in (result.stdout + result.stderr).lower():
            version_info = (result.stdout or result.stderr).strip().split("\n")[0]
            rasa_found = True
    except Exception:
        pass

# Method 4: rasa binary
if not rasa_found:
    rasa_cmd = VENV_DIR / "bin" / "rasa"
    if not rasa_cmd.exists():
        rasa_cmd = VENV_DIR / "Scripts" / "rasa.exe"
    if rasa_cmd.exists():
        try:
            result = subprocess.run(
                [str(rasa_cmd), "--version"],
                capture_output=True, text=True, timeout=10,
                cwd=str(WORKSPACE_ROOT), env=env,
            )
            if result.returncode == 0 and "rasa" in (result.stdout + result.stderr).lower():
                version_info = (result.stdout or result.stderr).strip().split("\n")[0]
                rasa_found = True
        except Exception:
            pass

# Method 5: import rasa
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-c", "import rasa; print(rasa.__version__)"],
            capture_output=True, text=True, timeout=10,
            cwd=str(WORKSPACE_ROOT), env=env,
        )
        if result.returncode == 0:
            version_info = f"Rasa Pro {result.stdout.strip()}"
            rasa_found = True
    except Exception:
        pass

if rasa_found:
    rp_ver = _rasa_pro_package_version(VENV_PYTHON, env, WORKSPACE_ROOT) if VENV_PYTHON else None
    rp_cmp = _normalize_version_for_compare(rp_ver) if rp_ver else ""
    if rp_cmp != EXPECTED_RASA_PRO_VERSION:
        detail = rp_ver or "unknown"
        print(f"❌ Step 2: FAILED - rasa-pro version is {detail}; expected {EXPECTED_RASA_PRO_VERSION} (0 points)")
        print("Hint: With venv activated, run 'pip install --no-cache-dir rasa-pro==3.17.0'")
        print("FAIL")
        sys.exit(1)
    print(f"✅ Step 2: PASSED - rasa-pro {rp_ver} installed (3 points)")
    score += 3
else:
    print("❌ Step 2: FAILED - Rasa Pro not installed or not accessible (0 points)")
    print("Hint: With venv activated, run 'pip install --no-cache-dir rasa-pro==3.17.0'")
    print("FAIL")
    sys.exit(1)
print("")

# ── Step 3: RASA_LICENSE (1 point) ────────────────────────────────────────
print("Step 3: Verifying RASA_LICENSE...")
env_file = WORKSPACE_ROOT / ".env"
file_val = _parse_rasa_license_from_dotenv_file(env_file)
env_val = os.environ.get("RASA_LICENSE", "").strip()

rasa_license_ok = False
license_source = ""

if _license_value_is_valid(file_val):
    rasa_license_ok = True
    license_source = "project-root .env"
elif _license_value_is_valid(env_val):
    rasa_license_ok = True
    license_source = "environment variable"

if rasa_license_ok:
    print(f"✅ Step 3: PASSED - RASA_LICENSE is set ({license_source}) (1 point)")
    score += 1
else:
    print("❌ Step 3: FAILED - No valid RASA_LICENSE found (0 points)")
    print(
        "Hint: From the project root run:\n"
        "  echo 'RASA_LICENSE=your-actual-key' > .env\n"
        "The file must be at the project root (next to chapter1/), not inside chapter1/."
    )
print("")

# ── Summary ───────────────────────────────────────────────────────────────
print("==========================================")
if score >= max_score:
    print(f"✅ PASS: Lab 0.1 setup complete! Score: {score}/{max_score}")
    print("Summary: Step 1 (venv) | Step 2 (Rasa Pro) | Step 3 (RASA_LICENSE)")
    print(f"Score: {score}/{max_score}")
    print("Successfully passed!")
    print("==========================================")
    sys.stdout.flush()
    print("PASS")
    sys.stdout.flush()
    sys.exit(0)
else:
    print(f"❌ FAIL: Lab 0.1 setup incomplete. Score: {score}/{max_score}")
    print("Summary: Step 1 (venv) | Step 2 (Rasa Pro) | Step 3 (RASA_LICENSE)")
    print(f"Score: {score}/{max_score}")
    print("Review the failed checks above and try again.")
    print("==========================================")
    sys.stdout.flush()
    print("FAIL")
    sys.stdout.flush()
    sys.exit(1)