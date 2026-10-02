
from bs4 import BeautifulSoup

# Sample HTML document
html = """
<html>
<head>
    <title>Student Information</title>
</head>
<body>

<h1>Student Details</h1>

<p>Welcome to Python for Data Science</p>

<ul>
    <li>Jeeya</li>
    <li>Yashasvi</li>
    <li>Rahul</li>
</ul>

<a href="https://www.google.com">Google</a>

</body>
</html>
"""

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract title
print("Title:")
print(soup.title.text)

# Extract heading
print("\nHeading:")
print(soup.h1.text)

# Extract paragraph
print("\nParagraph:")
print(soup.p.text)

# Extract list items
print("\nStudent Names:")
for student in soup.find_all("li"):
    print(student.text)

# Extract link
print("\nLink:")
print(soup.a.get("href"))
