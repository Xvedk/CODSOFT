import math  


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)


def calculator():
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sine' for sine function")
    print("Enter 'cosine' for cosine function")
    print("Enter 'tangent' for tangent function")
    
    choice = input("Enter operation: ")
    
    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 'add':
            result = add(num1, num2)
        elif choice == 'subtract':
            result = subtract(num1, num2)
        elif choice == 'multiply':
            result = multiply(num1, num2)
        elif choice == 'divide':
            result = divide(num1, num2)
        
        print(f"Result: {result}")
    elif choice in ('sine', 'cosine', 'tangent'):
        angle = float(input("Enter the angle in radians: "))
        
        if choice == 'sine':
            result = sine(angle)
        elif choice == 'cosine':
            result = cosine(angle)
        elif choice == 'tangent':
            result = tangent(angle)
        
        print(f"Result: {result}")
    else:
        print("Invalid input. Please enter a valid operation.")


calculator()
