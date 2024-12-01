# Exercise 5: File Search and Manipulation with `os` and `shutil` Libraries
import os 
import shutil

current_directory = "/Users/nebula/Desktop/DEVPACK/Viktor-Lessons-master/October2024"
dir_list = os.listdir(current_directory)

backup_folder = os.path.join(current_directory, 'backup')
    
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)


for file_name in dir_list:
    if file_name.endswith(".log"):
        shutil.move(file_name, os.path.join(backup_folder, file_name))
        
print(f"The .log files have been moved to: {backup_folder}")

# important file manipulation skills using Python’s standard libraries,
# which are essential for tasks like navigating file systems, 
# processing CSV and JSON data, handling timestamps, and moving files.