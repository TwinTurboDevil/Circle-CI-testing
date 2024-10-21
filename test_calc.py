import unittest
import math

# Assuming the calculator functions are in a module called 'calculator'
# Import the necessary functions from the calculator code

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Negative value for square root."
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Invalid input for logarithm."
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error! Negative value for factorial."
    return math.factorial(int(x))


class TestScientificCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 7), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 7), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(7, 0), "Error! Division by zero.")
        self.assertEqual(divide(5, 2), 2.5)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, -2), 1/9)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(-1), "Error! Negative value for square root.")

    def test_sine(self):
        self.assertAlmostEqual(sine(30), 0.5, places=5)
        self.assertAlmostEqual(sine(90), 1.0, places=5)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1.0, places=5)
        self.assertAlmostEqual(cosine(90), 0.0, places=5)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1.0, places=5)
        self.assertEqual(tangent(90), float('inf'))

    def test_logarithm(self):
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(1, 10), 0)
        self.assertEqual(logarithm(-10, 10), "Error! Invalid input for logarithm.")
        self.assertEqual(logarithm(10, 1), "Error! Invalid input for logarithm.")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-5), "Error! Negative value for factorial.")

if __name__ == '__main__':
    unittest.main()
