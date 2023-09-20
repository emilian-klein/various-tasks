#Read line number 4 from the test2_6.txt file

path_to_file = r"test2_6.txt"
file = open(path_to_file, "r")
lines = file.readlines()
file.close()

print(lines[3])