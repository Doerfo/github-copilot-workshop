# simple calculator which offers addition, subtraction, multiplication, division, and absolute value calculation

# and can be used in a command line interface or as a module

# this function adds two numbers
def add(x, y):
    return x + y

# this function subtracts two numbers
def subtract(x, y):
    return x - y

# this function multiplies two numbers
def multiply(x, y):
    return x * y


# this function calculates the absolute value of a number
def absolute(x):
    return x if x >= 0 else -x

# this function divides two numbers
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y