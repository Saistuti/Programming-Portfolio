# Week 7 : Python Sets and Dictionaries Exercises
This repository contains Python programs that demonstrate the use of sets, dictionaries, and string processing. The exercises focus on extracting unique data, comparing collections, storing information dynamically, and analysing text frequency.

## Program 1: Unique Letters in a String
This function takes a string and returns a sorted list of unique letters used in the string.

What it does:
- Removes duplicate letters using a set
- Sorts the remaining letters alphabetically

Python concepts used:
- Sets
- Type conversion (set to list)
- Sorting
- Functions

## Program 2: Letter Comparison Between Two Words
These functions compare the letters used in two words and return different sets of letters.

Functions included:
- letters_in_either = letters that appear in at least one word
- letters_in_both = letters common to both words
- letters_in_one_omly = letters that appear in only one of the words

Python concepts used:
- Set operations ( |, &, ^)
- Functions
- Sorting

## Program 3: Country & Capital Dictionary
This interactive program stores country names and their capital cities.
If a capital is unknown, the user is prompted to provide it.
The program continues until the user presses Enter without typing a country name.

Key features:
- Case-insensitive country handling
- Dynamic dictionary updates
- Continuous user interaction

Python concepts used:
- Dictionaries
- Loops (while)
- Conditional logic
- String methods (lower(), strip(), title())

## Program 4: Letter Frequency Analysis
This program performs frequency analysis on a message entered by the user.
It counts how often each letter appears and displays the six most common letters.

What it does:
- Converts input to lowercase
- Ignores non-letter characters
- Sorts letters by frequency

Python concepts used:
- Dictionaries
- Loops
- String methids (isalpha(), lower())
- Sorting with lambda expressions
