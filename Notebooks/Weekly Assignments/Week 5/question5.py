'''
This program takes a collection of temperature values from the
command line and displays the maximum, minimum, and mean.
If no values are provided, the program exits with an error message.
'''

import sys
import statistics

args = sys.argv[1:]

if not args:
    print("Error: No temperature  values provided.")
    sys.exit()

temps = [float(t) for t in args]

print("Maximum: ", max(temps))
print("Minimum: ", min(temps))
print("Mean: ", statistics.mean(temps))
