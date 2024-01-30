"""
    Program counts the amount of ones in the binary representation of an integer.
    For example, since 12 is 1100 in binary, the return value will be 2.
"""

def count_ones(number):
    binary_number = bin(number)[2:]
    print(f"Decimal: {number} -> Binary: {binary_number}")
    return int(binary_number.count("1"))

test_values = [12, 110, 1102]
for value in test_values:
    print(f"Counted ones: {count_ones(number=value)}")
