# You are given a string .
# # Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# str.isallnum() 1.
# str.isalpha()  2.
# str.isdigit()  3.
# str.islower()  4.
# str.isupper()  5.
if __name__ == '__main__':
   s = input("Enter a string: ")

if any(c.isdigit() for c in s):
    print(True)
else:
    print(False)

if any(c.islower() for c in s):
    print(True)
else:
    print(False)

if any(c.isupper() for c in s):
    print(True)
else:
    print(False)

if any(c.isalpha() for c in s):
    print(True)
else:
    print(False)

if any(c.isalnum() for c in s):
    print(True)
else:
    print(False)

