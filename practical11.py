
import pandas as pd

# Create a Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)

# Create a DataFrame
data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Riya"],
    "Age": [20, 21, 19, 20, 22],
    "Course": ["Computer Engineering", "Computer Engineering",
               "IT Engineering", "Computer Engineering",
               "IT Engineering"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# Data selection
print("\nName Column:")
print(df["Name"])

print("\nSelected Name and Marks:")
print(df[["Name", "Marks"]])

# Filtering
print("\nStudents with Marks greater than 85:")
print(df[df["Marks"] > 85])

# Grouping
print("\nStudents grouped by Course:")
grouped = df.groupby("Course")

for course, group in grouped:
    print("\nCourse:", course)
    print(group)

# Aggregation
print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nMaximum Marks by Course:")
print(df.groupby("Course")["Marks"].max())

print("\nMinimum Marks by Course:")
print(df.groupby("Course")["Marks"].min())
