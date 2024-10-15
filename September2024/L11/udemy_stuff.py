# f string // formatted string
# "str" + " str2" = "str str2"
# name = input("Enter your name: ")
# greeting = "Greetings, " + name # formatting of a string using the "+" operator
# greeting = f"Greetings, {name}. {5 + 8 / 4}" # formatted string | f string
# print(greeting)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0] # -> [1, 2, 3]
matrix[0][1] # -> 2

# List slicing -> returns part of a list

print(matrix[1:]) # a slice returns a list
print(matrix[:2])
# [2:8] -> 3rd item to 8th item

items = ["armor", "weapon", "potion"]
# [item1, item2, item3] = items

shapes = ("circle", "square", "rectangle")
(item1, _, _) = shapes

connection = {"host": "127.0.0.1", "port": "8080"}
host, port = connection.items()

print(host, port, sep=" | ")
