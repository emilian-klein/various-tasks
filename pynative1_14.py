#Print downward Half-Pyramid Pattern with Star (asterisk)

for x in range(6, 0, -1):
    for y in range(0, x-1):
        print("*", end = " ")
    print(" ")