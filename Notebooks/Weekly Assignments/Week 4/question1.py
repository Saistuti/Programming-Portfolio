'''
This function checks whether a given integer lies within the range
0 to 100 inclusive.
It returns True if the value is valid and False otherwise.
A short test program is included to demonstrate its use.
'''

def is_valid_mark(value):
    return 0 <= value <= 100

# Testing the program
num = int(input("Enter an integer: "))
print(is_valid_mark(num))