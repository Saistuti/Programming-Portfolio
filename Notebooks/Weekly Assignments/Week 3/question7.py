'''
This program asks the user to enter a number between 0 and 12.
It then prints the multiplication table for that number
from 0 times to 12 times.
'''

number = int(input("Enter a number between 0 and 12: "))

if 0 <= number <= 12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    print("Error: Number must be between 0 and 12")