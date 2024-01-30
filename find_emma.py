"""
    Program counts of how many sub-strings 'Emma' are hidden in the given string.
"""

sentence = input("Pass sentence: ")
substring_occurrences = sentence.count("Emma")
print(f"'Emma' appeared {substring_occurrences} times in sentence above.")
