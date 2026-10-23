# Module 2: Functions, Files & Exception Handling

# 1. Functions Examples
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Function calling
print(greet("Aditya"))
print("Addition:", add_numbers(10, 20))
print("Factorial of 5:", factorial(5))

# 2. File Handling
with open("sample.txt", "w") as f:
    f.write("Learning Functions, Files & Exception Handling\n")
    f.write("Codomax Digital Solutions - Module 2")

with open("sample.txt", "r") as f:
    content = f.read()
    print("\nFile Content:", content)

# 3. Exception Handling
try:
    num = int(input("\nEnter a number to divide 100: "))
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("Program completed successfully!")
