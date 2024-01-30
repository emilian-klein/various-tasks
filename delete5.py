"""
    Program finds the maximum possible value obtainable by deleting one '5' digit from the decimal representation of given number.
    It is assumed that number will contain at least one '5' digit.
"""

def convert_number_to_digits_list(number):
    return [int(digit) for digit in str(number)]

def solution(n):
    all_possible_numbers = []
    is_n_positive = n > 0
    digits = convert_number_to_digits_list(abs(n))
    for index, digit in enumerate(digits):
        if digit == 5:
            temp_number = digits[::]
            del temp_number[index]
            possible_number = int(''.join(map(str, temp_number)))
            if is_n_positive:
                all_possible_numbers.append(possible_number)
            else:
                all_possible_numbers.append(possible_number * -1)
    print(max(all_possible_numbers))

test_numbers = [15958, -5859, -5050, 6525, 78565, -154255]
for number in test_numbers:
    solution(number)
