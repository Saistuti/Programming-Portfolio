'''
This program counts the number of lines and characters in a file.
It is a simplified version of the Unix 'wc' command.
'''

import sys

if len(sys.argv) < 2:
    print("Error: No file name provided.")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        char_count = sum(len(line) for line in lines)
    
    print("Lines: ", line_count)
    print("Characters: ", char_count)
except FileNotFoundError:
    print("Error: File not found.")