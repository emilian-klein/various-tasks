"""
Task:
    Given a string and an integer number n, remove characters from a string starting from zero up to n.
    Return a new string.
"""


def remove_characters(string, n):
    return string[n:]


if __name__ == "__main__":
    while True:
        try:
            string = input("Enter string: ")
            n = int(input("Enter a 'n' number: "))
            if n > len(string):
                print("Pass a 'n' which is smaller than length of previously entered word!")
            else:
                result = remove_characters(string=string, n=n)
                print(result)
        except KeyboardInterrupt:
            exit()
