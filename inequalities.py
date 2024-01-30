"""
   Program returns True if a given inequality expression is correct and False otherwise.
"""

def check_inequality(inequality):
    results = []
    inequality = inequality.split(" ")
    for index, element in enumerate(inequality):
        if element == "<":
            partial_inequality_result = int(inequality[index - 1]) < int(inequality[index + 1])
            results.append(partial_inequality_result)
        elif element == ">":
            partial_inequality_result = int(inequality[index - 1]) > int(inequality[index + 1])
            results.append(partial_inequality_result)
    return all(results)

print(check_inequality("3 < 7 < 11"))
print(check_inequality("13 > 44 > 33 > 1"))
print(check_inequality("1 < 2 < 6 < 9 > 3"))
print(check_inequality("-10 > 2 < 6 < 9 > 3"))
