"""
Task:
    Print the following pattern:
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
"""
if __name__ == "__main__":
    for x in range(1, 6):
        print(" ".join(str(x) * x))
