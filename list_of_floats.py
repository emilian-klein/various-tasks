"""
    Program accept a list of 5 float numbers as an input from the user.
"""

try:
    numbers_list = []
    for _ in range(5):
        number = input("Enter a float number: ")
        numbers_list.append(float(number))
    print(numbers_list)
except ValueError:
    print("Pass a valid float number!")
