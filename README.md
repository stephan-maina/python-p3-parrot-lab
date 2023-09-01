# Debug and Parrot Python Scripts

This repository contains two Python scripts: debug.py and parrot.py. These scripts serve different purposes and demonstrate basic Python programming concepts.

# debug.py

The debug.py script showcases how to use Python's built-in pdb (Python Debugger) module for debugging. It defines a function divide_numbers that attempts to divide two numbers and demonstrates how to handle exceptions using try and except.

# Usage

To run the debug.py script, follow these steps:

Ensure you have Python installed on your system.

Navigate to the directory containing debug.py using your terminal or command prompt.

Run the script using the following command:

bash
Copy code
python debug.py

# How it Works

The debug.py script does the following:

Defines a function divide_numbers(a, b) to perform division.
Tries to divide two numbers (numerator and denominator).
Catches a ZeroDivisionError if the denominator is zero.
Starts a post-mortem debugging session using pdb.post_mortem() to inspect the program's state when an exception occurs.

# Contributing

If you'd like to contribute to the debug.py script or report issues, please follow these guidelines:

Reporting Issues: If you encounter a bug or have a suggestion, please open an issue on this repository.

Contributing Code: If you want to contribute code improvements, fork this repository, make your changes, and submit a pull request.

# parrot.py

The parrot.py script is a simple example of a Python script that defines a function parrot_says. This function accepts a message as input and echoes it back, simulating what a parrot might do.

# Usage
To run the parrot.py script, follow these steps:

Ensure you have Python installed on your system.

Navigate to the directory containing parrot.py using your terminal or command prompt.

Run the script using the following command:

bash
Copy code
python parrot.py

# How it Works
The parrot.py script does the following:

Defines a function parrot_says(message) that echoes the provided message.
Prompts the user to input a message.
Calls the parrot_says function with the user's message and displays the echoed message.

# Contributing

If you'd like to contribute to the parrot.py script or report issues, please follow the same contribution guidelines mentioned for debug.py.

# License
These scripts are provided under the MIT License. You can use and modify them freely according to the terms of the license.

## Resources

- [Default arguments in Python - GeeksforGeeks](https://www.geeksforgeeks.org/default-arguments-in-python/)

