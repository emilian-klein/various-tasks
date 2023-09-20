# Count the amount of ones in the binary representation of an integer.
# For example, since 12 is 1100 in binary, the return value should be 2.

def count_ones(number):
    binary_number = (bin(number)[2:])
    print(binary_number)
    return int(binary_number.count('1'))


print(count_ones(12))
print(count_ones(110))
print(count_ones(1102))
