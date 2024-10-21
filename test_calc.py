import math
from calc import add, subtract, multiply, divide, power, square_root,logarithm, factorial

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(5, 7) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-2, 5) == -10
    assert multiply(0, 7) == 0

def test_divide():
    assert divide(6, 2) == 4
    assert divide(7, 0) == "Error! Division by zero."
    assert divide(5, 2) == 2.5

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, -2) == 1/9

def test_square_root():
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(-1) == "Error! Negative value for square root."


def test_logarithm():
    assert logarithm(100, 10) == 2
    assert logarithm(1, 10) == 0
    assert logarithm(-10, 10) == "Error! Invalid input for logarithm."
    assert logarithm(10, 1) == "Error! Invalid input for logarithm."

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-5) == "Error! Negative value for factorial."
