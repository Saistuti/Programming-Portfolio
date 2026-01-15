'''
This function accepts a positive integer and returns its binary
(base-2) representation as a string.
The solution uses Python’s built-in binary conversion, which is the
clearest and most obvious approach.
'''

def to_binary(n):
    return bin(n)[2:]


# Testing the program
print(to_binary(10))   
print(to_binary(3))    