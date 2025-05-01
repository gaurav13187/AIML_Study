a = 5
b = 10

def add_two_numbers(x, y):
    return x + y

def subtract_two_numbers(x, y):
    return x - y

def multiply_two_numbers(x, y):
    return x * y

def divide_two_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


