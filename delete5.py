#Write a function solution that, given an integer N, returns the maximum possible value obtainable by deleting one '5' digit
#from the decimal representation of N. It is guaranteed that N will contain at least one '5' digit.

def solution(N):

    indexes = []
    all_possibilities = []

    if(N>0):
        converted_N = [int(x) for x in str(N)] #converting N into list containing single digits
        for index, element in enumerate(converted_N): #finding indexes where 5 is
            if(element == 5):
                indexes.append(index)
        for element in indexes: #creating all possible numbers with deleted single 5
            temp_N = converted_N.copy()
            temp_N.pop(element)
            temp_N = [str(x) for x in temp_N]
            temp_N = ''.join(temp_N)
            temp_N = int(temp_N)
            all_possibilities.append(temp_N)
        return max(all_possibilities) #returning maximum value 
    elif(N<0):
        N = abs(N) #getting rid of minus sign
        converted_N = [int(x) for x in str(N)] #converting N into list containing single digits
        for index, element in enumerate(converted_N): #finding indexes where 5 is
            if(element == 5):
                indexes.append(index)
        for element in indexes: #creating all possible numbers with deleted single 5
            temp_N = converted_N.copy()
            temp_N.pop(element)
            temp_N = [str(x) for x in temp_N]
            temp_N = ''.join(temp_N)
            temp_N = int(temp_N)
            all_possibilities.append(temp_N)
        all_possibilities = [x * -1 for x in all_possibilities] #assigning minus to every number
        return max(all_possibilities) #returning maximum value 
    else:
        return 0

#checking correctness
examples = [15958, -5859, -5000]

for N in examples:
     result = solution(N)
     print(result)