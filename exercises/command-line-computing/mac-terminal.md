# Command-line Computing

## Terminal (Mac OS)

Open the Terminal application.

### Current User

Print the current user's name.

```` sh
whoami
````

### Present Working Directory

Print the current/present working directory.

```` sh
pwd
````

### List Files in a Directory

List files in the current working directory.

```` sh
ls
ls -al # for a different display
````

### Navigate and Manage Directories

Change directories (specifying absolute file path).

```` sh
cd ~/Desktop
````

Make a new directory.

```` sh
mkdir my_folder
````

Remove a directory.

```` sh
rm my_folder # triggers an error
rm -rf my_folder # recursively (-r) forces (-f) removal
````

### Manage Files

Change directories (using relative file path).

```` sh
cd my_folder # first re-create this directory if it doesn't exist, else this will trigger an error
````

> FYI: Use the command `cd ..` to move "up" one directory relative to the current working directory.

Create a file.

```` sh
touch README.md
touch index.html
touch my_data.csv
touch my_message.txt
````

Remove a file.

```` sh
rm index.html
````

Edit and save a file, using a text editor like nano, atom, sublime, or vim.

```` sh
atom my_message.txt # requires "Install Shell Commands" from the Atom Settings
````

Print file contents.

```` sh
cat my_message.txt
````

Move a file.

```` sh
mv ~/Desktop/my_folder/my_message.txt ~/Desktop
````

Copy a file.

```` sh
cp ~/Desktop/my_message.txt ~/Desktop/my_folder
````

Copy contents of a file into the clipboard for pasting.

```` sh
pbcopy < ~/Desktop/my_folder/my_message.txt
# ... then just paste as you normally would after copying some text
````

### Further Exploration

There are many other utilities to use from the command-line.

First, turn up the volume on your computer, then make it speak:

```` sh
say "Hello, I am your computer. Let's be friends."
````

Optionally explore additional command-line interfaces, if you're curious.

#### Internet Computing

Trace the route traveled by a network request:

```` sh
traceroute google.com
# ... stop after a few seconds if necessary by pressing: control + c
````

Time the duration of a network request:

```` sh
ping google.com
# ... stop after a few seconds if necessary by pressing: control + c
````

Request the contents of a webpage:

```` sh
curl google.com
curl http://www.google.com
curl https://raw.githubusercontent.com/debate-watch/twenty_sixteen/master/lib/twenty_sixteen/candidates.json
````
