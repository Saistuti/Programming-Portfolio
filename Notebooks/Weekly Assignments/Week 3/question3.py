'''
This program checks whether a chosen password is valid.
The password must be entered twice and both entries must match.
Additionally, the password length must be between 8 and 12
characters inclusive.
'''

password1 = input("Enter new password: ")
password2 = input("Confirm password: ")

if password1 != password2:
    print("Error: Passwords do not match")
elif len(password1) < 8 or len(password2) > 12:
    print("Error: Password must be between 8 and 12 characters long")
else:
    print("Password Set")