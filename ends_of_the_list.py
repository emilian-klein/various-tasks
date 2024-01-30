"""
    Program generates a list with 12 random generated numbers which are in range between 0 and 10.
    It returns True if first and last number of that list are the same.
"""

import random

def generate_random_list():
    return [random.randint(0, 10) for _ in range(12)]

def check_list(list_to_check):
    if list_to_check[0] == list_to_check[-1]:
        return True
    else:
        return False

random_list = generate_random_list()
print(f"Generated list: {random_list}")
result = check_list(random_list)
print(result)
