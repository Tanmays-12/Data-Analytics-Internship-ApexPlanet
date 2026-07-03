# Data Quality Assessment

## 1. Missing Values

### Command Used

```python
df.isnull().sum()
```

### Results

| Column | Missing Values |
| ------ | -------------: |
| Age    |             17 |
| City   |             12 |

### Observation

The dataset contains missing values in the **Age** and **City** columns. All other columns contain complete data. These missing values will be addressed during the Data Cleaning & Transformation phase.


## 2. Duplicate Records

### Command Used

```python
df.duplicated().sum()
```

### Result

| Metric            | Value |
| ----------------- | ----: |
| Duplicate Records |     0 |

### Observation

No duplicate records were found in the dataset. Each row represents a unique transaction, so no duplicate removal was required during the data cleaning process.


## 3. Inconsistent Formatting

### Commands Used

```python
df["Gender"].unique()

df["City"].unique()

df["Product"].value_counts(dropna=False)

df["Category"].value_counts(dropna=False)
```

### Results

| Column   | Status                                    |
| -------- | ----------------------------------------- |
| Gender   | Consistent                                |
| City     | Consistent (contains missing values only) |
| Product  | Consistent                                |
| Category | Consistent                                |

### Observation

The categorical columns were examined for inconsistent formatting by reviewing their unique values and frequency counts. No variations in capitalization, spelling, or whitespace were observed. The only issue identified in the City column was missing values, which were already documented in the Missing Values section.

## 4. Outlier Assessment

### Method Used

Interquartile Range (IQR) Method

### Results

| Column      |       Outliers Detected |
| ----------- | ----------------------: |
| Age         |                       0 |
| Quantity    |                       0 |
| Unit_Price  |                       0 |
| Total_Sales | 19 (Potential Outliers) |

### Observation

The IQR method identified no outliers in the Age, Quantity, or Unit_Price columns.

The Total_Sales column contained 19 potential outliers based on the statistical threshold. However, since Total_Sales is calculated as **Quantity × Unit_Price**, these higher values represent legitimate high-value transactions rather than data errors. Therefore, no outlier removal was performed.


