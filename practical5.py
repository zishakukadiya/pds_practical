
print("==========================================")
print("1. TEXT FILE")
print("==========================================")

# Write operation
with open("sample.txt", "w") as file:
    file.write("Welcome to File Handling.\n")

print("Data written successfully.")


# Read operation
with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# Append operation
with open("sample.txt", "a") as file:
    file.write("This line is Appended.\n")

print("Data Append successfully.")


# Read the file again
with open("sample.txt", "r") as file:
    content = file.read()

print(content)


print("==========================================")
print("2. CSV FILE")
print("==========================================")

import csv


# Write operation
data = [
    ["ID", "Name", "Marks"],
    [1, "Deep", 93],
    [2, "Jeet", 89]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV data written successfully.")


# Read operation
print("\nCSV File Data:")

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Append operation
with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Kaish", 98])

print("\nCSV data appended successfully.")


# Read CSV again
print("\nUpdated CSV File Data:")

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)



print("\n==========================================")
print("3. BINARY FILE")
print("==========================================")


# Write operation
data = b"Hello World"

with open("students.bin", "wb") as file:
    file.write(data)

print("Binary data written successfully.")


# Read operation
with open("students.bin", "rb") as file:
    content = file.read()

print("Binary data reading...")
print(content)


# Append operation
new_data = b" Welcome to Python."

with open("students.bin", "ab") as file:
    file.write(new_data)

print("Binary data appended successfully.")


# Read binary file again
with open("students.bin", "rb") as file:
    content = file.read()

print("Updated binary data:")
print(content)

