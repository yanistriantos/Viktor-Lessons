# to get values inside your python code from the outside we use the input function
# syntax: input(<prompt>)

# age = input("Please enter your age: ")
# print_age = "You entered this age: 5"  + age
# print(print_age)

# if statement: checks if a given condition evaluates to True / False and depending on the result either EXECUTES or DOESN"T execute the code block
# else statement:

# age = 15
# if age > 18:
#    print("Can drive a car")


years = int(input("What age are you: "))
if years >= 18:
    print("You can vote")
else:
    print("You cant") 

age = 55
if age < 7:
    print("child")
elif age <= 19:
    print("teen")
elif age <= 50:
    print("middle age")
else:
    print("old")

