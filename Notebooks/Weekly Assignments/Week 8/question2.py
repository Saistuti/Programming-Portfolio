'''
This program compares two files and reports whether their contents
are exactly the same.
It is a simple implementation of the Unix 'diff' command.
'''

import sys

if len(sys.argv) < 3:
    print("Error: Two file names must be provided")
    sys.exit()

file1, file2 = sys.argv[1], sys.argv[2]

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        if f1.read() == f2.read():
            print("The files are the same.")
        else:
            print("Th files are different.")
except FileNotFoundError:
    print("Error: One or both files not found.")