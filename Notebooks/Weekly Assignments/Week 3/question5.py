'''
This program repeatedly asks the user to choose a password
until all conditions are met:
- Passwords must match
- Length must be between 8 and 12 characters
- Password must not be a common password
The program only ends once a valid password is set.
'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
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
        break