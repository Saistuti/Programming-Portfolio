'''
This function takes a string and returns a sorted list
containing all unique letters used in the string.
'''

def unique_letters(text):
    return sorted(set(text))

# Testing the program
print(unique_letters("cheese"))