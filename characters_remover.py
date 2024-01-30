"""
    Given a string and an integer n, the program removes characters from the beginning (index 0) of the string up to the n-th position.
"""

def remove_characters(string, n):
    return string[n:]

while True:
    try:
        string = input("Enter string: ")
        n = int(input("Enter a 'n' number: "))
        if n > len(string):
            print("Pass a 'n' which is smaller than length of previously entered word!")
        else:
            result = remove_characters(string=string, n=n)
            print(result)
    except ValueError:
        print("Pass a correct value!")
