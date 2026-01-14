'''
This program improves password security by preventing the use
of common passwords.
The password must match, be between 8 and 12 characters long,
and must not be one of the predefined bad passwords.
'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter new password: ")
password2 = input("Confirm password: ")

if password1 != password2:
    print("Error: Passwords do not match")
elif len(password1) < 8 or len(password2) > 12:
    print("Error: Password must be between 8 and 12 characters long")
elif password1.lower() in BAD_PASSWORDS:
    print("Error: Password is too common")
else:
    print("Password Set")