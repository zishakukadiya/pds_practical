# -------------------------------------------------
# 1. IF-ELSE
# -------------------------------------------------

print("1. IF-ELSE")

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")


# -------------------------------------------------
# 2. IF-ELIF-ELSE
# -------------------------------------------------

print("\n2. IF-ELIF-ELSE")

marks = int(input("Enter Marks: "))

if marks <= 100 and marks > 90:
    print("Grade A")

elif marks <= 90 and marks > 80:
    print("Grade B")

elif marks <= 80 and marks > 70:
    print("Grade C")

elif marks <= 70 and marks > 60:
    print("Grade D")

elif marks <= 60 and marks >= 50:
    print("Grade E")

elif marks > 100:
    print("Invalid marks")

else:
    print("Fail")


# -------------------------------------------------
# 3. CONTINUE / SKIP EVEN NUMBERS
# -------------------------------------------------

print("\n3. Skip Even Numbers")

for i in range(10):

    if i % 2 == 0:
        continue

    print(i)


# -------------------------------------------------
# 4. BREAK AND CONTINUE
# -------------------------------------------------

print("\n4. Break and Continue")

i = 1

while i <= 10:

    if i == 7:
        print("Break loop at 7")
        break

    elif i == 5:
        print("Skip iteration at 5")
        i += 1
        continue

    else:
        print(i)

    i += 1


# -------------------------------------------------
# 5. NESTED FOR LOOP
# -------------------------------------------------

print("\n5. Nested For Loop")

for i in range(1, 3):

    for j in range(10, 7, -1):

        print(i, j)