# Exercise Suite: Python Standard Libraries & File Manipulation
# # Exercise 1: Working with the `os` and `shutil` Libraries

import os
import shutil

path = "/Users/nebula/Desktop/DEVPACK/Viktor-Lessons-master/October2024/Lesson2"
dir_list = os.listdir(path)

print(f"The files and directories at path {path} are {dir_list}")

new_dir_path = os.path.join(path, "test_dir")
os.mkdir(new_dir_path)

for file_name in dir_list:
    # Check if the file has a .txt extension
    if file_name.endswith(".py"):
        file_path = os.path.join(path, file_name)
        shutil.copy(file_path, new_dir_path)
       
        
print(f"All .py files have been moved to {new_dir_path}")
