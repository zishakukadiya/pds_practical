class InvalidDivisionError(Exception):
    pass


try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    if n2 == 0:
        raise InvalidDivisionError("Cannot divide by zero")

    result = n1 / n2

    print(f"Result : {result}")


except InvalidDivisionError as e:
    print("Custom Exception :", e)


except ValueError:
    print("Please enter valid numbers.")


else:
    print("Division is valid.")


finally:
    print("End of operation.")