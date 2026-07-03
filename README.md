# ApexPlanet Data Analytics Internship – Task 1

## Project Overview

This project was completed as part of the ApexPlanet Data Analytics Internship.

The objective of Task 1 was to understand the dataset, assess data quality, clean and transform the data using Python and Pandas, and prepare an analysis-ready dataset.

---

## Objectives

- Access and understand the dataset
- Create a data dictionary
- Identify data quality issues
- Handle missing values
- Remove duplicate records
- Standardize date formats
- Perform feature engineering
- Export a cleaned dataset

---

## Dataset Information

Dataset Type:
Sales Transaction Dataset

Total Records:
997

Total Columns:
12

---

## Technologies Used

- Python
- Pandas
- Microsoft Excel

---

## Data Quality Assessment

The following checks were performed:

- Missing Value Analysis
- Duplicate Record Detection
- Formatting Consistency Check
- Outlier Detection using IQR

---

## Data Cleaning Performed

### Missing Values

- Age → Filled using Median
- City → Filled using Mode

### Duplicate Records

- Checked and removed if present

### Date Standardization

- Converted Order_Date into DateTime format

### Feature Engineering

Created a new feature:

High_Value_Order

Business Rule:

- Total Sales ≥ ₹100,000 → Yes
- Otherwise → No

---

## Output

Generated:

cleaned_dataset.xlsx

This dataset is ready for further analysis and visualization.

---

## Project Structure

```

data/
scripts/
documentation/
README.md
requirements.txt

```

---

## Author

Tanmay Krishna Sattiraju