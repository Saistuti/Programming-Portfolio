# Week 4 : Python Functions and String & Temperature Processing
This repository contains a collection of Python programs focused on functions, string manipulation, input validation, and temperature processing.

## Program 1: Valid Mark Checker
This program defines a function that checks whether an integer lies within the valid range of 0 to 100 inclusive. A short test program allows the user to enter a value and see the result.

What it does:
- Returns True if the number is between 0 and 100
- Returns False otherwise

Python concepts used:
- Functions
- Boolean expressions
- Comparison operations
- User input

## Program 2: Uppercase and Lowercase Counter
This program counts how many uppercase and lowercase letters appear in a given string.

What it does:
- Iterates through each character in the string
- Counts uppercase and lowercase letters
- Returns the result as a tuple

Python concepts used:
- Functions
- Loops (for)
- String methods (isupper(), islower())
- Tuples

## Program 3: Name Formantting
This program asks the user for their name and ensures it is displayed correctly with:
- First letter uppercase
- Remaining letters lowercase
If no name is entered, it greets the user as "Stranger".

Python concepts used:
- String methods (capitalize())
- Conditional statements
- Input validation

## Program 4: Remove Last Character from a String
This program defines a function that removes the last character of a string.
If the string has one or fewer characters, it is returned unchanged.

Python concepts used:
- Functions
- String slicing
- len() function

## Program 5: Temperature Conversion Functions
This program provides two functions:
- Convert Centigrade to Fahrenheit
- Convert Fahrenheit to Centigrade
Both functions are tested using sample values.

Python concepts used:
- Functions
- Aritnmetic operations
- Return values

## Program 6: Centrigade to Fahrenheit Input Converter
This program reads a temperature entered in the format <number>C, converts it to Fahrenheit, and prints the result in <number>F format.

Python concepts used:
- String slicing
- Type conversion (float)
- Arithmetic operations

## Program 7: Temperature Statistics (Fixed Input Count)
This program reads six centigrade temperatures, converts them to numeric values, and calculates: maximum temperature, minimum temperature and mean temperature.

Python concepts used:
- Lists
- Loops
- Built-in functions (max(), min())
- statistics.mean()

## Program 8: Temperature Statistics (Variable Input Count)
This program allows the user to enter any number of temperatures in centigrade format. Input ends when the user presses Enter without typing a value.

The program then displays:
- Maximum temperature
- Minimum temperature
- Mean temperature
If no values are entered, an appropriate message is shown.

Python concepts used:
- While loops
- Lists
- Input termination conditions
- Exception-safe logic
- statistics module
