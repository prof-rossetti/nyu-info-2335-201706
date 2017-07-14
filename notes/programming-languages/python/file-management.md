# Python Language Overview

## File Management

Use Python to read and write file contents, as well as to create and delete files.

Reference:

 + https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
 + https://docs.python.org/3/glossary.html#term-file-object
 + https://docs.python.org/3/library/io.html#module-io
 + https://www.tutorialspoint.com/python/python_files_io.htm

See also: [the `csv` module](../modules/csv.md) for reading CSV files and [the `os` module](../modules/os.md) for command-line-style file operations.

### Reading Files

First, create a file called `my_message.txt` and place inside it:

    Hello World.

    ...

    Goodbye.

```python
file_name = "my_message.txt" # refers to a file path relative to the path of your your script. this example refers to a file in the same directory.

with open(file_name, "r") as file:
    contents = file.read()
    print(type(contents))
    print(contents)

#> Hello World.
#>
#> ...
#>
#> Goodbye World.
```

### Writing Files

Write content to a new file:

```python
file_name = "my_message.txt" # refers to a file path relative to the path of your your script. this example refers to a file in the same directory.

with open(file_name, "w") as file:
    file.write("Hello World")

#> Hello World
```

Write multiple lines of content to a new file:

```python
file_name = "another_message.txt" # refers to a file path relative to the path of your your script. this example refers to a file in the same directory.

with open(file_name, "w") as file:
    file.write("Hello World" + "\n") # NOTE: "\n" is the character that represents a new line
    for line in ["one line", "another line", "last line"]:
        file.write(line + "\n")

#> Hello World
#> one line
#> another line
#> last line
```
