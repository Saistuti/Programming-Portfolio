# Week 5 : Python Command - Line and System Utilities
This repository contains a collection of Python programs that demonstrate the use of command-line arguments, system modules, network access, and file handling.

## Program 1: Operating System Platform Reporter
This program reports the operating system platform on which the Python interpreter is currently running.

What it does:
- Retrieves platform information from the system
- Displays the operating system identifier

Python concepts used:
- sys module
- Accessing system attributes

## Program 2: Command-Line Argument Counter
This program reports how many command-line arguments were provided when the script was run.
The program name itself is not included in the count.

What it does:
- Uses ays.argv to count arguments
- Subtracts one to ignore the script name

Python concepts used:
- Command-line arguments
- Lists and len()

## Program 3: Shortest Command-Line Argument
This program finds and prints the shortest command-line argument provided.
If no arguments are supplied, it prints an error message.

What it does:
- Extracts arguments exclusing the program name
- Sorts them by length
- Displays the shortest argument

Python concepts used:
- List slicing
- Sorting with key=len
- Conditional checks

## Program 4: Website Availability Checker
This program checks whether a website is reachable by sending an HTTP request to a URL provided via the command line.

What it does:
- Reads a URL from the command line
- Attempts to open the website
- Displays the HTTP status code if successful
- Prints an error if the site cannot be reached

Python concepts used:
- Command-line arguments
- Exception handling (try/except)
- urllib.request for HTTP requests

# Program 5: Temperature Statistics from Command Line
This program reads temperature values from the command line and displays:
- Maximum temperature
- Minimum temperature
- Mean temperature
If no values are provided, the program exits with an error message.

Python concepts used:
- List comprehensions
- Type conversion (float)
- Built-in functions (max(), min())
- statistics.mean()

# Program 6: File Backup Creator
This program creates a backup copy of a file whose name is provided as a command-line argument. The backup file has the same contents and a .bak extension.

What it does:
- Reads the filename from the command line
- Creates a backup copy
- Handles missing files gracefully

Python concepts used:
- File handling
- shutil.copy()
- Exception handling
- Command-line arguments
  
