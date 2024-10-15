# Problem statement is we have a security job where only men can apply whose age
#is greater then 18

age = input("Please Enter your Age: ")
age= int(age)
gender = input("Enter your gender male or female: ")

if gender == 'male':
  if age > 18:
    print("Eligible")
  else:
    print("Not Eligible")
else:
  print("Not Eligible")

# Nested Loops
for i in range(5):
  for i in range(2):
    print('ali')
print('Done')

# Nested List
car = ['bmw', 'honda', ['audi', 'ford'], 'ferrari']
for i in car:
  print(i)

  """# Problem statement is we have a security job where only men can apply whose age
is greater then 18
# Python Logical Operators
# 1. And -> Executed when both values are True
# 2. OR -> It executes either one of the value is True
# 3. Not -> When value is not True"""

age = input("Please Entery your Age: ")
age= int(age)
gender = input("Enter your gender male or female: ")

if gender=='male' and age > 18:
  print("Eligible")
elif gender=='male' or age > 18:
  print("Partially Eligible")
else:
  print("Not Eligible")

  # Not
if not gender=='male':
  print('female')