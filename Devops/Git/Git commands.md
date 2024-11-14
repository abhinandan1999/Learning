## Useful Git commands

### Git configuration commands
```
git config --global user.name "firstName lastName"
```
```
git config --global user.email "user@Email.com"
```

### Git Repo related commands
Initialize the repo with git functionality
```
git init
```

Get the current status of Repo
```
git status
```

### Git branch related commands
List down all the branch created locally and marks your current branch
```
git branch
```

List down all remote branches
```
git branch -a
```

Creates a branch with name "branch name" from current branch
```
git branch <branch name>
```

Checks out to "branch name"
```
git checkout <branch name>
```

Creates a branch called "new branch name" from "existing branch name" and checks out to it
```
git checkout -b <new branch name> <existing branch name>
```

Deletes the branch with name "branch name". It prevents from if commits are not merged
```
git branch -d <branch name>
```

Forcefully deletes the branch
```
git branch -D <branch name>
```

Renames the current branch to "new name"
```
git branch -m <new name>
```

To delete the branch remotely
```
git push origin --delete <branch name>
```

To push the locally created branch to remote <br>
*-u or --set-upstream*
```
git push -u origin <branch name>
```

### Commit related commands
Stage the file recursively from current directory
```
git add .
```

Commit the message with commit message
```
git commit -m <"commit message">
```

Stage and create commit files
```
git commit -am <"commit message">
```

Revert the changes which are not yet staged or committed
```
git checkout .
```

Unstage the files which are not yet committed
```
git restore --staged .
```

Undo the changes made in the latest commit but keep a record of it in history.
*This command creates a new commit that reverses the changes made in the latest commit. *
```
git revert HEAD
```

Reset the latest commit to previous commit
*Note: This will permanently delete the latest commit, so use it with caution, 
especially if you've already pushed the commit to a remote repositor*
```
git reset --hard HEAD~1
```

Rename the latest commit message
```
git commit --amend -m "New commit message"
```

Cleans the file and directory which are not added to stages or are untracked
```
git clean -fd
``` 

### Merge Related commands
Merges the "branch name" to current branch
```
git merge <branch name>
```

Squash all the commits of "branch name" into 1 commit and merge to current branch
```
git merge --squash <branch name>
```

### Pull related commands
Pull the changes from remote branch and merge to current branch
```
git pull origin <branch name>
```

Fetches data from the remote repository, updating your local copy of the remote-tracking branches
without altering your working directory or current branch.
```
git fetch origin
```

### Stash Related commands
To save the changes but not commit
```
git stash
```

To list all the stashes
```
git stash list
```

To apply the most recent stash.
```
git stash apply
```

To apply a specific stash
```
git stash apply <stash-name>
```

To delete the stash
```
git stash drop <stash-name>
```