# Ruby Language Overview

## Package Management

When you install Ruby, you also get Ruby's native package manager, `gem`. Use `gem` to install and manage third-party Ruby packages.

List packages currently installed:

```shell
gem list
```

Install a package (where `my_package` is the name of the package you want to install):

```shell
gem install my_package
```

### Project-specific Package Management

You can specify and manage project-specific package dependencies by listing them in a file called `Gemfile` in the project's root directory. Manage this file using a gem called `bundler`.

First check to see if `bundler` is already installed:

```shell
which bundle #> /usr/local/var/rbenv/shims/bundle
```

Install `bundler` unless it is not already installed:

```shell
gem install bundler
```

To specify a project's dependencies, first initialize a new `Gemfile`:

```shell
cd /path/to/your/project
bundle init
```

Then revise the `Gemfile` file. Write the name of each required Ruby package dependency on a new line, save the file, and exit. For example:

    source "https://rubygems.org"

    gem "rails"
    gem "rspec"
    gem "pry"

Finally, install package dependencies, as necessary:

```shell
bundle install
```

After running `bundle install`, a new file called `Gemfile.lock` will reflect the current versions of all package dependencies.
