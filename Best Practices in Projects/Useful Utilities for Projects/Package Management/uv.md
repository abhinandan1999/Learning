# UV vs PIP Command Cheat Sheet

A side-by-side comparison of **UV** (modern package manager) and **PIP** (default Python package manager).

---

## Package Management

| **Task** | **UV Command** | **PIP Command** | **Notes / Differences** |
|----------|----------------|----------------|-----------------------|
| Install package | `uv add <package>` | `pip install <package>` | `uv` updates lock file automatically; pip does not. |
| Install package in active virtual env | `uv add --active <package>` | `pip install <package>` | `uv` updates lock file automatically; pip does not. |
| Install specific version | `uv add <package>@<version>` | `pip install <package>==<version>` | Same functionality. |
| Upgrade package | `uv upgrade <package>` | `pip install --upgrade <package>` | `uv upgrade` is simpler and can upgrade all with `--all`. |
| Upgrade all packages | `uv upgrade --all` | `pip list --outdated && pip install --upgrade <package>` | `pip` requires manual chaining; `uv` is one command. |
| Remove/uninstall package | `uv remove <package>` | `pip uninstall <package>` | Both remove the package. |

---

## Information & Listing

| **Task** | **UV Command** | **PIP Command** | **Notes / Differences** |
|----------|----------------|----------------|-----------------------|
| List installed packages | `uv pip list` | `pip list` | `uv list --outdated` like `pip list --outdated`. |
| Show package info | `uv info <package>` | `pip show <package>` | Both show version, dependencies, and location. |
| Show dependency tree | `uv tree` | `pipdeptree` (external) | `uv` has built-in tree; pip needs extra tool. |

---

## Environment Management

| **Task** | **UV Command** | **PIP Command** | **Notes / Differences** |
|----------|----------------|----------------|-----------------------|
| Initialize environment | `uv init` | `python -m venv <env>` | `uv` creates env + lock file automatically. |
| Initialize environment with specific python version | `uv venv <name> --python <x.xx version of python` | Pip Does not manage version of python | `uv` creates .venv + lock file automatically in specific version of python. |
| Convert requirements.txt to uv.lock | `uv add -r requirements.txt` | None | It installs packages from requirements.txt file and create *uv.lock* |
| Sync/install from lock file/pyproject.toml | `uv sync` | `pip install -r requirements.txt` | `uv` uses lock file for reproducibility; pip uses `requirements.txt`. |
| Creates uv.lock file | `uv lock` |  | `uv` creates uv.lock file for reproducibility; pip uses `requirements.txt`. |
| Export environment | `uv export` | `pip freeze > requirements.txt` | `uv` maintains structured lock file; pip just lists installed packages. |
| Convert uv.lock file to requirements.txt | None | `uv export --no-hashes --format requirements-txt -o <filename>.txt` | It converts *uv.lock* file to *requirements.txt*

---

## Maintenance & Utilities

| **Task** | **UV Command** | **PIP Command** | **Notes / Differences** |
|----------|----------------|----------------|-----------------------|
| Clear cache | `uv cache clean` | `pip cache purge` | Both clear cached wheels/packages. |
| Clean unused packages | `uv clean` | *(manual)* | No direct `pip` equivalent. |
| Help | `uv help` | `pip help` | Both show commands and flags. |

---

## Key Takeaways
1. **`uv` is more opinionated** — it manages a lock file and reproducible installs automatically.  
2. **`pip` is lower-level** — you must manually manage versions and dependencies.  
3. **Dependency tree** is built into `uv`, whereas pip usually requires `pipdeptree`.  

---
