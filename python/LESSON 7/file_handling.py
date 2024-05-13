# mode -> начин на работа
# modes = {"write": "w", "read": "r", "append": "a"}

def work_with_file(file_name, mode):
    file = open(file_name, mode)
    if mode == "w" or mode == "a":
        stuff_to_write = input("What to write to the file: ")
        file.write(stuff_to_write + "\n")
    elif mode == "r":
        file_content = file.read()
        print(file_content)
    file.close()

work_with_file("my_file.txt", "r")

# IO operationrs IO -> Input / Output
