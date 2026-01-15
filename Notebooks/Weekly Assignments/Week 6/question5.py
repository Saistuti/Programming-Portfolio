'''
This function hides a message inside random letters.
It randomly chooses an interval between 2 and 20.
Each character of the message is placed at that interval,
with random letters filling the gaps.
The function returns the encrypted message and the interval used.
'''

import random
import string

def hide_message(message):
    interval = random.randint(2, 20)
    encrypted = ""

    for char in message:
        encrypted += char
        for _ in range(interval - 1):
            encrypted += random.choice(string.ascii_lowercase)

    return encrypted, interval

# Testing the program
encrypted_text, step = hide_message("send cheese")
print("Encrypted:", encrypted_text)
print("Interval:", step)