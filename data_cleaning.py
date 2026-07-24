

import pandas as pd
import numpy as np



# Load matches Dataset.
data=pd.read_csv("matches.csv")
print("Loaded CSV file's Shape is",data.shape)
print("...........................................")
print("Loaded CSV file's Information is",data.info())
print("...........................................")
print("Loaded CSV file's Description is",data.describe())
print("...........................................")
print("Missing Values are : \n", data.isnull().sum())
print("...........................................")
print("Displaying DATA Types : \n", data.dtypes)


data.drop("method", axis=1, inplace=True)

data.shape

# Fill categorical columns with mode... city, player_of_match , and winner
data['city'].fillna(data['city'].mode()[0], inplace=True)
data['player_of_match'].fillna(data['player_of_match'].mode()[0], inplace=True)
data['winner'].fillna(data['winner'].mode()[0], inplace=True)

print(data["city"].isnull().sum())

print(data["winner"].isnull().sum())

print(data["player_of_match"].isnull().sum())

# Fill numeric columns with median
data["result_margin"].fillna(data["result_margin"].median(), inplace=True)
data["target_runs"].fillna(data["target_runs"].median(), inplace=True)
data["target_overs"].fillna(data["target_overs"].median(), inplace=True)

print("Number of duplicate rows:", data.duplicated().sum())

# Dropping duplicate rows

before= data.shape[0]
data.drop_duplicates(inplace=True)
after= data.shape[0]
print("Duplicate rows removed:", before - after)

# Outlier Remove

numeric_columns = ["result_margin", "target_runs"]

for col in numeric_columns:

    # Ignore missing values
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Count outliers
    outliers = ((data[col] < lower) | (data[col] > upper)).sum()
    print(f"{col}: {outliers} outliers found")

    # Cap outliers
    data[col] = data[col].clip(lower=lower, upper=upper)

print("\nOutliers have been capped.")

print("\nFinal Data Types:")
print(data.dtypes)

# Save cleaned dataset as matches_cleaned
data.to_csv("matches_cleaned.csv", index=False)
print("Matches cleaned file saved successfully.")
print(data.columns.tolist())

# Load again the cleaned dataset

data=pd.read_csv("matches_cleaned.csv")

# Load Delivery Dataset now....................................................................

delivery_data=pd.read_csv("deliveries.csv")
print("Loaded CSV file's Shape is",delivery_data.shape)
print("...........................................")
print("Loaded CSV file's Information is",delivery_data.info())
print("...........................................")
print("Loaded CSV file's Description is",delivery_data.describe())
print("...........................................")
print("Missing Values are : \n", delivery_data.isnull().sum())
print("...........................................")
print("Displaying DATA Types : \n", delivery_data.dtypes)

print("Number of duplicate rows:", delivery_data.duplicated().sum())

delivery_data.drop_duplicates(inplace=True)

delivery_data.shape

# Outlier remove
numeric_columns = ["batsman_runs", "total_runs"]

for col in numeric_columns:

    Q1 = delivery_data[col].quantile(0.25)
    Q3 = delivery_data[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = ((delivery_data[col] < lower) | (delivery_data[col] > upper)).sum()

    print(f"{col}")
    print("Q1 =", Q1)
    print("Q3 =", Q3)
    print("IQR =", IQR)
    print("Lower Limit =", lower)
    print("Upper Limit =", upper)
    print("Outliers =", outliers)
    print()

    # Cap outliers
    delivery_data[col] = delivery_data[col].clip(lower=lower, upper=upper)

# Now save cleaned Csv

delivery_data.to_csv("deliveries_cleaned.csv", index=False)


