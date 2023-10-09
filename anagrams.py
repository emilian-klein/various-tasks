"""
Task:
    Write a program which asks the user for two separate texts and checks whether, the entered texts are anagrams
    and prints the result. Assume that two empty strings are not anagrams, treat upper- and lower-case letters as equal.
    Spaces are not taken into account during the check - treat them as non-existent.
"""


def get_text(message):
    text = input(message)
    return text


def delete_whitespaces(text):
    text_no_whitespaces = "".join(text.split())
    return text_no_whitespaces


def count_characters(text):
    counted_characters = {}
    for char in text:
        char_occurrences = text.count(char)
        if char not in counted_characters.keys():
            counted_characters[char] = char_occurrences
    return counted_characters


def is_anagram(text1, text2):
    text1 = delete_whitespaces(text1)
    text2 = delete_whitespaces(text2)
    if len(text1) == 0 and len(text2) == 0:
        print("It is not an anagram.")
    else:
        text1_chars = count_characters(text1.lower())
        text2_chars = count_characters(text2.lower())
        if text1_chars == text2_chars:
            print("It is an anagram.")
        else:
            print("It is not an anagram.")


def main():
    try:
        while True:
            text1 = get_text("Pass first sentence: ")
            text2 = get_text("Pass second sentence: ")
            is_anagram(text1, text2)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
