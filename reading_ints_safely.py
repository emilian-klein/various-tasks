"""
    Program is able to accept an integer value and to check if it is within a specified range.
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

read_int_safely("Enter a number from -10 to 10: ", -10, 10)
