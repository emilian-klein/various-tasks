"""
Task:
    Reverse a given number and return True if it is the same as the original number.
"""


def is_palindrome_number(number):
    reversed_number = str(number)[::-1]
    if int(reversed_number) == number:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter any number: "))
            if is_palindrome_number(number=number):
                print("The original and reversed number are the same!")
            else:
                print("The original and reversed number are not the same!")
        except ValueError:
            print("Enter valid number!")
        except KeyboardInterrupt:
            exit()
