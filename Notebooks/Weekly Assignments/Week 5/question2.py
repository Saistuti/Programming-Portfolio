'''
This program reports how many command-line arguments were provided.
The program name itself is not counted as an argument.
'''

import sys

argument_count = len(sys.argv) -1
print("Number of arguments provided: ", argument_count)