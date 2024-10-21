import math

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


def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Invalid input for logarithm."
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error! Negative value for factorial."
    return math.factorial(int(x))

def display_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("10. Logarithm (log base x)")
    print("11. Factorial")
    print("12. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-12): ")

        if choice == '12':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '10', '11']:
            num1 = float(input("Enter the first number: "))
            if choice in ['5', '10']:
                num2 = float(input("Enter the second number: "))
        elif choice in ['7', '8', '9']:
            num1 = float(input("Enter the angle in degrees: "))
        elif choice == '6':
            num1 = float(input("Enter the number: "))
        elif choice == '11':
            num1 = float(input("Enter the number for factorial: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"Square root of {num1} = {square_root(num1)}")
        elif choice == '7':
            print(f"sin({num1}°) = {sine(num1)}")
        elif choice == '8':
            print(f"cos({num1}°) = {cosine(num1)}")
        elif choice == '9':
            print(f"tan({num1}°) = {tangent(num1)}")
        elif choice == '10':
            base = float(input("Enter the base: "))
            print(f"log base {base} of {num1} = {logarithm(num1, base)}")
        elif choice == '11':
            print(f"Factorial of {num1} = {factorial(num1)}")
        else:
            print("Invalid Input. Please select a valid option.")

if __name__ == "__main__":
    main()
