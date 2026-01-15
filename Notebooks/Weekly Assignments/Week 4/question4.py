'''
This function removes the last character from a given string.
If the string contains one or fewer characters, it is returned unchanged.
A test program is included.
'''

def remove_last_char(text):
    if len(text) <= 1:
        return text
    return text[:-1]

# Testing the program
word = input("Enter a string: ")
print(remove_last_char(word))