from math import *

num1 = float(input("Enter a number: "))
action = raw_input("Enter operator: ")
num2 = float(input("Enter another number: "))
print("")

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
elif action == "/":
    print(num1 / num2)
elif action == "^":
    print(pow(num1, num2))
else:
    print("Please enter a valid number!")