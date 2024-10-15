import random
import math_utilities

inventory = ["apple", "banana"]
get = inventory[0][1]
print(get)

my_dictionary = {"health": 50, "name": "Yani", "health": 70}
player = {
    "health": 50,
    "attack": 15,
    "armor": 20
}
have = my_dictionary["health"]
value = player.get("armor")
print(have, value)

# db_credentials = {
#     "user": "...",
#     "port": "...",
#     "password": "...",
#     "database": "..."
# }

# mysql.connect(db_credentials)

new_tuple = (1, 5, 7)
new_list = [1, 5, 7, 5]

my_list = list()
my_set = set()
for _ in range(100_000):
    random_number = random.randint(1, 10)
    my_list.append(random_number)
    my_set.add(random_number) 

# print(my_list, len(my_list))
# print(my_set, len(my_set))

items = [1, 2, 3, 4, 5, 6, 7]
if len(items) > 10:
    print(items[10])
    # ...
    # ...
    # ...
elif len(items) > 5: # else if {...} else
    print(items[5])
else:
    print("equals or less than five items")

print(math_utilities.divide(5, 10))
