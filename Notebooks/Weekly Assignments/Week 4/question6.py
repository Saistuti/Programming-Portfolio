'''
This program reads a temperature in centigrade entered in the format
<number>C, converts it to fahrenheit, and displays the result in
the same format.
'''

temp_input = input("Enter temperature in centigrade: ")

value = float(temp_input[:-1])
fahrenheit = (value * 9/5) + 32

print(f"{fahrenheit}F")