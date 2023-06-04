# Python Cheat Sheet

# Basic Syntax
# Python statements are written line by line.
# Use indentation (usually 4 spaces) to define code blocks.
# Use the # symbol for single-line comments.

# Example:
print("Hello, World!")  # This line prints "Hello, World!"

# Data Types
# int: integers (e.g., 5, -2)
# float: floating-point numbers (e.g., 3.14, -0.5)
# str: strings (e.g., "Hello", 'World')
# bool: Boolean values (True or False)

# Example:
age = 25
pi = 3.14
name = "Alice"
is_student = True

# Variables and Assignment
# Use the assignment operator = to assign values to variables.
# Variable names must start with a letter or underscore and can contain letters, numbers, or underscores.
# Python is case-sensitive.

# Example:
x = 5
y = "Hello"
z = 3.14

# Basic Input/Output
# print("text"): displays text on the console.
# input("prompt"): accepts user input from the console.

# Example:
print("Hello, World!")  # This line prints "Hello, World!"
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Basic Operations
# Arithmetic: + (addition), - (subtraction), * (multiplication), / (division), ** (exponentiation), % (modulo)
# Comparison: == (equal to), != (not equal to), < (less than), > (greater than), <= (less than or equal to), >= (greater than or equal to)
# Logical: and (logical and), or (logical or), not (logical not)

# Example:
x = 5 + 3  # Addition: 8
y = 10 - 2  # Subtraction: 8
z = 4 * 5  # Multiplication: 20
w = 10 / 3  # Division: 3.3333...
p = 2 ** 3  # Exponentiation: 8
q = 15 % 4  # Modulo: 3

# Control Flow
# if statement: executes code block if a condition is true.
# else statement: executes code block if the preceding if statement condition is false.
# elif statement: allows checking additional conditions.
# for loop: iterates over a sequence of elements.
# while loop: repeatedly executes a block of code while a condition is true.
# break statement: exits the innermost loop.
# continue statement: skips the rest of the current loop iteration and moves to the next iteration.

# Example:
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

for i in range(1, 6):
    print(i)

num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

# Lists
# Ordered collection of elements enclosed in square brackets [].
# Access elements using indexing (starting from 0) or slicing.
# Common operations: len(), append(), insert(), remove(), pop(), sort(), reverse()

# Example:
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing an element: "apple"

fruits.append("orange")  # Adding an element to the end
fruits.insert(1, "grape")  # Inserting an element at a specific index

fruits.remove("banana")  # Removing an element by value
removed_fruit = fruits.pop()  # Removing and returning the last element

fruits.sort()  # Sorting the list in ascending order
fruits.reverse()  # Reversing the order of elements in the list

# Functions
# Reusable blocks of code defined using the def keyword.
# Can take parameters and return values.

# Example:
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8

# Modules
# Python files containing functions, classes, or variables.
# Import modules using the import statement.

# Example:
import math

print(math.sqrt(16))  # Output: 4.0

# Error Handling
# Use try and except statements to catch and handle exceptions.

# Example:
try:
    num = int(input("Enter a number: "))
    print("The square of the number is:", num ** 2)
except ValueError:
    print("Invalid input. Please enter a valid number.")