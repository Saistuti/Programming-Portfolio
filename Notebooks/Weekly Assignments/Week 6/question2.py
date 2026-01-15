'''
This function takes an integer and returns a list of all its factors.
A factor is any integer that divides the number exactly with no remainder.
'''

def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
        
    return result

# Testing the program
print(factors(15))  