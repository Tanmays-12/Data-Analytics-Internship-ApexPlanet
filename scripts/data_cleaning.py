import pandas as pd

df = pd.read_excel("../data/ApexPlanet_DataAnalytics_Dataset.xlsx")

# Missing Values

df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

print(df.isnull().sum())

# Remove duplicate records
df.drop_duplicates(inplace=True)  # Inplace is used because, without it the python will create a new cleaned copy and won't change the exisiting dataset

# Verify duplicates
print("Duplicate Records:", df.duplicated().sum())


# Convert Order_Date to datetime format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Verify the data type
print(df["Order_Date"].dtype)

print(df["Order_Date"].dt.month)

df["High_Value_Order"] = df["Total_Sales"].apply(lambda x : "Yes" if x >= 100000 else "No")

# Exporting Cleaned Dataset

df.to_excel("../data/cleaned_dataset.xlsx", index=False)