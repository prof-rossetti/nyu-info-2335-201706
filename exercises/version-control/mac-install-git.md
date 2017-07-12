# Version Control: Installing Git on Mac OS

## Download Git

You may download Git CLI from the [Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_mac), but you are encouraged to use the [Homebrew](https://brew.sh/) package manager to install it.

Check to see if Homebrew is installed:

```` sh
which brew
````

Install Homebrew if necessary:

```` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

Install Git and follow any post-installation instructions:

```` sh
brew install git
````

## Configure Git

After downloading, configure your Git installation:

```` sh
git config --global user.name "Your Name"
git config --global user.email your_name@example.com

git config --global core.editor atom # optional, if Atom is your text editor of choice, to instruct Git to use Atom when asking you to edit various text files.
````
