'''
This program prompts the user to enter a temperature in Celsius.
It converts the given temperature into Fahrenheit using the formaula:
Fahrenheit = (Celsius x 9/5) + 32
Finally, it displays the converted temperature.
'''

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}C is equivalent to {fahrenheit}F.")
