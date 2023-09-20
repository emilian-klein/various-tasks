#Given a list of random generated numbers, return True if first and last number of a list is same

import random, time

def RandomListGen():
    numbers_list = []
    for x in range(0,10):
        n = random.randint(0,10)
        numbers_list.append(n)
    return numbers_list

def ListCheck(numberslist):
    if(numberslist[0]==numberslist[-1]):
        print("True")
    else:
        print("False")

x = 0
while x < 25:
    test_list = RandomListGen()
    print(test_list)
    ListCheck(test_list)
    x = x+1
    time.sleep(3)