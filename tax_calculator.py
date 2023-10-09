"""
Task:
    Calculate income tax for the given income by adhering to the below rules:

    Income	        Rate (in %)
    ---------------------------
    First $10,000	0
    Next $10,000	10
    The remaining	20
"""


def calculate_tax(income):
    if income <= 10000:
        result = 0
    elif 10000 < income <= 20000:
        result = (income - 10000) * 0.10
    elif income > 20000:
        result = 1000 + ((income - 20000) * 0.20)
    return "{:.2f}".format(result)


if __name__ == "__main__":
    while True:
        try:
            income = float(input("Enter your income [$]: "))
            print(f"Calculated tax: {calculate_tax(income)}")
        except ValueError:
            print("Pass valid income!")
        except KeyboardInterrupt:
            exit()
