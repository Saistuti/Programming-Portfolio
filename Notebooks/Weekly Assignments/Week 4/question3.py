'''
This program asks the user for their name and ensures that it is
displayed with the first letter in uppercase and the remaining
letters in lowercase, regardless of how the user typed it.
'''

name = input("Enter your name: ")

if name == "":
    print("Hello, Stranger!")
else:
    formatted_name = name.capitalize()
    print(f"Hello, {formatted_name}. Good to meet you!")
