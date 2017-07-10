# Version Control

Access this course repository from your local machine using the Git CLI.

## Prerequisites

  1. [Git Overview](/notes/git/notes.md)
  1. [Git Command-line Overview](/notes/git/cli.md)
  1. ["Human Software" Project](/projects/human-software/project.md)

## Objectives

  1. Familiarize yourself with fundamental concepts of document version control.
  1. Learn the Git version control system.
  1. Install, and practice using, the Git CLI.

## Instructions

Install the Git CLI, then use it to access your fork of the course repository.

### Install Git CLI

First, check to see if Git is already installed on your machine:

```` sh
# Mac Terminal:
which git

# Windows Command Prompt:
where git
````

If it is not installed, follow the OS-specific instructions below to install it:

  + [Installing Git CLI on Mac OS](mac-install-git.md)
  + [Installing Git CLI on Windows OS](windows-install-git.md)

If it is installed, you should be able to run `git` from the command-line.

### Access Course Repository

Assuming you have already forked the course repository during the "Human Software" project, once you have installed Git, you should be able to clone your fork to your local machine. For instructions, reference the ["Git CLI" section of the Contributor's Guide](/CONTRIBUTING.md#via-git-cli).







<hr>

## Extra Practice

Complete one or more of the following tutorials as desired:

  + [Git Tutorial](https://try.github.io/)
  + [Intro to GitHub](https://services.github.com/on-demand/intro-to-github/)
  + Git Client Tutorials:
    + [Intro to GitHub Desktop](https://services.github.com/on-demand/github-desktop/)
    + [Intro to GitHub CLI](https://services.github.com/on-demand/github-cli/)

Reference also this [Git CLI Overview](/notes/git/cli.md).

After participating in these tutorials and practicing on your own, you should be able to:

  + Initialize a new Git repository.
  + Review, stage, and commit file changes.
  + Configure remote repositories, link them to local repositories, and push and pull (sync) them.
  + Checkout a branch, commit changes to that branch, push to remote branch, and merge branches.
