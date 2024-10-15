points = ["5", 1, 2, 3, 4, "5", 6, 7, 8, 9, 10]
points.remove("5")
# points.pop()
print(points)

five_points = points[0:5]

print(five_points)

# what does a list look at the memory level?
# list == address + size
# points.size = 10
# points.address = 1050

fifth_element = points[4]

# 1050 + 4 -> 1054
# fifth_elemnt would be calculated by getting the starting position of the list (1050) and adding the index amount 

print(len(points))

item_prices = {"coffee": 10, "game": 15}
if "game" in item_prices:
    print("ok")

names = ["viktor", "qni"]
names.sort()
print(names)

# a = 0
# q = 31
# q > v => True

numbers = [1, 2, 3, 4, 1, 1, 1, 1, 1]
# below code is just for demonstration purposes. To make it work use indexes

# for num1 in numbers:
#     for num2 in numbers:
#         if num1 == num2:
#             numbers.remove(num2)

print(list(set(numbers)))

print(round(5.4999))
input()
