"""
    Program iterates from 0 to 10. In each iteration it prints the sum of the current number and previous number.
"""

for number in range(10):
    if number == 0:
        print(f"{number} + - = {number}")
    else:
        print(f"{number} + {number - 1} = {number + (number - 1)}")
