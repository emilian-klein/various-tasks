"""
Task:
    Program returns an int value of base raises to the power of exp.
"""

def exponent(base, exp):
    return base**exp

while True:
    try:
        base = int(input("Base = "))
        exp = int(input("Exponent = "))
        if exp > 0:
            result = exponent(base, exp)
            print(f"{base} raised to the power of {exp} is: {result}")
        else:
            raise ValueError
    except ValueError:
        print("Pass valid value!")
