# Python Language Overview

## The `os` Module

Reference: https://docs.python.org/3/library/os.html.

Use the `os` module perform command-line-style file and directory operations, and to access system environment variables.

### File Operations

```python
import os

os.listdir("/path/to/Desktop")
```

### Directory Operations

```python
import os

os.getcwd()

os.chdir("/path/to/Desktop")

os.mkdir("/path/to/Desktop/my-dir")
```

## Accessing Environment Variables

Prerequisite: follow the [Environment Variables Overview](/notes/environment-variables/notes.md) to set an environment variable called `NYU_INFO_2335`.

```python
import os

os.environ["NYU_INFO_2335"] #> SecretPassword123
```
