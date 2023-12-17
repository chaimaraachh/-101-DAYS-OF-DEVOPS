
"""Write a simple script to check if the file and directory exist using the OS module."""

import os

def check_file_or_directory():
    to_check = input("Enter the file/directory name to check: ")

    if os.path.exists(to_check):
        print(f"The file or directory '{to_check}' exists.")
    else:
        print(f"The file or directory '{to_check}' does not exist.")

check_file_or_directory()
