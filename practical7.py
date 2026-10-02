import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yashu@2007"
)

cursor = con.cursor()

print("MySQL connected successfully!")

cursor.execute("CREATE DATABASE IF NOT EXISTS college")

cursor.execute("USE college")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
""")

con.commit()

print("Database and table created successfully!")

# Insert student records

sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"

values = [
    ("Rahul", 20, "Computer Engineering"),
    ("Priya", 21, "Computer Engineering"),
    ("Amit", 19, "Computer Engineering")
]

cursor.executemany(sql, values)

con.commit()

print("Student records inserted successfully!")


# Display student records

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("\nStudent Records:")

for row in rows:
    print(row)


# Close connection

cursor.close()
con.close()

print("\nMySQL connection closed.")