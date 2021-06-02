#Create a function that returns True if a given inequality expression is correct and False otherwise.

def correct_signs(inequality):
    results = []
    inequality = inequality.split(' ') #splitting whole string using space
    
    for x in range(0,len(inequality)-1,2):
        temp_inequality = ''.join(inequality[x:3+x]) #creating inequalisties in loop 
        for char in temp_inequality: #searching for inequality symbol
            if(char.isdigit()==False):
                symbol = char
                break
        if(symbol=='>'): #based on found symbol check if inequality is true and return result to results list
            temp_inequality = temp_inequality.split(symbol)
            if(int(temp_inequality[0]) > int(temp_inequality[1])):
                results.append(True)
            else:
                results.append(False)
        elif(symbol=='<'):
            temp_inequality = temp_inequality.split(symbol)
            if(int(temp_inequality[0]) < int(temp_inequality[1])):
                results.append(True)
            else:
                results.append(False)
    
    for result in results: #if False is in results list whole function returns False
        if(result==False):
            return False
    return True #if otherwise return True

print(correct_signs("3 < 7 < 11")) 
print(correct_signs("13 > 44 > 33 > 1")) 
print(correct_signs("1 < 2 < 6 < 9 > 3"))