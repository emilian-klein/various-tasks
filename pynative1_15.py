#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

def exponent(base, exp):
    return base**exp

while(True):
    base = int(input("Base = "))
    exp = int(input("Exponent = "))
    if(exp>0):
        solution = exponent(base, exp)
        print("{} rasied to the power of {} is: {}".format(base,exp,solution))
    else:
        print("Pass a non-negative exponent!")