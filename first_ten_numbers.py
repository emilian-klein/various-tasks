"""
Task:
    Given a range of the first 10 numbers, iterate from the start number to the end number.
    In each iteration print the sum of the current number and previous number.
"""
if __name__ == "__main__":
    for number in range(10):
        if number == 0:
            print(f"{number} + - = {number}")
        else:
            print(f"{number} + {number - 1} = {number + (number - 1)}")
