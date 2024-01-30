"""
    Program accepts any three words from one input() call.
"""

words = input("Enter any three words with spaces between them: ")
result = words.split(" ")
print(f"Passed words are: {' '.join(result)}")
