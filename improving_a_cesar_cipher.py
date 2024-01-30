"""
    The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
    Program allows the shifted value to come from the range 1..25 inclusive. Moreover, it lets the code preserve the letters' case.
    It asks the user for one line of text to encrypt and for a shift value so that it could print encoded text.
"""

def ask_for_sentence_to_encrypt():
    sentence_to_encrypt = input("Sentence to encrypt: ")
    return sentence_to_encrypt

def ask_for_shift_value():
    while True:
        try:
            shift_value = int(input("Shift value: "))
            if shift_value < 1 or shift_value > 25:
                raise ValueError
            else:
                return shift_value
        except ValueError:
            print("That's not a valid integer.")
            continue

def encrypt_message(sentence_to_encrypt, shift_value):
    encrypted_sentence = ""
    for char in sentence_to_encrypt:
        if char.isalpha():
            if char.isupper():
                encrypted_sentence += chr((ord(char) - 65 + shift_value) % 26 + 65)
            else:
                encrypted_sentence += chr((ord(char) - 97 + shift_value) % 26 + 97)
        else:
            encrypted_sentence += char
    return encrypted_sentence

sentence_to_encrypt = ask_for_sentence_to_encrypt()
shift_value = ask_for_shift_value()
encrypted_sentence = encrypt_message(sentence_to_encrypt, shift_value)
print("Encrypted sentence:", encrypted_sentence)
