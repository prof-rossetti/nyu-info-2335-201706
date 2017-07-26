# Environment Variables

Some applications require private authentication-related variables such as passwords, API keys, and secret tokens. Hard-coding these values into software's source code would be irresponsible from a security standpoint, especially when sharing the source code online.

So instead we store these secret values in special variables called "environment variables" which are accessible by any program running on the given computer. And we reference their values from an application's source code by invoking the name of the environment variable.

If an application requires a certain set of environment variables, they need to be set on each machine which expects to run the application - this includes developer computers as well as public-facing application servers.

## Setting

Set a new environment variable called `NYU_INFO_2335`:

```shell
# Mac Terminal:
echo export NYU_INFO_2335="SecretPassword123" >> ~/.bash_profile

# Windows Command Prompt:
set NYU_INFO_2335="SecretPassword123" # or use `setx NYU_INFO_2335="SecretPassword123"` to set this variable globally
```

>NOTE: On a Mac, you should be able to see and manage environment variables within a hidden file called
`~/.bash_profile`.

After setting a new environment variable, exit and re-open your command-line application for the changes to take affect.

## Getting

You will know it worked if you can access the environment variable from the command-line:

```shell
# Mac Terminal:
echo $NYU_INFO_2335 #> SecretPassword123

# Windows Command Prompt:
echo %NYU_INFO_2335% #> SecretPassword123
```

See also: [the `os` module](/notes/programming-languages/python/modules/os.md#accessing-environment-variables) for accessing environment variables in Python.
