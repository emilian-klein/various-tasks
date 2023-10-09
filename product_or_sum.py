"""
Task:
    Given two integer numbers return their product. If the product is greater than 1000, then return their sum.
"""


def product_or_sum(number1, number2):
    if number1 * number2 > 1000:
        return number1 + number2
    else:
        return number1 * number2 


if __name__ == "__main__":
    while True:
        try:
            number1 = int(input("number1 = "))
            number2 = int(input("number2 = "))
            final_answer = product_or_sum(number1=number1, number2=number2)
            print(f"The result is: {final_answer}.")
        except ValueError:
            print("Pass valid number!")
        except KeyboardInterrupt:
            exit()
