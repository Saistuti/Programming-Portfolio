'''
This program performs frequency analysis on a message.
It counts how often each letter appears (case-insensitive)
and reports the six most common letters with their counts.
Non-letter characters are ignored.
'''

message = input("Enter a message: ").lower()

counts = {}

for char in message:
    if char.isalpha():
        counts[char] = counts.get(char, 0) + 1

sorted_letters = sorted(counts.items(), key = lambda x: x[1], reverse = True)

for letter, count in sorted_letters[:6]:
    print(letter, ":", count)