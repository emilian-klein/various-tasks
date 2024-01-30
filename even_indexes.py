"""
    Program from given string displays only those characters which are present at an even index number.
"""

while True:
    word = input("Original string is: ")
    print("Characters at even indexes:", word[::2])
