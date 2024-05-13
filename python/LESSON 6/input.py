name = input("Enter your name: ") #prompt
print("Your name is: "  + name)

def full_name(first_name, second_name):
    full_name = first_name + " " + second_name 
    return full_name

name1 = full_name("VIktor", "Stefanov")
name2 = full_name("Vladislav", "Tonev")
print(name1 , name2)

