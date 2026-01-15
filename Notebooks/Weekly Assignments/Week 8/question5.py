'''
This program checks the spelling of words in a text file.
It prints all words that are not found in a dictionary file.
Punctuation is ignored and comparison is case-insensitive.
'''

import sys
import string

if len(sys.argv) < 3:
    print("Error: Text file and dictionary file required.")
    sys.exit()

text_file = sys.argv[1]
dict_file = sys.argv[2]

try:
    with open(dict_file, "r") as df:
        dictionary = set(word.strip().lower() for word in df)

    with open(text_file, "r") as tf:
        for line in tf:
            words = line.translate(
                str.maketrans("", "", string.punctuation)
            ).lower().split()

            for word in words:
                if word not in dictionary:
                    print(word)

except FileNotFoundError:
    print("Error: File not found.")
