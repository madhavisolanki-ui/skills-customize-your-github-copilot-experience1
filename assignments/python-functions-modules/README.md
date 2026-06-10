# 📘 Assignment: Python Functions and Modules

## 🎯 Objective

Practice writing reusable functions and organizing code into modules. Students will build helper functions, separate them into a Python module, and then import those helpers into the main program.

## 📝 Tasks

### 🛠️ Task 1: Create reusable functions

#### Description
Implement functions that perform common tasks such as greeting a user, calculating a rectangle area, and checking whether a word is a palindrome.

#### Requirements
Completed program should:

- Define a `greet_student(name)` function that returns a greeting string.
- Define a `calculate_rectangle_area(width, height)` function that returns the rectangle area.
- Define an `is_palindrome(text)` function that returns `True` when the text is a palindrome and `False` otherwise.

### 🛠️ Task 2: Move helpers into a module

#### Description
Create a `utils.py` module to store reusable helper functions, then import them into `starter-code.py`.

#### Requirements
Completed assignment should:

- Move the helper functions into `utils.py`.
- Import the functions in `starter-code.py` using `from utils import ...`.
- Keep `starter-code.py` as the entry point for the program.

### 🛠️ Task 3: Use the module in a program

#### Description
Complete the program so it prompts the user for input, calls functions from the module, and prints the results.

#### Requirements
Completed program should:

- Ask the user for their name and print a greeting.
- Ask for width and height and print the rectangular area.
- Ask for a word and print whether it is a palindrome.
- Use the imported helper functions from `utils.py`.
