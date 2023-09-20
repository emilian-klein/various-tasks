#Print multiplication table form 1 to 10

from array import *
rows = 10
columns = 10
output_table = [[0 for x in range(rows)] for y in range(columns)]

for x in range(1,11):
    for y in range(1,11):
        output_table[x-1][y-1] = x*y

for x in range(1,11):
    for y in range(1,11):
        print(output_table[x-1][y-1], end=" ")
        if(y==10):
            print("")