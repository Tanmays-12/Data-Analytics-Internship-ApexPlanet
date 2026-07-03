# Data Cleaning Process

## 1. Handling Missing Values

### Objective

Replace missing values without removing records from the dataset.

### Cleaning Performed

* Missing values in the **Age** column were replaced using the **median** of the column.
* Missing values in the **City** column were replaced using the **mode** (most frequently occurring city).

### Verification

After applying the cleaning operations, all missing values were successfully removed from the dataset.

| Column | Missing Values After Cleaning |
| ------ | ----------------------------: |
| Age    |                             0 |
| City   |                             0 |


## 2. Handling Duplicate Records

### Objective

Remove duplicate records to prevent repeated transactions from affecting the analysis.

### Cleaning Performed

The dataset was checked for duplicate records using Pandas. No duplicate records were found; therefore, no rows were removed.

### Verification

Duplicate Records After Cleaning: **0**


## 3. Standardizing Date Format

### Objective

Convert the `Order_Date` column from text format to a datetime format for easier date-based analysis.

### Cleaning Performed

The `Order_Date` column was converted using the `pd.to_datetime()` function.

### Verification

The column data type was successfully converted to `datetime64`, enabling future analysis such as extracting the month, year, and day from each order date.


## 4. Feature Engineering

### Objective

Create a new feature that provides additional business insight without modifying the original data.

### Feature Created

**Column Name:** `High_Value_Order`

### Business Logic

A new column named `High_Value_Order` was created based on the `Total_Sales` column.

* If `Total_Sales` is greater than or equal to **₹100,000**, the order is classified as **"Yes"**.
* Otherwise, it is classified as **"No"**.

### Purpose

This feature helps identify high-value transactions quickly, making it easier to:

* Analyze premium customer purchases.
* Filter high-revenue orders.
* Build business dashboards and reports.
* Support future business analysis and decision-making.

### Verification

The newly created column was verified by comparing the values of `Total_Sales` with the corresponding `High_Value_Order` classification.
