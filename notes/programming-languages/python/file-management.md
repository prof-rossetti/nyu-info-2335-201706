# Python Language Overview

## File Management

Use Python to read and write file contents, as well as to create and delete files.

Reference:

 + https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
 + https://docs.python.org/3/glossary.html#term-file-object
 + https://docs.python.org/3/library/io.html#module-io
 + https://www.tutorialspoint.com/python/python_files_io.htm

See also: [the `csv` module](../modules/csv.md) for reading and writing CSV files, and [the `os` module](../modules/os.md) for command-line-style file operations and functionality to help specify file paths.

### Reading Files

To setup these examples, create a new directory on your Desktop called `file-mgmt` and navigate there from your command line. Create two new files called `my_message.txt` and `my_script.py` and place in the following contents, respectively:

    Hello World.

    ...

    Goodbye.

```python
file_name = "my_message.txt" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "r") as file: # NOTE: "r" means "open the file for reading"
    contents = file.read()
    print(contents)

#> Hello World.
#>
#> ...
#>
#> Goodbye World.
```

### Writing Files

Write content to file:

```python
file_name = "new_message.txt" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "w") as file: # NOTE: "w" means "open the file for writing"
    file.write("Hello World")

#> Hello World
```

You can write multiple lines of content to a new file:

```python
file_name = "longer_message.txt" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "w") as file:
    file.write("Hello World" + "\n") # NOTE: "\n" is the character that represents a new line
    for line in ["one line", "another line", "last line"]:
        file.write(line + "\n")

#> Hello World
#> one line
#> another line
#> last line
```
