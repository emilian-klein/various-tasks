#Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def removeChars(word,n):
    print(word[n:])

word = input("Enter any word: ")
while True:
    n = int(input("Enter a n number: "))
    if(n > len(word)):
        print("Pass a number which is smaller than lenght of previously entered word!")
    else:
        break

removeChars(word,n)