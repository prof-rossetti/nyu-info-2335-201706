# Python Language Overview

## File Management

Use Python to read and write file contents, as well as to create and delete files.

Reference:

 + https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
 + https://docs.python.org/3/glossary.html#term-file-object
 + https://docs.python.org/3/library/io.html#module-io
 + https://docs.python.org/3/library/os.html
 + https://www.tutorialspoint.com/python/python_files_io.htm

### Writing to File

Write content to a new file:

```python
file_name = "my_message.txt" # refers to a file path relative to the path of your your script. this example refers to a file in the same directory.

with open(file_name, 'w') as file:
    file.write("Hello World")

#> Hello World
```

Write multiple lines of content to a new file:

```python
file_name = "another_message.txt" # refers to a file path relative to the path of your your script. this example refers to a file in the same directory.

with open(file_name, 'w') as file:
    file.write("Hello World" + "\n") # NOTE: "\n" is the character that represents a new line
    for line in ["one line", "another line", "last line"]:
      file.write(line + "\n")

#> Hello World
#> one line
#> another line
#> last line
```

### Reading Files

TBA
