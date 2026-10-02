
import pandas as pd
import numpy as np

# ==========================================
# DATA CLEANING
# ==========================================

# Create sample dataset
data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Rahul", "Riya"],
    "Age": [20, 21, np.nan, 22, 20, 23],
    "Salary": [25000, 30000, 28000, np.nan, 25000, 1000000]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA")
print("-------------")
print(df)

# ==========================================
# 1. DETECT MISSING VALUES
# ==========================================

print("\nMISSING VALUES")
print("--------------")

print(df.isnull().sum())

# ==========================================
# 2. HANDLE MISSING VALUES
# ==========================================

# Fill missing Age with mean age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with mean salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nDATA AFTER HANDLING MISSING VALUES")
print("-----------------------------------")
print(df)

# ==========================================
# 3. REMOVE DUPLICATE RECORDS
# ==========================================

print("\nNUMBER OF DUPLICATE RECORDS:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDATA AFTER REMOVING DUPLICATES")
print("-------------------------------")
print(df)

# ==========================================
# 4. DETECT OUTLIERS
# ==========================================

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]

print("\nOUTLIERS IN SALARY")
print("------------------")
print(outliers)

# ==========================================
# 5. REMOVE OUTLIERS
# ==========================================

df_cleaned = df[
    (df["Salary"] >= lower_limit) &
    (df["Salary"] <= upper_limit)
]

print("\nFINAL CLEANED DATA")
print("------------------")
print(df_cleaned)
