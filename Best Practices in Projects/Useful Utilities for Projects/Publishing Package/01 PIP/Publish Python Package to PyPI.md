
### Rules of Python Packaging

The moost important documents that define how Python packaging works are the following PEPs:

- PEP 427 describes how wheels should be packaged.
- PEP 440 describes how version numbers should be parsed.
- PEP 508 describes how dependencies should be specified.
- PEP 517 describes how a build backend should work.
- PEP 518 describes how a build system should be specified.
- PEP 621 describes how project metadata should be written.
- PEP 660 describes how editable installs should be performed.

### Freeze the dependencies using pip
```
python -m pip install pip-tools
pip-compile pyproject.toml # Outputs requirements.txt
```

### Install dependencies
```
python -m pip install -r requirements.txt
```

### Install Optional Dependencies
```
pip-compile --extra dev pyproject.toml # Outputs requirements.txt
```

### Install the package
Note: To install the package specify the name and version in pyproject.toml
```
python -m pip install -e .
```
Note: The -e flag installs the package in editable mode, which means that the package will be reinstalled if you make changes to the source code.

### Run the package
```
[project.scripts]
realpython = "reader.__main__:main"
```

```
realpython
python -m reader
```

### Publish the package
Note: To publish the package to PyPI, you need to have a PyPI account.
To publish to TestPyPI, you need to have a TestPyPI account.

Steps Involved:
1. Install the dependencies
```
python -m pip install build twine
```

2. Build the package using tools like build
```
python -m build
```

3. Validate the package
```
cd dist/
unzip realpython_reader-1.0.0-py3-none-any.whl -d reader-whl
tree reader-whl/ # Install tree if not installed
```

Can also be validated by twine
```
twine check dist/*
```

4. Upload the package using twine
```
twine upload -r testpypi dist/* # Upload to TestPyPI
twine upload -r pypi dist/* # Upload to PyPI
```


