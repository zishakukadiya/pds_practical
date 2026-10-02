
import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employee.csv")

print("Employee Data:")
print(df)

# 1. Monthly Income Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Monthly Income"], bins=6, edgecolor="black")
plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")
plt.show()

# 2. Age vs Monthly Income
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Monthly Income"])
plt.title("Age vs Monthly Income")
plt.xlabel("Age")
plt.ylabel("Monthly Income")
plt.show()

# 3. Correlation Matrix
print("\nCorrelation Matrix:")
print(df[["Age", "Monthly Income", "YearsAtCompany"]].corr())

# 4. Correlation Heatmap
plt.figure(figsize=(7, 5))
plt.imshow(
    df[["Age", "Monthly Income", "YearsAtCompany"]].corr(),
    cmap="coolwarm",
    interpolation="none"
)
plt.colorbar()

plt.xticks(
    range(3),
    ["Age", "Monthly Income", "YearsAtCompany"]
)
plt.yticks(
    range(3),
    ["Age", "Monthly Income", "YearsAtCompany"]
)

plt.title("Correlation Heatmap")
plt.show()
