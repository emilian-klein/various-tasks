#Given two integer numbers return their product. If the product is greater than 1000, then return their sum

def answer(number1, number2):
    if(number1*number2>1000):
        return number1 + number2
    else:
        return number1 * number2 

number1 = int(input("number1 = "))
number2 = int(input("number2 = "))

final_answer = answer(number1,number2)
print("The result is:", final_answer)