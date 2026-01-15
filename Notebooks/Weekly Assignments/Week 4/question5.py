'''
These functions convert temperatures between centigrade and fahrenheit.
One function converts centigrade to fahrenheit and the other does
the reverse. Both functions are tested with example values.
'''

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Testing the program
print("25C in Fahrenheit: ", c_to_f(25))
print("77F in Centigrade: ", f_to_c(77))
