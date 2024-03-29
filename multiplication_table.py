"""
    Program prints on the screen multiplication table form 1 to 10.
"""

table = [
        [" ", "|", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["1", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["2", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["3", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["4", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["5", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["6", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["7", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["8", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["9", "|", "", "", "", "", "", "", "", "", "", "", ""],
        ["10", "|", "", "", "", "", "", "", "", "", "", "", ""],
]

for x in range(2, 12):
    for y in range(2, 12):
        table[x][y] = (x - 1) * (y - 1)

for row in table:
    for item in row:
        print("{:2s} ".format(str(item)), end="")
    print()
