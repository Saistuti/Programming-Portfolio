'''
This program searches a file for lines containing a given string.
It prints all lines that contain the search pattern.
This is a simple version of the Unix 'grep' command.
'''

import sys

if len(sys.argv) < 3:
    print("Error: Search string and file name required.")
    sys.exit()

pattern = sys.argv[1]
filename = sys.argv[2]

try:
    with open(filename, "r") as file:
        for line in file:
            if pattern in line:
                print(line.rstrip())
except FileNotFoundError:
    print("Error: File not found.")