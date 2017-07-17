# CRUD Application (CSV File Datastore)

Write Python software to perform CRUD operations on an inventory of products kept in a CSV file.

> NOTE: CRUD is an acronym for "Create", "Read", "Update", and "Destroy". These operations represent the primary actions performed on database resources (i.e. records) within an information system. The "Read" operation comprises two operations: the "List" operation for reading all resources, as well as the "Show" operation for reading a single resource.

## Learning Objectives

  1. Gain familiarity with the concept of CRUD operations.
  1. Gain familiarity with the concept of program/data independence.
  1. Practice writing software in Python.
  1. Practice reading and writing CSV files in Python.
  1. Practice version control.
  1. Practice contributing to open source software.

## Prerequisites

  1. ["Shopping Cart" Project](/projects/shopping-cart/project.md)
  1. [Python `csv` Module Overview](/notes/programming-languages/python/modules/csv.md)

## Requirements

TBA:

  + reads and writes from CSV file
  + all CRUD operations:
    + List
    + Create
    + Show
    + Update
    + Destroy
  + auto-increments product ids on "Create"
  + Handles a CSV file without any product rows, but assumes presence of the expected header row
  + "Show", "Update", and "Destroy" operations should fail gracefully (display a friendly user message) if a matching product is not found
  + students are encouraged but not required to simplify duplicate code via the refactoring process
  + interface displays a greeting mentioning the user's name, displays the number of products currently in the CSV file, and informs the user of all available product operations
  + program should fail gracefully (display a friendly user message) if user inputs an invalid CRUD operation

## Instructions

### Setup

Create a new project repository on GitHub.com and note its remote clone address. Clone it to your Desktop or some other location on your local machine. Navigate into the project repository via the command line.

Create in the project repository the following files:

  + `README.md`
  + `app/products_app.py`
  + `data/.gigitnore`

In the `README.md` file, place content to identify your application and instruct someone else how to download and run it:

    # Name of Your App

    Some description or other info about what the app does.

    ## Installation

    ```shell
    git clone remote_clone_address_of_your_repo_here
    cd some/path/to/repo/
    ```

    ## Usage

    ```shell
    python app/products_app.py
    ```

In the `app/products_app.py` file, place some placeholder print statement, like `print("HELLO")`.

In the `data/.gitignore`, place the following code, which says "exclude from version control all files in this directory besides this one":

    *
    !.gitignore


Commit your changes to version control using a message like "Setup new project repo".

Finally, download [the `products.csv` file](products.csv) into your repository's `data` directory so its name is `data/products.csv`. You can achieve this by updating your local fork of the course repository and copying the file from there (recommended), or by copying the file's ["raw" contents](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-70-201706/master/projects/crud-app/products.csv) from GitHub and pasting them into a new local file (easier, and acceptable due to the small size of our file). Your application will read and write to this file, so there is a chance it may get messed up during application development. So you are encouraged to also download a redundant copy, perhaps called `products_copy.csv` into the `data` directory, to have on-hand in case you ever need to re-paste its contents into the main `products.csv` file.

After downloading the CSV file(s), you should not see them tracked in version control. If you do, make sure to configure the `data/.gitignore` file as prescribed above. Alright, you are ready to start development!

### Implementation

#### Checkpoint I - User Inputs

  1. do stuff
  1. do stuff
  1. do stuff

#### Checkpoint II - Reading and Writing to CSV File

  1. do stuff
  1. do stuff
  1. do stuff

#### Checkpoint III - CRUD Operations

  1. do stuff
  1. do stuff
  1. do stuff

#### Further Exploration - Validate Format of Prices

For students desiring optional further exploration, the program's "Create" and "Update" operations should validate the product information input by the user, displaying a helpful message (e.g. "Please input a price formatted as a number with two decimal places.") when necessary.

## Submission Instructions

Push your changes to your remote project repository on GitHub.com, and note its URL.

Update your fork of the course repository. In the [submissions.csv file](submissions.csv), add a new row including your GitHub username and the project repository's URL. The CSV file's rows should be ordered alphabetically by GitHub username. Commit your changes to your fork of the course repository and submit a Pull Request for your fork's content to be merged into the course repository. See the [Contributor's Guide](/CONTRIBUTING.md) for instructions. At this time, you are encouraged to use the Git CLI to submit your work.

## Evaluation

Full credit for presence of a Python program which runs without error, meets all requirements, and exactly or near-exactly produces the desired functionality.

Else 87.5% credit for presence of a Python program which runs without error, meets all requirements, and produces most of the desired functionality.

Else 75% credit for presence of a Python program which runs without error, meets all requirements, and produces much of the desired functionality.

Else half credit for presence of a Python program which doesn't run or doesn't meet the requirements, or doesn't produce much of the desired functionality.

Else no credit.
