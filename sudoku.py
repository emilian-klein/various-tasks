"""
    Program reads 9 rows of Sudoku, each containing 9 digits.
    It outputs appropriate information if Sudoku is valid or not.

    Sudoku is valid when:
    - Each row contains unique values from 1-9.
    - Each column contains unique values from 1-9.
    - Each of the 9 sub-squares, of size 3x3, contains a unique value from 1-9.
"""

def get_sudoku_grid():
    sudoku_grid = []
    i = 1
    while len(sudoku_grid) != 9:
        row = input(f"Enter {i} row: ")
        if validate_row(row):
            row = [int(digit) for digit in row]
            sudoku_grid.append(row)
            i += 1
    return sudoku_grid

def validate_row(row):
    if len(row) == 9 and row.isdigit():
        return True
    else:
        print("Provided row is invalid!")
        return False

def show_sudoku(sudoku_grid):
    print("\nCreated sudoku board:")
    for row in sudoku_grid:
        print(row)

def check_sudoku(sudoku_grid):
    unique_values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    if check_rows(sudoku_grid, unique_values) and check_columns(sudoku_grid, unique_values) and check_subsquares(sudoku_grid, unique_values):
        print("\nSudoku is valid!")
    else:
        print("\nSudoku is invalid!")

def check_rows(sudoku_grid, unique_values):
    for row in sudoku_grid:
        if set(row) == unique_values:
            return True
        else:
            return False

def check_columns(sudoku_grid, unique_values):
    columns = get_columns(sudoku_grid)
    for column in columns:
        if set(column) == unique_values:
            return True
        else:
            return False

def get_columns(sudoku_grid):
    columns = []
    for i in range(9):
        columns.append([row[i] for row in sudoku_grid])
    return columns

def check_subsquares(sudoku_grid, unique_values):
    subsquares = get_subsquares(sudoku_grid)
    for subsquare in subsquares:
        if set(subsquare) == unique_values:
            return True
        else:
            return False

def get_subsquares(sudoku_grid):
    subsquares = []
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            subsquare = []
            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    subsquare.append(sudoku_grid[j][i])
            subsquares.append(subsquare)
    return subsquares

sudoku_grid = get_sudoku_grid()
show_sudoku(sudoku_grid)
check_sudoku(sudoku_grid)
