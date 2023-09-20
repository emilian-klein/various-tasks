#Calculate income tax for the given income by adhering to the below rules

print("""==========
Taxable Income	 Rate (in %)
First $10,000	 0
Next $10,000	 10
The remaining	 20
==========""")

while(True):
    income = int(input("Enter your income [$]: "))
    if(income<=10000):
        print("Income tax = 0 $")
    elif(income>10000 and income<=20000):
        level1_tax = (income - 10000) * 0.1
        print("Income tax = ", level1_tax)
    elif(income>20000):
        level1_tax = 10000 * 0.1
        level2_tax = level1_tax + (income - 20000)*0.2
        print("Income tax = ", round(level2_tax, 2))
