#Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.

def number_split(n):
    if(n>1):
        if(n%2==0):
            split = int(n/2)
            result = [split, split]
            return result
        elif(n%2!=0):
            split = int(n/2)
            result = [split, split+1]
            return result 
    elif(n<-1):
        n = abs(n)
        if(n%2==0):
            split = int(n/2)
            result = [split, split]
            result = [-1 * x for x in result]
            return result
        elif(n%2!=0):
            split = int(n/2)
            result = [split+1, split]
            result = [-1 * x for x in result]
            return result
    else:
            return None    

print(number_split(20))
print(number_split(15))
print(number_split(-16))
print(number_split(-27))
print(number_split(1))