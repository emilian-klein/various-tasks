"""
Task:
    Given a list of random generated numbers iterate it and print only those numbers which are divisible of 5.
"""
import random
import time


def generate_random_list():
    return [random.randint(0, 100) for _ in range(10)]


def is_divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        try:
            random_list = generate_random_list()
            print(f"Generated list: {random_list}")
            for number in random_list:
                if is_divisible_by_5(number=number):
                    print(number, end=" ")
            print()
            time.sleep(5)
        except KeyboardInterrupt:
            exit()
