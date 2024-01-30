"""
    Program takes an integer and returns the factorial of that integer.
    That is, the integer multiplied by all positive lower integers.
"""

def factorial(number):
    if number == 0:
        return 0
    else:
        result = 1
        for x in range(1, number+1):
            result *= x
        return result

test_numbers = [3, 5, 10]
for number in test_numbers:
    print(factorial(number))
