# Python Dictionaries - Exercises

In this set of exercises, you will learn how to work with dictionaries in Python. A dictionary is a data structure that stores key-value pairs. These exercises will take you from the basics of creating dictionaries to more advanced concepts like nested dictionaries and merging dictionaries.

---

## Exercise 1: Creating and Accessing Dictionary Elements

1. Create a dictionary called `student` with the following key-value pairs:
   - `"name"`: `"John"`
   - `"age"`: `20`
   - `"major"`: `"Computer Science"`
2. Access and print the value associated with the key `"name"`.
3. Access and print the value associated with the key `"major"`.

---

## Exercise 2: Adding and Updating Dictionary Elements

1. Add a new key-value pair to the `student` dictionary: `"gpa"`: `3.8`.
2. Update the value for the `"age"` key to `21`.
3. Print the updated dictionary.

---

## Exercise 3: Removing Dictionary Elements

1. Use `del` to remove the `"gpa"` key from the `student` dictionary.
2. Use `pop()` to remove the `"age"` key and capture its value.
3. Print the dictionary after both removals and print the value of the `"age"` key that was removed.

---

## Exercise 4: Checking for Keys

1. Check if the key `"major"` exists in the `student` dictionary.
2. Check if the key `"age"` exists.
3. Print appropriate messages for each check.

---

## Exercise 5: Iterating Through a Dictionary

1. Create a dictionary called `course_grades` with the following key-value pairs:
   - `"Math"`: `90`
   - `"English"`: `85`
   - `"History"`: `88`
2. Write a loop that prints each course and its corresponding grade.

---

## Exercise 6: Dictionary Comprehension

1. Create a list called `numbers`: `[1, 2, 3, 4, 5]`.
2. Use a dictionary comprehension to create a dictionary where the keys are the numbers from the list, and the values are the squares of those numbers.
3. Print the resulting dictionary.

---

## Exercise 7: Nested Dictionaries

1. Create a dictionary called `university` where the keys are department names (`"CS"`, `"Math"`) and the values are dictionaries with `"students"` and `"professors"` as keys.
2. Access and print the number of students in the `"CS"` department.
3. Update the number of professors in the `"Math"` department to `8`.

---

## Exercise 8: Merging Two Dictionaries

1. Create two dictionaries:
   - `person1 = {"name": "Alice", "age": 25}`
   - `person2 = {"city": "New York", "email": "alice@example.com"}`
2. Merge `person2` into `person1` using the `update()` method.
3. Print the merged dictionary.

---

## Exercise 9: Counting with Dictionaries

1. Given a list of colors: `["red", "blue", "green", "blue", "red", "blue"]`.
2. Write a function that counts how many times each color appears in the list using a dictionary.
3. Print the resulting dictionary.

---

## Exercise 10: Default Dictionaries (Advanced)

1. Import `defaultdict` from the `collections` module.
2. Create a `defaultdict` where the default value is a list.
3. Populate it with the following data:
   - `"group1"`: `["Alice", "Bob"]`
   - `"group2"`: `["Charlie", "David"]`
4. Add a new name, `"Eve"`, to `"group1"`.
5. Print the updated dictionary.

---

**Good luck with your exercises!** You should now feel more comfortable with dictionaries and how to use them to store and manipulate data.
