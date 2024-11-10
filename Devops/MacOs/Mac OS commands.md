## MACOS Commands

### Setup Homebrew
#### 1. Install xcode command line tools
Installs command line tool for mac. This includes all kind of useful stuff like C-compiler, etc.
Can also be installed from App store
```
xcode-select --install
```

#### 2. Install Homebrew
HomeBrew is an open source package manager for mac.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
*Note: HomeBrew does not automatically update itself nor any of the packages installed.*
```
brew update
brew upgrade
```

