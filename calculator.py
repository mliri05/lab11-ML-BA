#https://github.com/mliri05/lab11-ML-BA
# Partner 1: Max Lirio
# Partner 2: Bravery Aung

import math

def square_root(a):
    if (a < 0):
        raise ValueError("Cannot take square root of a negative number")

    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def multiply(a, b):
    return a * b

def div(a, b):
    if (a == 0):
        raise ZeroDivisionError("Cannot divide by zero")

    else:
        return b / a

def divide(a, b):
    if (a == 0):
        raise ZeroDivisionError("Cannot divide by zero")

    else:
        return b / a

def logarithm(a, b):
    if (a <= 0) or (b <= 0):
        raise ValueError("Logarithm arguments must be positive")

    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b

def exponent(a, b):
    return a ** b
