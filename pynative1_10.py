#Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

import random

def RandomListGen():
    numbers_list = []
    for x in range(0,10): #quantity of numbers in single list
        n = random.randint(-100,100) #range of generated integer numbers
        numbers_list.append(n)
    return numbers_list

list1 = RandomListGen() #randomly generated list
list2 = RandomListGen() #randomly generated list
list3 = [] #output list
print(list1)
print(list2)

for x in list1:
    if(x%2!=0):
        list3.append(x)

for x in list2:
    if(x%2==0):
        list3.append(x)

print("Result list is", list3)