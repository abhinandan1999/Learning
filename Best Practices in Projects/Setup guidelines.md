### Set up Virtual Environment

#### Install Pyenv
It is a python version manager
[Pyenv git repo](https://github.com/pyenv/pyenv)
```
brew install pyenv
```

#### Install pyenv-virtualenv
Plugin to manage virtual environment for python
[pyenv-virtualenv git repo](https://github.com/pyenv/pyenv-virtualenv)
```
brew install pyenv-virtualenv
```

#### Initialize pyenv and pyenv-virtualenv
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
```
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```

#### Utility functions of Pyenv
##### List the path of Pyenv installations
```
pyenv root
```

##### List all version of python which can be installed
```
pyenv install -l
```

##### Install the required version of python
```
pyenv install <version of python>
Ex: pyenv install 3.13.0
```

##### List all versions of python which are installed
```
pyenv versions
```

##### Create Virtual Environment
```
pyenv virtualenv <version of python> <vir-env name>
```

##### List all the virtual environments
```
pyenv virtualenvs
```

##### Activate the virtual environment
```
pyenv activate <vir-env-name>
```

##### Setup a .python-version file to automatically activate virtual environment as switch is made to this directory
*Note: This will create a file named .python-version that contains the name of the virtualenv. Make sure to never commit this file to git!*
```
pyenv local <vir-env name>
```

##### Deactivate Virtual Env
```
pyenv deactivate
```

##### Delete Virtual Env
```
pyenv virtualenv-delete <vir-env name>
```



