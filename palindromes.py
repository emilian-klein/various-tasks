"""
Task:
    Your task is to write a program which:
    - asks the user for some text;
    - checks whether the entered text is a palindrome, and prints result.
Note:
    - assume that an empty string isn't a palindrome;
    - treat upper-case and lower-case letters as equal;
    - spaces are not taken into account during the check - treat them as non-existent;
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


def main():
    try:
        while True:
            sentence = ask_for_sentence_to_check()
            is_palindrome(sentence)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
