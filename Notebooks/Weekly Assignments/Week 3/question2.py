'''
This program simulates choosing a password.
The user is asked to enter a new password twice.
If both passwords match, the password is accepted.
If they do not match, an error message is displayed.
'''

password1 = input("Enter new password: ")
password2 = input("Confirm passord: ")

if password1 == password2:
    print("Password Set")
else:
    print("Error: Passwords do not match")