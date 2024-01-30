"""
    Program writes all content of a 'test_file_1.txt' into a new test_file_2.txt by skipping line number 5.
"""
path_to_test_file_1 = "test_file_1.txt"
path_to_test_file_2 = "test_file_2.txt"
with open(path_to_test_file_1, "r") as file_1:
    file_1_content = file_1.readlines()
    del file_1_content[4]
    with open(path_to_test_file_2, "w") as file_2:
        for line in file_1_content:
            file_2.write(line)
