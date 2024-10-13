"""Activity 6: Basic Calculator
Problem Statement:
Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.

Questions:
- How to create Choices for the user?
- How the user input two numbers?
- How can you add your define functions inside your If-else statements?
- How do stop the calculations at a certain part?
- How do you cope with this when a user will type a invalid input?"""

def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def divide(x,y):
  return x/y

print("SELECT OPERATION")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
  choice = input("ENTER CHOICE:")

  if choice in ("1","2","3","4"):
    try:
      num1 = float(input("ENTER FIRST NUMBER:"))
      num2 = float(input("ENTER SECOND NUMBER:"))

    except ValueError:
      print("Invalid Input. \n Please enter a number btw 1-4:")
      continue

    if choice == "1":
      print(num1, "+",num2, "=", add(num1,num2))

    elif choice== "2":
      print(num1, "-",num2, "=", subtract(num1,num2))

    elif choice== "3":
      print(num1, "*",num2, "=", multiply(num1,num2))

    elif choice== "4":
      print(num1, "/",num2, "=", divide(num1,num2))

    New_calculation = input("Do you want to do any other calculation (yes/no)")
    if New_calculation =="no":
      break
    else:
      print("Invalid Input")


