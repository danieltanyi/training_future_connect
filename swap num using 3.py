"""Activity 3: Swap Numbers
Problem Statement:
Swap the numbers with and without the 3rd Variable.

Questions:
- How you will create and store the value in 3rd variable?
- How you will do it without the 3rd Variable?"""

x = int(input("Enter number 1:"))
y = int(input("Enter number 2:"))

temp = x=y
y=temp

print("After swapping \nNumber 1:", x)
print("Number 2:" , y)
