#Given a list of random generated numbers, Iterate it and print only those numbers which are divisible of 5

import random, time

def RandomListGen():
    numbers_list = []
    for x in range(0,20): #quantity of numbers in single list
        n = random.randint(0,100) #range of generated integer numbers
        numbers_list.append(n)
    return numbers_list

def IsDevisible(numberslist):
    print("Devisible numbers of 5 from the list above are:")
    for x in numberslist:
        if(x % 5 == 0):
            print(x)

x = 0
while x < 25:
    test_list = RandomListGen()
    print(test_list)
    IsDevisible(test_list)
    print("===========") 
    time.sleep(10)