# complex types of data
# list, tuple, dictionary, set

# list creation syntax: [<item1>, <item2>, <item2>]
fruits = ["banana", "apple", "pinapplae", "orange"]
banana = fruits[0]
print(banana)
fruits[4]

# list indexsing. Example below is throwing an error out of bounds
# first_item = fruits[100]

# in a list any type of data can be stored

# list function to add an item
fruits.append(55)
fruits.append("coconut")
print(fruits)

# tuple
# syntax (<item1>, <item2>, etc...)

# What's special about tuples?
# TUple CAN NEVER CHANGE
# This immutability gives advantages over plain lists

fruits = ("banana", "apple", "pineapple", "orange", 45)

