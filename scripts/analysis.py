import pandas as pd

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")


print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Gender"].unique())
print(df["City"].unique())
print(df["Product"].value_counts(dropna=False))
print(df["Category"].value_counts(dropna=False))
print(df.describe())  #gives statisical information about every numeric column


# -------------------------------
# Outlier Detection using IQR
# -------------------------------

# ---------------------------------------
# Function to Detect Outliers Using IQR
# ---------------------------------------

def detect_outliers(column):

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

    print("=" * 50)
    print("Column :", column)
    print("Q1 :", Q1)
    print("Q3 :", Q3)
    print("IQR :", IQR)
    print("Lower Limit :", lower_limit)
    print("Upper Limit :", upper_limit)
    print("Number of Outliers :", len(outliers))


# Check every numeric column

detect_outliers("Age")
detect_outliers("Quantity")
detect_outliers("Unit_Price")
detect_outliers("Total_Sales")
