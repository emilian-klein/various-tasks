#Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

y = 1
x = 1

while x <= 5:
    x = str(x)
    print (y*(x + " "))
    x = int(x)
    x = x + 1
    y = y + 1
