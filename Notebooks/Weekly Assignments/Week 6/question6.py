'''
This program decrypts a message that was encrypted using a fixed interval.
It extracts every nth character from the encrypted message
to reconstruct the original message.
'''

def reveal_message(encrypted, interval):
    message = ""
    for i in range(0, len(encrypted), interval):
        message += encrypted[i]
    return message

# Testing the program
encrypted = "sxyexynxydxycxyhxyexyexysxye"
interval = 3
print(reveal_message(encrypted, interval))
