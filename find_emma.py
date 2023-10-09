"""
Task:
    Print the count of sub-string 'Emma' in the given string.
"""
if __name__ == "__main__":
    while True:
        try:
            sentence = input("Pass sentence: ")
            substring_occurrences = sentence.count("Emma")
            print(f"'Emma' appeared {substring_occurrences} times in sentence above.")
        except KeyboardInterrupt:
            exit()
