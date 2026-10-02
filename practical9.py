import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("employee.csv")

income = df["MonthlyIncome"]

print(df["MonthlyIncome"].describe())

# 1. Histogram
plt.figure(figsize=(8, 6))

plt.hist(df["MonthlyIncome"], bins=10)

plt.xlabel("Monthlyincome")
plt.ylabel("Number of employees")
plt.title("Distribution of monthly income")

plt.tight_layout()

plt.savefig("monthly_income_distribution.png")
plt.close()


# 2. Scatter Plot
plt.figure(figsize=(8, 6))

plt.scatter(
    df["TotalWorkingYears"],
    df["MonthlyIncome"]
)

plt.xlabel("Total Working years")
plt.ylabel("Monthly Income")
plt.title("Total Working years vs Monthly Income")

plt.tight_layout()

plt.savefig("working_years_vs_income.png")
plt.close()


# 3. Correlation
correlation = df["TotalWorkingYears"].corr(
    df["MonthlyIncome"]
)

print("correlation= ", correlation)


vars = [
    "MonthlyIncome",
    "TotalWorkingYears",
    "YearsAtCompany",
    "JobSatisfaction"
]

correlation_matrix = df[vars].corr()

print(correlation_matrix.round(2))


# 4. Heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("correlation matrix of emmployee variables")

plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.close()


print("1. monthly_income_distribution.png")
print("2. working_years_vs_income.png")
print("3. correlation_heatmap.png")