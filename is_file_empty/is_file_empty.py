"""
   Program checks if given file is empty.
"""

import os

files_to_check = ["empty_file.txt", "not_empty_file.txt"]
for file in files_to_check:
    if os.stat(file).st_size == 0:
        print("File is empty!")
    else:
        print("File is not empty!")
