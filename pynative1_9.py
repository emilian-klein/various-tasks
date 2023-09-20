#Reverse a given number and return true if it is the same as the original number

while(True):
    given_number = input("Enter any number: ")
    reversed_number = given_number[::-1]

    if(given_number == reversed_number):
        print("The original and reversed number are the same")
    else:
        print("The original and reversed number are not the same")
    