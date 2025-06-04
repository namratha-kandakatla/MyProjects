"""Adds two numbers provided by the user and identifies the larger number."""


def add_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a + b
        larger = a if a >= b else b
        print(f"{a} + {b} = {result}")
        print(f"The larger number is {larger}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    add_numbers()
