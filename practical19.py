
import pandas as pd

# ==========================================
# DATA PREPROCESSING USING PANDAS
# ==========================================

# Create first dataset
data1 = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 75, 88]
}

df1 = pd.DataFrame(data1)

print("ORIGINAL DATA")
print("-------------")
print(df1)


# ==========================================
# 1. SLICING
# ==========================================

print("\n1. SLICING")
print("----------")

print(df1.iloc[0:3])

print("\nSelected Columns:")
print(df1[["Name", "Marks"]])


# ==========================================
# 2. FILTERING
# ==========================================

print("\n2. FILTERING")
print("------------")

filtered_data = df1[df1["Marks"] >= 80]

print(filtered_data)


# ==========================================
# 3. SORTING
# ==========================================

print("\n3. SORTING")
print("----------")

sorted_data = df1.sort_values(by="Marks", ascending=False)

print(sorted_data)


# ==========================================
# 4. CONCATENATING
# ==========================================

data2 = {
    "Name": ["Riya", "Karan"],
    "Age": [20, 21],
    "Marks": [92, 78]
}

df2 = pd.DataFrame(data2)

combined_data = pd.concat([df1, df2], ignore_index=True)

print("\n4. CONCATENATED DATA")
print("--------------------")
print(combined_data)


# ==========================================
# 5. AGGREGATION
# ==========================================

print("\n5. AGGREGATION")
print("--------------")

print("Average Marks:", combined_data["Marks"].mean())
print("Maximum Marks:", combined_data["Marks"].max())
print("Minimum Marks:", combined_data["Marks"].min())
print("Total Marks:", combined_data["Marks"].sum())


# ==========================================
# 6. NORMALIZATION
# ==========================================

print("\n6. NORMALIZATION")
print("----------------")

# Min-Max normalization
min_marks = combined_data["Marks"].min()
max_marks = combined_data["Marks"].max()

combined_data["Normalized_Marks"] = (
    (combined_data["Marks"] - min_marks)
    / (max_marks - min_marks)
)

print(combined_data)
