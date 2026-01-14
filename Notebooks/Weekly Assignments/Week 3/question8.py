'''
This program prints a multiplication table based on user input.
If the number is positive, the table is printed from 0 to 12.
If the number is negative, the table is printed backwards
from 12 down to 0 using the absolute value of the number.
'''

number = int(input("Enter a number: "))

if abs(number) > 12:
    print("Error: Number must be between -12 and 12")
else:
    if number >= 0:
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
    else:
        for i in range(12, -1, -1):
            print(f"{i} x {abs(number)} = {i * abs(number)}")
            