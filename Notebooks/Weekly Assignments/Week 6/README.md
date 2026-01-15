# Week 6 : Python Functions - Number Theory and Simple Encryption
This repository contains a collection of Python functions that focus on number processing, string manipulation, and simple encryption techniques.

## Program 1: Integer to Binary Converter
This function converts a positive integer into its binary (base-2) representation and returns it as a string.

What it does:
- Uses Python's built-in bin() function
- Removes the 0b prefix to return only the binary digits

Python concepts used:
- Functions
- Built-in functions
- String slicing

## Program 2: Factor Finder
This function returns a list of all factors of a given integer. A factor is any number that divides the integer exactly with no remainder.

What it does:
- Iterates through all numbers from 1 to n
- Checks divisibility using the modulus operator

Python concepts used:
- Functions
- Loops (for)
- Lists
- Modulus operator (%)

## Program 3: Prime Number Checker
This function checks whether a given integer is a prime number. A prime number is greater than 1 and has no divisors other than 1 and itself.

What it does:
- Rejects values less than or equal to 1
- Tests divisibility by numbers from 2 to n-1

Python concepts used:
- Functions
- Conditional statements
- Loops
- Boolean return values

## Program 4: Simple Message Encryption
This function performs a simple form of encryption by:
- Removing all spaces from a message
- Reversing the resulting string

Python concepts used:
- String methods (replace)
- String slicing
- Functions

## Program 5: Hidden Message Encryption
This function hides a message inside random letters to make it harder to read.

What it does:
- Randomly chooses an interval between 2 and 20
- Inserts random lowercase letters between each character of the message
- Returns both the encrypted message and the interval used

Python concepts used:
- Functions
- Random number generation
- Nested loops
- String concatenation
- random and string modules

## Program 6: Hidden Message Decryption
This program decrypts a message that was encrypted using a fixed interval.
It reconstructs the original message by extracting every nth character.

What it does:
- Reads characters at fixed steps through the encrypted message
- Rebuilds the original hidden message

Python concepts used:
- Function
- Loops with step values
- String indexing

