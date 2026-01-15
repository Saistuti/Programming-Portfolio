'''
This program reads any number of centigrade temperatures entered
in the format <number>C.
Input ends when the user presses Enter without typing a value.
The program then displays the maximum, minimum, and mean.
'''

import statistics

temps = []

while True:
    temp_input = input("Enter temperature: ")

    if temp_input == "":
        break

    temps.append(float(temp_input[:-1]))

if temps:
    print("Maximum: ", max(temps))
    print("Minimum: ", min(temps))
    print("Mean: ", statistics.mean(temps))
else:
    print("No temperatures entered.")