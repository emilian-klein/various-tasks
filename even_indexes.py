"""
Task:
    Given a string, display only those characters which are present at an even index number.
"""
if __name__ == "__main__":
    while True:
        try:
            word = input("Original string is: ")
            print("Characters at even indexes:", word[::2])
        except KeyboardInterrupt:
            exit()
