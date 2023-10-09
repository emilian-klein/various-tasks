"""
Task:
    Your task is to write a function able to input integer values and to check if they are within a specified range.

    The function should:

    - Accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
    - if the user enters a string that is not an integer value, the function should emit the message:
      "Error: wrong input" and ask the user to input the value again;
    - if the user enters a number which falls outside the specified range, the function should emit the message
      "Error: the value is not within permitted range (min..max)" and ask the user to input the value again;
    - if the input value is valid, return it as a result.
"""


def read_int_safely(prompt, minimum, maximum):
    try:
        value = int(input(prompt))
        assert minimum <= value <= maximum
    except ValueError:
        print("Error: wrong input!")
        return None
    except AssertionError:
        print(f"Error: the value is not within permitted range ({minimum} - {maximum})!")
        return None
    else:
        print(f"The number is: {value}")
        return value


def main():
    try:
        while True:
            read_int_safely("Enter a number from -10 to 10: ", -10, 10)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
