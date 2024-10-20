# Exercise 1: Creating and Accessing Dictionary Elements

# student = {
#     "name": "John",
#     "age": 20, 
#     "major": "Computer Science",
#     "gpa": 3.8,
# }   
# print(student["name"])
# print(student["major"])

# student.update({"age": 21})
# student["age"] = 21

# del student['gpa']
# value = student.pop('age')

# print(f"The popped value of age is: {value}")

# if "major" in student:
#         print("The key 'major' exists in the dictionary")

# if "age" in student:
#         print("The key 'age' exists in the dictionary")

# print(student)


# course_grade = {
    
# "Math": 90,
# "English": 85,
# "History": 88,
# }

# for (lesson, grade) in course_grade.items():
#     print(lesson, grade)
   
#    #Dictonary Comrehenesion 
# numbers = [1, 2 ,3, 4, 5]
# my_dict = {x: pow(x, 2) for x in numbers}

# print(my_dict)

#Nested Dictionary

university = {
     "CS": {"students": 20, "professors": 15 },
     "Math": {"students" : 10, "professors": 10 }    
}

# # print(university["CS"]["students"])

# university.update({"Math": {"students": 10, "professors": 8}})
# university["Math"]["professors"] = 8
# print(university)
                  
# from collections import defaultdict

# my_dict = defaultdict(list)

# my_dict = {
# "group1": ["Alice", "Bob"],
# "group2": ["Charlie", "David"]
# }
# my_dict["group1"].append("Eve")

# print(my_dict)
