"""
Task:
    Write script to check if given file is empty.
"""
import os


if __name__ == "__main__":
    if os.stat(r"test_files/test_file_1.txt").st_size == 0:
        print("File is empty!")
    else:
        print("File is not empty!")
