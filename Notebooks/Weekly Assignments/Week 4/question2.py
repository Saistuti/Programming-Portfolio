'''
This function takes a string as input and counts how many uppercase
and lowercase letters it contains.
It returns both counts as a tuple.
A test program is included to display the result.
'''

def count_case(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

# Testing the program
message = input("Enter a string: ")
u, l = count_case(message)
print("Uppercase letters:", u)
print("Lowercase letters:", l)