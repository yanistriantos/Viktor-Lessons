def divide_numbers():
    while True:
        a = int(input("Enter number one: "))
        b = int(input("Enter number two: "))
        try:
            print(f"The result of dividing {a} by {b} is: {a / b}")
            return
        except ZeroDivisionError:
            print("Divison by zero is inccorect. Please, try again")


# The result of diving 5 by 2 is 2.5
    
# divide_numbers()

def read_file(filename):
    try:
        file = open(filename, "r")
        file_content = file.read()
        print(file_content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist")

# read_file("test.txt")


# Лоша практика, "catch all errors"
try:
    pass
except Exception:
    pass


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

def input_number():
    while True:
        try:
            num = float(input("Enter your number: "))
            print(num)
            return
        except ValueError:
            print("Error: Invalid input. Please entehttps://discordapp.com/channels/1118862363207151616/1119928651497082920r a valid number.")

input_number()
