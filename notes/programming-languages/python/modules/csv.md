# Python Language Overview

## The `csv` Module

Reference: https://docs.python.org/3/library/csv.html.

Use the `csv` module to process data stored in Comma Separated Values (CSV) format.

To setup these examples, create a new directory on your Desktop called `csv-mgmt` and navigate there from your command line. Create a Python script in that directory called `my_script.py` and place inside it contents from each of the following sections, respectively.

### Writing CSV Files

```python
import csv

csv_file_path = "teams.csv"

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})

#> city,name
#> New York,Yankees
#> New York,Mets
#> Boston,Red Sox
#> New Haven,Ravens
```

### Reading CSV Files

```python
import csv

csv_file_path = "teams.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        print(row["city"], row["name"])

#> New York Yankees
#> New York Mets
#> Boston Red Sox
#> New Haven Ravens
```
