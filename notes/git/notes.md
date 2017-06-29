# Git

> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. - [Git Website](https://git-scm.com/)

Git is a command-line utility which allows us to track changes and manage different versions of the files that comprise our software projects.

Source Code: https://github.com/git/git.

Documentation: https://git-scm.com/doc.

Command Line Reference Documents (Cheat Sheets):

  + https://education.github.com/git-cheat-sheet-education.pdf
  + https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf
  + https://www.git-tower.com/blog/git-cheat-sheet/

## Git vs GitHub

Git is a command-line utility. Whereas GitHub is an online platform - a social network of sorts - where programmers create profiles and publish software projects.

> GitHub is a development platform inspired by the way you work. From open source to business, you can host and review code, manage projects, and build software alongside millions of other developers. - [GitHub website](https://github.com/)

GitHub and competitor [BitBucket](https://bitbucket.org/product) both use Git paradigms and technologies.

GitHub is **the** place to find and explore the world's leading open source code projects. It also provides robust project management features to help you collaborate with other developers.

## Tools (Clients)

You can use a number of different tools and techniques to use Git. The most efficient way is via the command line. But that requires some understanding of command-line computing. So often it's easier to start with a more user-friendly and easy-to-learn tool like one of these [Git GUI](https://git-scm.com/downloads/guis) applications. Perhaps the leading Git GUI application is [GitHub Desktop](https://desktop.github.com/), however the application can at times run into performance issues (i.e. general slowness), and does not contain all the features of the Git command line utility.

Choose the Git client that works best for you for now, while recognizing you should eventually end up using the command line.

### Git Command Line Utility

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
