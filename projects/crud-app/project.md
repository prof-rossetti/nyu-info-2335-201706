# CRUD Application (CSV File Datastore)

Write Python software to perform CRUD operations on an inventory of products kept in a CSV file.

> NOTE: CRUD is an acronym for "Create", "Read", "Update", and "Destroy". These operations represent the primary actions performed on resources (i.e. records) within an information system. The "Read" operation actually comprises two operations: the "List" operation for reading all resources, as well as the "Show" operation for reading a single resource.

## Learning Objectives

  1. Gain familiarity with the concept of CRUD operations.
  1. Gain familiarity with the concept of program/data independence.
  1. Practice writing software in Python.
  1. Practice reading and writing CSV files in Python.
  1. Practice version control.
  1. Practice contributing to open source software.

## Prerequisites

  1. ["Shopping Cart" Project](/projects/shopping-cart/project.md)
  1. [CRUD Overview](/notes/information-systems/crud-operations.md)
  1. [Python `csv` Module Overview](/notes/programming-languages/python/modules/csv.md)

## Instructions

### Setup

Initialize a new project repository to contain your application code. Call it whatever you want. Inside it, create a new directory called `app`. Inside of the `app` directory, place a new file called `products_app.py`.

TBA ...

### Requirements

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

### Further Exploration

#### Validate Format of Prices

For students desiring optional further exploration, the program's "Create" and "Update" operations should validate the product information input by the user, displaying a helpful message (e.g. "Please input a price formatted as a number with two decimal places.") when necessary.

## Submission Instructions

Push your project repository to GitHub.com and note its URL.

Update your fork of the course repository. In the [submissions.csv file](submissions.csv), add a new row including your GitHub username and the project repository's URL. The CSV file's rows should be ordered alphabetically by GitHub username. Commit your changes and submit a Pull Request for your content to be included in the course repository. See the [Contributor's Guide](/CONTRIBUTING.md) for instructions. At this time, you are encouraged to use the Git CLI to submit your work.

## Evaluation

Full credit for presence of a Python program which runs without error, meets all requirements, and exactly or near-exactly produces the desired functionality.

Else 87.5% credit for presence of a Python program which runs without error, meets all requirements, and produces most of the desired functionality.

Else 75% credit for presence of a Python program which runs without error, meets all requirements, and produces much of the desired functionality.

Else half credit for presence of a Python program which doesn't run or doesn't meet the requirements, or doesn't produce much of the desired functionality.

Else no credit.
