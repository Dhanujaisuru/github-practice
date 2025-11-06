# calculator.py
# A simple Python calculator for GitHub practice

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("-----------------")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

print("hello my dear friend")