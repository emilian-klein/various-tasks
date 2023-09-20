#Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number

for x in range(0,10):
    if(x==0):
        print("Current number:", x, "Previous number: -", "Sum:", x)
    else:
        print("Current number:", x, "Previous number:", x-1, "Sum:", x+(x-1))