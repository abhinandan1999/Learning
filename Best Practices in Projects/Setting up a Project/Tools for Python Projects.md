# Tools to Improve Python Project
## BLACK - Format the python codes according to PEP8 guidelines

### 1. black 
#### Install black
```
pip install black
```

#### Utility commands of black
Format the code according to PEP8 Guidlines
```
black <src-folder-name>
```

Show the file to be formatted but will not format the code
```
black --check --diff <filename.py>
```

By default black allows only 88 characters for its length, to change to any other length (let's say 60), we use this command
```
black -l 60 <filename.py>
``` 

### 2. Black for .ipynb files
#### Install Blackcellmagic
```
pip install blackcellmagic
```

#### Utility commands of blackcellmagic
Load the extension in the first cell of notebook
```
%load_ext blackcellmagic
```

To format the cell according to PEP8 guidlines use magic command at start of cell
```
%% black
```

### 3. code format .ipynb file according to PEP8 guidelines using command line
#### Install jupyterblack
```
pip install jupyterblack
```

#### Utility commands of jupyterblack
To format the .ipynb file run the command
```
jblack </path/to/.ipynb/file>
```

## ISORT - Sort the import in python according to PEP8 guidelines

### 1. isort
#### Install isort
```
pip install isort
```

#### Utility commands for isort
To use isort on .py files
```
isort <filename1.py><filename2.py>
```

Recursively sort the imports of <.py> file in current directory
```
isort .
```

Shows the proposed changes without applying them
```
isort <filename.py> --diff
```

## Pydocstyle - It is a static analysis tool for checking compliance with Python docstring conventions as per PEP 257.

### 1. pydocstyle
#### Install pydocstyle
```
pip install pydocstyle
```

#### Utility commands for pydocstyle
To run pydocstyle check on .py file for any compliance break from PEP 257
```
pydocstyle --convention=[google, pep257, numpy] <filename.py>
```

## Flake8 - To check the quality and style of python code.

### 1. flake8
#### Install flake8
```
pip install flake8
```

#### Utility commands for flake8
To run flake8 checks on a .py file
```
flake8 <filename.py>
```

To run flake8 for specified error codes use it with --select argument
```
flake8 --select=F401,E501 <filename.py>
```

Example of flake8 error Codes
1. E/W Codes (from pycodestyle):
    E: Errors (for PEP 8 style violations).
    W: Warnings (for less severe style issues).

    Examples:
    * E501: Line too long (character limit).
    * E302: Expected 2 blank lines, found 1.
    * W291: Trailing whitespace.

2. F Codes (from PyFlakes):
    F: Errors related to potential bugs or logical issues in the code, such as undefined or unused variables, and imports.

    Examples:
    * F401: Module imported but unused.
    * F821: Undefined name (variable or function used without being defined).
    * F841: Local variable assigned but never used.

3. C Codes (from McCabe Complexity):
    C: Cyclomatic complexity-related warnings, showing where functions are too complex.

    Example:
    * C901: Function is too complex.

4. B Codes (from flake8-bugbear):
    B: Finds common bugs and bad practices in Python code.

    Examples:
    * B001: Unused loop control variable.
    * B008: Do not perform function call in default arguments (may cause unexpected behavior).
    * D Codes (from flake8-docstrings, if installed):
    * D: Docstring-related checks (for PEP 257 compliance).

    Examples:
    * D100: Missing docstring in public module.
    * D102: Missing docstring in public method.
 
 ### autoflake
 #### Install autoflake
 ```
 pip install autoflake
 ```

 #### Utility commands for autoflake
 To cleanup a single file and remove unused imports
 ```
 autoflake --in-place <filename.py>
 ```

 To remove unused variables as well as imports
 ```
 autoflake --in-place --remove-unused-variables <filename.py>
 ```

## MYPY - [TODO]

## BANDIT - [TODO]

## POETRY - [TODO]

## Jupyter notebook

## Jupyter lab

## NBQA - [TODO]



