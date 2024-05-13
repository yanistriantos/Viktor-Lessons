# variable (променлива) 
# variable - placeholder for a value

# a variable has a name and a value that it holds

# everything in double or single quotes "", '' is TEXT
# STRING = text
name = "Viktor"

# the variable age holds an INTEGER value
age = 2

# the variable kg holds a FLOAT type of value (C++ it's called DOUBLE)
kg = 2.3

# BOOLEAN data type
slow = False
fast = True

# those are the basic data types - STRING, INTEGER, FLOAT, BOOLEAN

# print("vsqkakuv text")
# print(15)

# print(name, age, kg, slow, fast)

# arithmetic operators
age1 = 20
age2 = 15
both_age = age1 + age2 # addition
height = age1 - age2 # subtraction
res1 = age1 * age2 # multiplicaiton 
res2 = age1 / age2 # division
res3 = age1 // age2 # floor division
reminder = age1 % age2 # modulo operator (остатъка от делението)
exponentiation = 3 ** 3 # exponentiation
#print(both_age, height)
#print(exponentiation)

# when combining strings together it is called CONCATENATION
first_name = "Ioannis"
last_name = "Triantos"
full_name = first_name + " " + last_name
print(full_name)

age = 15
name = "Viktor"
# print(name + age)

# Comparison operators. All comparison operators return a BOOLEAN value. True / False
num1 = 15
num2 = 17

bigger = num1 > num2
smalller = num1 < num2
be = num1 >= num2
se = num1 <= num2
equal = num1 == num2 # equiality check
notequal = num1 != num2 # inequaltiy check
check = 23.6 > 20
print(bigger, smalller, be, se, equal, notequal)                     

print(type(first_name))
print(type(age))
print(type(kg))
print(type(equal))

# to change the type of a variable is called TYPE CASTING
name = "Viktor"
num = 7
print(name + " = " + str(num))

age = "150"
print(int(age) + 5)

fast = 0
print(fast, bool(fast))

# Type castings: str(), int(), float(), bool()
