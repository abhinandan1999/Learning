The `pyproject.toml` is configuration file that simplifies the process of packaging and distributing Python projects.
By unifying the Package Setup, Managing Dependencies, and Streamlining Builds.


## Three Top Level Sections of pyproject.toml
1. [build-system] - Required for packaging/building tooling (PEP 518). Declares build dependencies and backend.
2. [project] - (PEP 621) Place for Project Metadata.
3. [tool] - Tools config for tools like black, isort, pytest, etc.

### [build-system]
``` toml
[build-system]
requires = ["setuptools>61", "wheel"] # List of requirements specifiers
build-backend = "setuptools.build_meta" # import path to backend

# Optional
backend-path = ["build_backend_dir] # Rarely used
```

Note: If no [build-system] section is present, then it is assumed to be using setuptools with the default backend.
``` toml
[build-system]
requires = ["setuptools>61", "wheel"] # Default Requires
build-backend = "setuptools.build_meta:__legacy__" # Default Backend
```

### [project] (PEP 621)
```
[project]
name = "example-package"                 # required (string) - Project Distribution Name - MUST
version = "0.1.0"                        # required (string) or dynamic - Version String - MUST
description = "Short desc"               # optional (string) - One Line Description
readme = "README.md"                     # or table form (see below) - 
requires-python = ">=3.8"                # python version specifier (string) - Tools use this to determine compatibility
license = { text = "MIT" }               # or license = "MIT" (string) or table
authors = [{name = "A Name", email="a@x"}]   # list of tables
maintainers = [{name="B Name", email="b@x"}] # optional
keywords = ["cli","http"]                # array of strings - keywords are free-form search tags that help humans discover your package.
classifiers = ["Programming Language :: Python :: 3"]  # trove classifiers 
urls = { "Homepage" = "https://...", "Docs" = "https://..." } # table of strings
dependencies = ["requests>=2.0,<4.0", 'typing-extensions; python_version<"3.8"'] # Same as requirements.txt - OPTIONAL
optional-dependencies = { test = ["pytest>=7"], docs=["sphinx"] } # Additional Optional Dependencies
dynamic = ["version"]                    # list of fields computed at build time - Duty of [build-system.build-backend]

[project.readme]
file = "README.md"
content-type = "text/markdown"

[project.urls]
Homepage = "https://..."
Docs = "https://..."

# Entry points / scripts:
[project.scripts] # Optional (If defined then function must be present)
mycli = "mypkg.cli:main"

[project.gui-scripts]
my-gui = "mypkg.gui:main"

[project.entry-points."some.group"]
plugin = "some.module:Factory"
```

### [tool] - Tool specific Config
Tools put their config here
```
[tool.black]
line-length = 120

[tool.isort]
line-length = 120
```
