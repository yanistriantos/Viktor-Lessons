import math

operation = input("Choose Calculation: \n"
                  " Add \n"
                  " Subtract \n"
                  " Multiply \n"
                  " Divide \n"
                  " Exponentiation \n"
                  " Square root\n")

num1 = float(input("Enter number: "))

if operation == "Add":
    num2 = float(input("Enter number two: "))
    ans = num1 + num2
elif operation == "Subtract":
    num2 = float(input("Enter number two: "))
    print(f"The result of subtracting {num2} from {num1} is:")
    ans = num1 - num2
elif operation == "Multiply":
    num2 = float(input("Enter number two: "))
    print(f"The result of multiplying {num1} by {num2} is: ")
    ans = num1 * num2
elif operation == "Divide":
    num2 = float(input("Enter number two: "))
    if num2 == 0:
        print("Can't divide by 0")
    else:
        print(f"The result of dividing {num1} by {num2} is: ")
        ans = num1 / num2
elif operation == "Exponentiation":
    num2 = float(input("Enter number two: "))
    print(f"The result of exponentiating {num1} by {num2} is: ")
    ans = num1 ** num2
elif operation == "Square root":
    if num1 < 0:
        print("Cannot calculate square root of a negative number")
    else:
        ans = math.sqrt(num1)
        print(f"The result of taking the square root of {num1} is: {ans}")
else:
    print("Invalid operation")

if operation in ["Add", "Subtract", "Multiply", "Divide", "Exponentiation"]:
    print("Answer:", ans)
   