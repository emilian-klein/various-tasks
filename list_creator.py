"""
    Program generates two lists and later creates new list based on odd numbers from the first list and even numbers from the second list.
"""

import random

def generate_random_list():
    return [random.randint(0, 50) for _ in range(5)]

def get_even_numbers_from(numbers_list):
    even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers_list)
    return list(even_numbers_iterator)

def get_odd_numbers_from(numbers_list):
    odd_numbers_iterator = filter(lambda x: (x % 2 != 0), numbers_list)
    return list(odd_numbers_iterator)

def create_new_list(list1, list2):
    return get_odd_numbers_from(list1) + get_even_numbers_from(list2)

list1 = generate_random_list()
print(f"List1: {list1}")
list2 = generate_random_list()
print(f"List2: {list2}")
result = create_new_list(list1=list1, list2=list2)
print(f"Result: {result}")

