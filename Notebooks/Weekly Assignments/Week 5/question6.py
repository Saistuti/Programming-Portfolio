'''
This program takes the name of a file as a command-line argument
and creates a backup copy of it.
The backup file contains an exact copy of the original contents
and has a different name.
'''

import sys
import shutil

if len(sys.argv) < 2:
    print("Error: No file name provided.")
    sys.exit()

filename = sys.argv[1]
backup_name = filename + ".bak"

try:
    shutil.copy(filename, backup_name)
    print("Backup created:", backup_name)
except FileNotFoundError:
    print("Error: File not found.")