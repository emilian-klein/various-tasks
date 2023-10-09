"""
Task:
    Given a number, return a list containing the two halves of the number.
    If the number is odd, make the rightmost number higher.
"""


def number_split(n):
    a = n // 2
    b = n - a
    return [a, b]


if __name__ == "__main__":
    test_numbers = [20, 15, -16, -27, 1, 101, -101]
    for numbers in test_numbers:
        print(number_split(numbers))
