"""
    Program formats the following data using a string.format() method:
    - total_money = 1000
    - quantity = 3
    - price = 450
"""

total_money = 1000
quantity = 3
price = 450
sentence = "I have {} dollars so I can buy {} football for {:.2f} dollars."
print(sentence.format(total_money, quantity, price))
