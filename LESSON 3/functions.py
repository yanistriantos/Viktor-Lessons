import math

# function: input -> does_something -> output 
# syntaxys: def <function_name>(<args>, <args2>, ...):
#   code block
#   return <data>

# without return None is returned
# wihtout a return statement an implicit return None is done
def add_two_numbers(a, b):
    a + b

# using a reutrn statement
def add_numbers(a, b):
    return a + b

# print(add_numbers(15, 15))

# createa a function that does the following
# takes a name as arguments e.g. "Viktor"
# returns "Hello, Viktor!"
def greed(name):
    return name

print(greed(5))

# function magic_function.Takes 2 arguments. Returns the square root of those items
# funciton sub: the same but with subtraction
# function mult: the same but with multiplicaiton
# function rem: returns the remainder
def rem(number1, number2 ):
    return number1 % number2

def mult(num1, num2 ):
    return num1 * num2

def sub(num1, num2):
    return num1 - num2

def magic_function(num1):
    return math.sqrt(num1)

    
print(rem(4, 864), mult(18437.12, 18.2), sub(34665, 7456), magic_function(6547))

# when a given function is called the current execution flow of the program stops and junmps to that function
