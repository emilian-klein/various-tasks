#Write all content of a given file into a new file by skipping line number 5

path_to_file = r"test2_6.txt"
file = open(path_to_file, "r")
lines = file.readlines()
file.close()

del lines[4]

path_to_new_file = r"new_test2_6.txt"
new_file = open(path_to_new_file, "w")
for line in lines:
    new_file.write(line)
new_file.close()