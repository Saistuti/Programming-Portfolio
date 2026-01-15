# Week 8 : Python Command-Line Utilities
This repository contains a collection of small Python programs that reimplement simplified versions of common Unix commands. The purpose of these programs is to demonstrate understanding of:
- Command-line arguments
- File handling
- Core Python data structures
- Clear and readable problem-solving approaches

## Program 1: Number Lines
A simple implementation of the Unix nl command.

What it does:
- Takes a file name as a command-line argument
- Prints each line of the file with a line number at the start

Python concepts used:
- sys.argv
- File handling with open()
- enumerate()
- Strong formatting

## Program 2: File Comparison
A simple implementation of the Unix diff command.

What it does:
- Takes two file names as command-line arguments
- Compares their contents
- Reports whether the files are the same or different

Python concepts used:
- File reading
- String comparison
- Exception handling (try/except)

## Program 3: Search for Text
A basic implementation of the Unix grep command.

What it does:
- Takes a search string and a file name as arguments
- Prints all lines in the file that contain the search string
- Search is case-insensitive

Python concepts used:
- Command-line arguments
- String methods
- Loops
- Case-insensitive comparison

## Program 4: Line and Character Count
A simplified version of the Unix wc command.

What it does:
- Takes a file name as a command-line argument
- Prints the number of lines and characters in the file

Python concepts used:
- File reading
- Lists
- Built-in functions(len, sum)

## Program 5: Simple Spell Checker
A basic spell-checking program inspired by the Unix spell command.

What it does:
- Takes a text file and a dictionary file as arguments
- Prints words that do not appear in the dictionary
- Ignores punctuation and case

Python concepts used:
- Sets for fast lookup
- Dictionaries
- String cleaning
- string.punctuation
- File handling

## Supporting Files
sample.txt and words.txt

These are sample text files used to test the programs. They are used by question1.py, question2.py, question3.py, question4.py and question5.py
