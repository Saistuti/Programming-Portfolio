'''
This function 'encrypts' a message by removing all spaces
and then reversing the resulting string.
'''

def simple_encrypt(message):
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]

# Testing the program
print(simple_encrypt("hello world"))