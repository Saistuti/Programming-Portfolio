'''
This program implements a simple version of the Unix 'nl' command.
It takes a file name as a command-line argument and prints each line
of the file preceded by its line number.
'''

import sys

if len(sys.argv) < 2:
    print("Error: No file name provided.")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        for number, line in enumerate(file, start = 1):
            print(f"{number}\t{line.rstrip()}")
except FileNotFoundError:
    print("Error: File not found.")