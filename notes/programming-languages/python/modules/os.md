# Python Language Overview

### The `os` Module

Reference: https://docs.python.org/3/library/os.html.

Use the `os` module perform command-line-style file and directory operations, and to access system environment variables.

## File Operations

```python
import os

```

## Directory Operations

```python
import os

```

## Environment Variables

Some applications require private authentication-related variables such as passwords, API keys, and secret tokens. Hard-coding these values into software would be irresponsible from a security standpoint. So we instead store these secret values in "environment variables". Environment variables are defined in your "profile", which is a hidden file on your local machine, the path of which differs based on operating system. On Mac OS, a common profile is the `~/.bash_profile`. On Windows OS, ____________.

First edit your profile to include an environment variable called "NYU_INFO_2335".

```shell
# Mac Terminal:
echo export NYU_INFO_2335="SecretPassword123" >> ~/.bash_profile
# ...OR...
atom ~/.bash_profile # then paste inside... export NYU_INFO_2335="SecretPassword123"

# Windows Command Prompt:

```

Exit and re-open your command-line application for the changes to take affect. You will know it worked if you can access the environment variable from the command-line:

```shell
# Mac Terminal:
echo $NYU_INFO_2335 #> SecretPassword123

# Windows Command Prompt:

```


Finally, use Python to access the environment variable:

```python
import os

os.environ["NYU_INFO_2335"] #> SecretPassword123
```
