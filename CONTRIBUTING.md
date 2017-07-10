# Contributor's Guide

This document describes instructions and best practices for contributing to this repository. Fork this repository, revise content, then submit.

> NOTE: All contributors must abide by [course policies](/POLICIES.md).

> NOTE: Most files in this repository are written in a syntax called Markdown. For reference, see this [Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).

## Forking Process

Fork this repository via the GitHub.com interface to create a copy under the ownership of your own GitHub user:

![A screencast depicting a user clicking the "Fork" button at the top right of the course repository page.](/admin/forking.gif)

You should now be able to view your fork online at https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-70-201706.

## Content Revision Process

To revise content, use a Git Client of choice. Refer to the instructions below depending on which you choose.

### Via GitHub

Add or revise files using the online interface. For example:

![A screencast depicting the user creating a new file via the GitHub online interface.](/admin/revising-fork-content.gif)

### Via Git CLI

#### Configuring Remotes

Navigate to your Desktop, or some other directory where you would like to download the course repository:

```shell
# Mac OS:
cd ~/Desktop # or some other directory where you'd like to download the repository

# Windows OS:
cd C:\Users\YOUR_USERNAME\Desktop\ # where YOUR_USERNAME is the name of the user currently operating your local machine
```

Clone your fork to your local machine:

```` sh
git clone https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-70-201706.git # feel free to use the SSH version instead only if you've done this kind of thing before
cd nyu-info-2335-70-201706/
````

If this is the first time you are downloading the fork, also add a remote to track changes from the original course repository:

```` sh
git remote -v # lists all current remotes. you should see "origin" here pointing to your fork.
git remote add upstream https://github.com/prof-rossetti/nyu-info-2335-70-201706.git # or use the SSH version if you are used to doing that.
git remote -v # you should now also see an "upstream" remote pointing to the original course repository.
````

#### Updating your Fork

If the course repository has changed since you last interacted with it (most situations), update your local repository by pulling changes from the course repository:

```` sh
git branch # to see which branch you are on (if you are using branches)
git checkout master # to make sure you are on the master branch (if you are using branches)
git pull upstream master
````

If something unexpected is happening and you would like to overwrite your fork based on the current state of the upstream course repository, forcibly pull from the course repository:

```` sh
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force
````

#### Revising Content

Add or revise files using a text editor (e.g. Atom):

```` sh
atom . # this will open the directory in your text editor, allowing you to use to to edit file contents
````

Review your changes:

```` sh
git status
git diff
````

Commit the changes when you are satisfied:

```` sh
git add .
git commit -m "Some description of the changes"
````

Push the changes to your fork:

```` sh
git push origin master
````

You should now be able to view your changes reflected online in your own fork.

## Submission Process

After your fork contains the changes you'd like to be included in the course repository, create a Pull Request (PR) using the GitHub online interface. For example:

![A screencast depicting a user submitting a Pull Request via the GitHub online interface.](/admin/submitting-pull-request.gif)

In the PR message, describe what changes you made and why.

An instructor will review your PR within a timely manner. If an instructor accepts your changes, he will merge them into the course repository's master branch, at which point you should be able to view your changes reflected in the course repository.

Congratulations! :clap: Thanks! :pray:
