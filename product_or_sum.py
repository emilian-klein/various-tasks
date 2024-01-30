"""
    Program calculates product of two numbers but if the product is greater than 1000, then it calculates their sum.
"""

def product_or_sum(number1, number2):
    if number1 * number2 > 1000:
        return number1 + number2
    else:
        return number1 * number2

try:
    number1 = int(input("number1 = "))
    number2 = int(input("number2 = "))
    final_answer = product_or_sum(number1=number1, number2=number2)
    print(f"The result is: {final_answer}.")
except ValueError:
    print("Pass valid number!")
