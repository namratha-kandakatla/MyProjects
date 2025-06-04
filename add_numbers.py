"""Adds two numbers provided by the user."""


def add_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a + b
        print(f"{a} + {b} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    add_numbers()
