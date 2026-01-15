'''
This program reads six centigrade temperatures entered in the format
<number>C. It converts them to numeric values and then displays
the maximum, minimum, and mean temperature.
'''

import statistics

temps = []

for i in range(6):
    temp_input = input("Enter temperature: ")
    temps.append(float(temp_input[:-1]))

print("Maximum: ", max(temps))
print("Minimum: ", min(temps))
print("Mean: ", statistics.mean(temps))