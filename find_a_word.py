"""
    Program takes two strings: one being a word (e.g., "dog") and the second being a combination of any characters. Then it checks if characters comprising the
    first string are hidden inside the second string?
"""

def get_text(message):
    text = input(message)
    return text

def find_chars(word, char_combination):
    word = word.strip().lower()
    char_combination = char_combination.strip().lower()
    char_combination = list(char_combination)
    for char in word:
        if char in char_combination:
            char_index = char_combination.index(char)
            char_combination.pop(char_index)
        else:
            return False
    return True

while True:
    word = get_text("Pass word: ")
    char_combination = get_text("Pass character combination: ")
    if find_chars(word, char_combination):
        print(f"Word '{word}' can be constructed using characters in '{char_combination}'")
    else:
        print(f"Word '{word}' can NOT be constructed using characters in '{char_combination}'")
