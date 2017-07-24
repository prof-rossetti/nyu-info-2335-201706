# Pyhon Language Overview

## Package Management

Reference: https://docs.python.org/3/installing/index.html#installing-index.

When you install Python, you also get Python's package manager, `pip`. Use `pip` to install and manage third-party Python packages.

List packages currently installed:

```shell
pip list
```

Install a package (where `my_package` is the name of the package you want to install):

```shell
pip install my_package
```

### Project-specific Package Management

You can specify and manage project-specific package dependencies by listing them in a file called `requirements.txt` in the project's root directory.

To specify a project's dependencies, first create a new `requirements.txt` file:

```shell
cd /path/to/your/project

# Mac Terminal:
touch requirements.txt

# Windows Command Prompt:
type nul > requirements.txt
```

Then revise the `requirements.txt` file. Write the name of each required Python package dependency on a new line, save the file, and exit. For example:

    ipython
    pytest
    numpy
    django
    git+https://github.com/eskerda/pybikes.git

Finally, install package dependencies, as necessary:

```shell
pip install -r requirements.txt
```
