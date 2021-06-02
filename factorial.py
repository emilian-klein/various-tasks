#Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

def factorial(number):
    if(number == 0):
        return 0
    else:
        result = 1
        for x in range(1,number+1):
            result = result * x
        return result

print(factorial(3))
print(factorial(5))
print(factorial(13))