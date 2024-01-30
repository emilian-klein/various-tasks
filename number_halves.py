"""
   Program prints a list containing the two halves of the number.
    If the number is odd, it makes the rightmost number higher.
"""

def number_split(n):
    a = n // 2
    b = n - a
    return [a, b]

test_numbers = [20, 15, -16, -27, 1, 101, -101]
for numbers in test_numbers:
    print(number_split(numbers))
