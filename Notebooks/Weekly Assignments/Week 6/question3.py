'''
This function determines whether a given integer is a prime number.
A prime number is greater than 1 and has no factors other than 1 and itself.
'''

def prime_num(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

# Testing the program
print(prime_num(12))   
print(prime_num(5))    