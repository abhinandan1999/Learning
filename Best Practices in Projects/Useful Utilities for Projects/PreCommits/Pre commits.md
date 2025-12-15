### What are Pre Commits?
Pre commit hooks are script that are run automatically before a commit is made.

### How pre-commit works?

1. git commit
2. .pre-commit-config.yaml is read
3. Run the hooks in .pre-commit-config.yaml
4. If any hook fails, the commit is aborted

### How to install pre-commit?
Add the dependency `pre-commit` in `pyproject.toml`

### Define the hooks in .pre-commit-config.yaml
For Example to define a hook to run `black` and `isort` on the files in the repository, add the following to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local # Tells pre-commit how to install/run hooks
    hooks: # This defines the hooks to run
      - id: black # Pre-commit hook identifier
        name: black # Pre-commit display name
        entry: black # Command pre-commit executes
        language_version: python3 # Python runtime used by pre-commit
        types: [python] # File filtering done by pre-commit
        additional_dependencies: [black] # Dependencies installed inside pre-commit’s isolated venv
```

or
```yaml
repos:
  - repo: https://github.com/psf/black # Maintained by tool authors
    rev: 24.10.0 # Reproducible formatting across machines
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/pycqa/isort # Maintained by tool authors
    rev: 5.13.2 # Reproducible formatting across machines
    hooks:
      - id: isort

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml

```

And Specify the hook dependencies in `pyproject.toml`
```toml
[tool.pre-commit]
additional_dependencies = ["black"]

[tool.black]
line-length = 120
target-version = ["py39"]
skip-string-normalization = false
```

### How to initialize pre-commit?
Run `pre-commit install`
This will create a hook in `.git/hooks/pre-commit` with the content of the hooks in `.pre-commit-config.yaml`

#### Which files are checked by pre-commit?
It will be applied to all files which are staged for commit. i.e. files after `git add`
