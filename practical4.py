# ------------------------------------------
# 1. SIMPLE USER-DEFINED FUNCTION
# ------------------------------------------

print("1. Simple Function")

def greet():
    print("Hello! Welcome to Python Programming.")


greet()


# ------------------------------------------
# 2. FUNCTION WITH ARGUMENTS
# ------------------------------------------

print("\n2. Function with Arguments")

def add(a, b):
    print("Sum =", a + b)


add(10, 20)


# ------------------------------------------
# 3. FUNCTION TO FIND SQUARE
# ------------------------------------------

print("\n3. Square Function")

def square(n):
    print("Square =", n * n)


square(5)


# ------------------------------------------
# 4. FUNCTION WITH KEYWORD ARGUMENTS
# ------------------------------------------

print("\n4. Keyword Arguments")

def student(name, age):
    print("Name =", name)
    print("Age =", age)


student(age=19, name="Deep")


# ------------------------------------------
# 5. FUNCTION WITH VARIABLE NUMBER
#    OF ARGUMENTS
# ------------------------------------------

print("\n5. Variable Number of Arguments")

def total(*numbers):
    print("Numbers =", numbers)
    print("Total =", sum(numbers))


total(10, 20, 30, 40, 50)


# ------------------------------------------
# 6. USING MATH MODULE
# ------------------------------------------

print("\n6. Math Module")

import math

print("Square Root of 49 =", math.sqrt(49))
print("Value of Pi =", math.pi)
print("Power =", math.pow(2, 3))
print("Factorial of 5 =", math.factorial(5))


# ------------------------------------------
# 7. USING RANDOM MODULE
# ------------------------------------------

print("\n7. Random Module")

import random

numbers = [10, 20, 30, 40, 50]

print("Random Number =", random.randint(1, 100))
print("Random Choice =", random.choice(numbers))


# ------------------------------------------
# 8. USING STATISTICS MODULE
# ------------------------------------------

print("\n8. Statistics Module")

import statistics

data = [10, 20, 30, 40, 50]

print("Data =", data)
print("Mean =", statistics.mean(data))
print("Median =", statistics.median(data))
print("Mode =", statistics.mode([10, 20, 20, 30, 40]))