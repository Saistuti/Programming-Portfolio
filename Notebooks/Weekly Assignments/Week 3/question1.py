'''
This program asks the user to enter their name.
If the user presses Enter without typing a name,
the program displays the greeting "Hello, Stranger!".
Otherwise, it greets the user using the name they entered.
'''

name = input("Hello, what is your name? ")

if name == "":
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}. Good to meet you!")