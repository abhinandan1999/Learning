## Tools to Improve Python Project

### 1. BLACK - 
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

### 3. Format .ipynb file using command line
#### Install jupyterblack
```
pip install jupyterblack
```

#### Utility commands of jupyterblack
To format the .ipynb file run the command
```
jblack </path/to/.ipynb/file>
```

