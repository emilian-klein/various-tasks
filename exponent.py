"""
Task:
    Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
"""


def exponent(base, exp):
    return base**exp


if __name__ == "__main__":
    while True:
        try:
            base = int(input("Base = "))
            exp = int(input("Exponent = "))
            if exp > 0:
                result = exponent(base, exp)
                print(f"{base} raised to the power of {exp} is: {result}")
            else:
                print("Pass a non-negative exponent!")
        except KeyboardInterrupt:
            exit()
        except ValueError:
            print("Pass valid value!")
