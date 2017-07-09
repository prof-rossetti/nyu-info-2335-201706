# Installing Ruby

First, check to see if Ruby is already installed on your machine:

```shell
# Mac Terminal:
which ruby

# Windows Command Prompt:
where ruby
```

If Ruby is not installed, follow the OS-specific instructions below to install it.

Once Ruby is installed, you should be able to run `irb` and `gem` from the command-line. And after following the instructions below, you should also be able to run `bundle` from the command line. Additionally, you should be able to check the versions of each:

```shell
ruby --version #> ruby 2.2.3p173 (2015-08-18 revision 51636) [x86_64-darwin15]
gem --version #> 2.4.5.1
bundle --version #> Bundler version 1.13.6
```

> FYI: `irb` stands for "interactive ruby"

For more information about `bundler`, see the [Package Management](package-management.md) overview.

## Windows OS

Download Ruby from the [Ruby website](https://www.ruby-lang.org/en/downloads/).

## Mac OS

You may download Ruby from the [Ruby website](https://www.ruby-lang.org/en/downloads/), however you are encouraged to use the [Homebrew](https://brew.sh/) package manager to install it via one of two ways:

  1. Direct Installation (for students)
  2. Managed Installation (for professionals, if you think you may at some time be working on multiple ruby projects that require different versions)

First, check to see if Homebrew is installed:

```shell
which brew
```

Install Homebrew if necessary:

```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### A) Direct Installation

Reference: https://www.ruby-lang.org/en/documentation/installation/#homebrew.

Use Homebrew to install Ruby:

```shell
brew install ruby
```

### B) Managed Installation

Reference:   

  + https://www.ruby-lang.org/en/documentation/installation/#rbenv
  + https://github.com/rbenv/rbenv#homebrew-on-mac-os-x

Use Homebrew to install a Ruby version manager called [`rbenv`](https://github.com/rbenv/rbenv#homebrew-on-mac-os-x), then use the version manager to install and manage various ruby versions.

First check to see if `rbenv` is installed:

```shell
which rbenv #> /usr/local/bin/rbenv
```

Install `rbenv` unless it is already installed:

```shell
brew install rbenv
rbenv init
```

Use `rbenv` to install a specific version:

```shell
rbenv install 2.4.1
```

Check the version you are using:

```shell
rbenv version
```
