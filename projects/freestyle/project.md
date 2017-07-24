# Freestyle Project

Create an information system which uses application software to satisfy your own personal or professional interests.

Preliminary example project ideas include:

  + [Social Media API Client (Twitter)](examples/twitter-api-client/project-example.md)
  + [Weather API Client](examples/weather-api-client/project-example.md)
  + [Stock Market API Client](examples/stock-market-api-client/project-example.md)
  + [Email API Client](examples/email-api-client/project-example.md)
  + Stock-trading Algorithm (building upon the Stock Market API Client)
  + Database-connected CRUD Application
  + Web-based CRUD Application
  + PDF-parsing Application
  + Natural Language Processing Application
  + Statistical Modeling Application

Optionally work in a team comprised of a small handful of students (perhaps at most three or four). Feel free to discuss ideas and find teammates in the `#freestyle` Slack channel. If there are any teams, they should be formed before the end of the project's Proposal Phase (see details below). Also note: team projects should have greater scope than individual projects, and each individual team member is still responsible for contributing a significant portion of the project's source code.

## Learning Objectives

  1. Propose and define requirements and objectives for an information system solution to a personal or professional problem or opportunity.
  1. Research and plan the information system's technology components, including third-party software packages and hardware providers, as necessary.
  1. Implement system objectives by writing software in Python.

## Prerequisites

  1. ["CRUD Application" Project](/projects/crud-application/project.md)
  1. [Software Licenses Overview](/notes/software/licensing.md)
  1. [Environment Variables Overview](/notes/programming-languages/python/modules/os.md#accessing-environment-variables) -- if your project requires secret passwords or API keys
  1. [Accessing Environment Variables using the `os` Module](/notes/programming-languages/python/modules/os.md#accessing-environment-variables) -- if your project requires secret passwords or API keys
  1. [Heroku Overview](/notes/hardware/heroku.md) -- if you'd like to run your software on a remote server

## Instructions

### Proposal Phase

Choose a project from the [list of examples](examples/), or design your own with a similar scope as the provided examples.

Define project scope and objectives, including information inputs and outputs, in a proposal form, and submit it to the professor for approval.

After reviewing your proposal, the professor may help you refine your project's focus, share helpful resources, and/or provide other guidance to help you succeed.

### Implementation Phase

After your project proposal has been approved, write software in Python to satisfy its objectives.

## Requirements

The system must transform one or more information inputs into one or more information outputs to achieve one or more stated objectives.

The system should strive to demonstrate a unique set of functionality which differentiates it in some significant way from other potential student submissions. If building upon one of the project examples, the system should also strive to differentiate itself from the example and/or add upon it in a significant way.

The system must perform its functions using software written in Python. The software's source code must meet the repository requirements below.

### Repository Requirements

The software's source code should be hosted on GitHub.com in its own repository which uses the following conventions:

  + Contains a file named `README.md` which provides instructions for how to install and use the software.
  + Contains a license named `LICENSE.md` or `LICENSE.txt` or `LICENSE` which specifies copyright holder(s) and terms of use. You are recommended to choose from one of the standard licenses available within the GitHub.com user interface when you create a new repository.
  + Contains a directory called `planning` which contains artifact(s) from the research, planning, and proposal processes.
  + Contains a directory called `app` (or some other name of choice) which contains one or more Python files to perform the application's functionality. The Python files may exist within various sub-directories of the `app` directory, if appropriate.
  + Contains a commit history which reflects incremental development progress, perhaps corresponding with various checkpoint steps if you have chosen one of the example projects.

If the software reads or writes files to represent information inputs and/or outputs, the data files should exist in a directory called `data` and should in most cases be excluded from version control using a `data/.gitignore` file. Ask the professor if you're not sure if or how this applies to your program.

If the software has tests, they should exist in a directory called `test` or `tests` or another name of choice. And the `README.md` should contain instructions for how to run them.

## Submission Instructions

To earn credit for the Proposal Phase deliverable, submit the [Proposal Form](https://goo.gl/forms/VuwbJiR7Q1JTSYG03) by the specified due date. If working on a team, only one member should submit the form on behalf of all teammates, and the "Contributor(s)" section should list the email addresses of all official team members.

To earn credit the Implementation Phase deliverable: edit the [submissions.csv file](submissions.csv) by adding a new row to include your GitHub username(s) and your project's GitHub repository URL; then commit your changes and submit a Pull Request for your changes to be included in the course repository. See the [Contributor Guide](/CONTRIBUTING.md) for instructions. At this time, you are encouraged to use the Git CLI to submit your work.

## Evaluation

The Proposal Phase deliverable is worth 25% of the project grade, and the Implementation Phase deliverable comprises the remaining 75% of the project grade.

In addition, an optional Testing deliverable is worth up to 10% extra credit to be applied toward the weight of this project.

> NOTE: If extra credit raises a project's grade above 100%, that higher grade will carry over into final course grade calculations. :smiley: :chart_with_upwards_trend:

### Proposal Evaluation

Proposal Form responses submitted before the due-date will receive full credit. Late submissions will receive partial credit.

### Implementation Evaluation

Full credit for presence of Python application software which runs without error, meets all requirements, and satisfies proposed objectives. Otherwise partial credit may be awarded.

### Testing Evaluation

Presence of relevant and meaningful software test(s) will earn full bonus points. Otherwise partial bonus points may be awarded.
