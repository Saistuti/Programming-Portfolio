'''
These functions compare the letters used in two words.
Each function returns a sorted list of unique letters.
'''

def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_one_only(word1, word2):
    return sorted(set(word1) ^ set(word2))

# Testing the program
w1 = "cheese"
w2 = "bread"

print(letters_in_either(w1, w2))
print(letters_in_both(w1, w2))
print(letters_in_one_only(w1, w2))