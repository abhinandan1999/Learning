# PIP: Python Install Package

`pip` = Python’s package manager. Used to install, upgrade, remove, and manage Python packages.  

---

## Installing Packages
```bash
pip install <package>
```

**Options:**
- `==1.2.3` → install specific version  
- `>=1.0,<2.0` → install version range  
- `--upgrade` / `-U` → upgrade to latest version  
- `--pre` → allow pre-releases  
- `--force-reinstall` → reinstall even if already installed  
- `--no-deps` → install without dependencies  
- `-r requirements.txt` → install from requirements file  
- `--index-url <url>` → use custom package index  
- `--extra-index-url <url>` → add extra package index  

**Examples:**
```bash
pip install requests==2.31.0
pip install "requests>=2.20,<2.30"
pip install --upgrade/U requests
pip install numpy --pre
pip install --force-reinstall requests
pip install pandas --no-deps
pip install -r requirements.txt
pip install requests --index-url https://pypi.org/simple
pip install private-lib --extra-index-url https://mycompany.com/pypi/simple
```

---

## Uninstalling Packages
```bash
pip uninstall <package>
```

**Options:**
- `-y` → confirm uninstall automatically  

**Example:**
```bash
pip uninstall requests -y
```

---

## Listing Installed Packages
```bash
pip list
```

**Options:**
- `--outdated` → show outdated packages  
- `--uptodate` → show up-to-date packages  
- `--format=columns/json/freeze` → choose output format  

**Example:**
```bash
pip list --outdated
pip list --uptodate
pip list --format=columns
pip list --format=json
pip list --format=freeze
```

---

## Show Package Details
```bash
pip show <package>
```

**Example:**
```bash
pip show pandas
```

---

## Freeze Environment
```bash
pip freeze
```

**Options:**
- Redirect to file for requirements
```bash
pip freeze > requirements.txt
```

---

## Check Dependencies
```bash
pip check
```
Reports broken or conflicting dependencies.

---

## Download Without Installing
```bash
pip download <package>
```

**Options:**
- `-d ./folder` → specify download directory  
- `--only-binary :all:` → download wheel only  

**Example:**
```bash
pip download requests
pip download requests -d ./<Directory>
pip download numpy --only-binary :all:
pip download pandas -d ./wheels --only-binary :all:
```

---

## Build Wheels
```bash
pip wheel <package>
```
Builds `.whl` files locally instead of installing.

---

## Configuration
```bash
pip config list
pip config set global.index-url https://pypi.org/simple
```

---

## Debug Information
```bash
pip debug
```
Shows pip + environment details.

---

## Extra Tool: Dependency Tree
(Not built-in, requires `pipdeptree`)
```bash
pip install pipdeptree
pipdeptree
```

---

**Preferred Way to Use:**
```bash
python -m pip install <package>
```
to ensure you’re installing into the correct Python/virtual environment.
