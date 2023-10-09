"""
Task:
    Read line number 4 from the 'test_file_1.txt'.
"""
if __name__ == "__main__":
    with open("test_files/test_file_1.txt", "r") as file:
        current_line = 0
        line_to_read = 4
        for line in file:
            if current_line == line_to_read - 1:
                print(line)
                break
            current_line += 1
