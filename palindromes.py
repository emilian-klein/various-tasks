"""
    Program:
    - asks the user for some text,
    - checks whether the entered text is a palindrome, and prints result,
    - it assumes that an empty string isn't a palindrome,
    - it treats upper-case and lower-case letters as equal,
    - spaces are not taken into account during the check.
"""

def ask_for_sentence_to_check():
    sentence_to_check = input("Sentence to check: ")
    return sentence_to_check

def is_palindrome(sentence):
    sentence = delete_whitespaces(sentence)
    sentence = sentence.casefold()
    if len(sentence) == 0:
        print("It is not a palindrome.")
    elif sentence == sentence[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

def delete_whitespaces(sentence):
    sentence = "".join(sentence.split())
    return sentence

while True:
    sentence = ask_for_sentence_to_check()
    is_palindrome(sentence)
