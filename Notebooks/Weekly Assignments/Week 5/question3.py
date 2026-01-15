'''
This program takes multiple command-line arguments and prints
the shortest one.
If no arguments are provided, it prints an error message and exits.
'''

import sys

args = sys.argv[1:]

if not args:
    print("Error: No arguments provided.")
else:
    args.sort(key=len)
    print("Shortest argument:", args[0])