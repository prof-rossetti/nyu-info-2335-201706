# Python Language Overview

### The `csv` Module

Reference: https://docs.python.org/3/library/csv.html.

Use the `csv` module to process data stored in Comma Separated Values (CSV) format.

## Reading CSV Files

```python
import csv

csv_file_path = "some/relative-path/to/my_data.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... reader = csv.reader(csv_file)
    for row in reader:
        print(list(row.keys())) # shows you the column names as keys
        print(row["some_key"]) # you can treat the row like a dictionary and access one of its attributes
```

## Writing CSV Files

```python
import csv

csv_file_path = "some/relative-path/to/my_data.csv"

with open(csv_file_path, "w") as csv_file:
    headers = ["city", "name"]
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})
```
