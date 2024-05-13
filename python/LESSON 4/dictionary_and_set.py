# Dictionary
# Mapping between two items

# key - value mapping
users = {
    "username": "viktor",
    "password": "whatever",
}

# The way to get data out of a dictionary
print(users["password"])

def count_words(sentence):
    word_count = {}
    # word_count = { "a": 15 ``}
    # word_count["a"] = 20
    # print(word_count["a"])

    for word in sentence:
        word = word.strip(".,!?").lower()

        if word:
            # word_count["a"] = word_count.get("a", 0) + 1 
            word_count[word] = word_count.get(word, 0) + 1
        
    return word_count

result = count_words("qowijrqwoijtqwoiy jqowitj i oqiwjt oqiwj yohqnjtwpksdgmd;fl ngso mpkomko peyrkpwonjrhkeornh ktepognskpj")
print(result)

student = {
    "name": "Viktor",
    "grades": {
        "math": 5,
        "physics": 3
    }
}

students = [
    {"name": "John", "age": 22},
    {"name": "Emily", "age": 20},
    {"name": "Mike", "age": 21},
]

# set: immutable sequence
# set use case: when youre data is NOT going to change USE A TUPLE 

# set: doesn't allow duplication of 

names = {"Viktor", "Qni", "Viktor"}
print(names)

import random

random_numbers = [random.randint(0, 3) for _ in range(10 ** 9)]
print(random_numbers)
print(set(random_numbers))

# list comprehension example without a list comprehension
nums = []
for number in range(10 ** 6):
    nums.append(number)

# list comprehension syntax
nums = [number for number in range(10**6)]
print(nums)
