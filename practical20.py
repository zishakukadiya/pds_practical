
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(12, 8))

# Data
x = [1, 2, 3, 4, 5]
y = [10, 25, 20, 35, 30]

subjects = ["Python", "PDS", "CN", "WAD", "SS"]
marks = [85, 72, 90, 80, 70]

data = [95, 70, 55, 60, 65, 70, 75, 80, 85, 90]

students = ["A", "B", "C", "D", "E"]
scores = [70, 80, 65, 90, 75]


# 1. Line Plot
plt.subplot(2, 3, 1)

plt.plot(x, y, marker="o")

plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()


# 2. Bar Chart
plt.subplot(2, 3, 2)

plt.bar(subjects, marks)

plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")


# 3. Histogram
plt.subplot(2, 3, 3)

plt.hist(data, bins=5)

plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")


# 4. Pie Chart
plt.subplot(2, 3, 4)

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Pie Chart")


# 5. Scatter Plot
plt.subplot(2, 3, 5)

plt.scatter(students, scores)

plt.title("Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.grid()


# Figure properties
plt.suptitle(
    "Different Types of Plots using Matplotlib",
    fontsize=16
)

plt.tight_layout()

plt.savefig("practical20_graphs.png")
