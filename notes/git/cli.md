### Git Command Line Utility

This document provides a general reference for common tasks using the Git Command-line Interface (CLI).

#### Initializing a Local Repository

Navigate to an existing directory, then check to see if that directory is a Git repository by running one of the Git commands, for example:

```` sh
git log # see a history of recent commit messages
````

If you see an error that says *"fatal: Not a git repository (or any of the parent directories): .git"*, then you first need to initialize a new repository in this directory:

```` sh
git init . # initialize a new git repository, creating a hidden folder called .git in your project's root directory
````

#### Committing Changes

A general iterative workflow to commit your changes is as follows...

Detect changes:

```` sh
git status # see what files have changed since the last version
git diff # see how those files have changed (only shows diffs for files that existed during the last version, not for newly created files)
````

Stage and commit changes:

```` sh
git add . # either add files individually by name, or use the . to represent all files in the repository. this "stages" the files for commit. you can undo this with `git reset`
git log # take a look at the most recent commit messages as you consider what message to apply to the upcoming commit, in case you want to maintain a consistent narrative and/or tone across related commit messages
git commit -m "my message" # saves the changes and adds a unique reference for this particular version
````

> Note: Get comfortable with these commands, because you will use them every time you commit your changes to version control! Optionally alias them by adding one or more new entries to your profile (e.g. `~/.bash_profile`). For example:
>
>     alias gd="git diff"
>     alias gs="git status"

#### Associating Local and Remote Repositories

This process can differ based on different circumstances, but these instructions assume you have created both a local repository and a remote repository.

How to associate an existing GitHub-hosted remote Git repository with an existing local Git repository:

  1. Create a new repo on GitHub, and note its clone url (either HTTPS or SSH, depending on your preference).
  2. Navigate to the root directory of your existing local repository.
  3. Configure a "remote" address for your local repository: `git remote add origin CLONE_URL`. Note: the overwhelming convention is to name your GitHub remote, "origin".
  4. One-time association of remote repo with local repo: `git pull origin master --allow-unrelated-histories` (then you'll be in a Vi window, so press "shift + ZZ" to save and exit the window).

#### Pushing Changes

Assuming you have created a remote repository on GitHub and configured your local repository with the corresponding remote address:

```` sh
git pull origin master # best practice, pull before you push in case other changes have been made to the remote repository.
git push origin master
````

After pushing, you should be able to visit your remote repository on GitHub and see your code there.
