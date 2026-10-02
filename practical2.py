a = [100, 200, 300, 400]

print("Original List =", a)

a.append(500)
print("Append =", a)

a.insert(2, 250)
print("Insert =", a)

a.remove(200)
print("Remove =", a)

a.pop()
print("Pop =", a)

a.sort()
print("Sort =", a)

a.reverse()
print("Reverse =", a)

print("Count(300) =", a.count(300))
print("Index(250) =", a.index(250))
print("Length =", len(a))


t = (10, 20, 10, 45, 60)

print("Tuple =", t)
print("Count(10) =", t.count(10))
print("Index(45) =", t.index(45))
print("Length =", len(t))


s = {10, 20, 30}

print("Original Set =", s)

s.add(40)
print("Add =", s)

s.remove(20)
print("Remove =", s)

s.discard(10)
print("Discard =", s)

s.update([60, 80])
print("Update =", s)

s.pop()
print("Pop =", s)

print("Length =", len(s))


d = {
    "car": "BMW",
    "Model": 2024,
    "price": 5000000
}

print("Dictionary =", d)
print("Keys =", d.keys())
print("Values =", d.values())
print("Items =", d.items())
print("Get car =", d.get("car"))

d.update({"car": "BMW", "Model": 2024, "price": 6000000})
print("Update =", d)

d.pop("Model")
print("Pop =", d)

d.clear()
print("Clear =", d)


s = "Computer Engineering Department"

print("Original String =", s)
print("Upper =", s.upper())
print("Lower =", s.lower())

print("Replace =", s.replace("Engineering", "Science"))

print("Split =", s.split())

print("Find =", s.find("Engineering"))

print("Startswith =", s.startswith("Computer"))
print("Endswith =", s.endswith("Department"))

print("Count =", s.count("e"))

s1 = "Python Lab"
print("Strip =", s1.strip())