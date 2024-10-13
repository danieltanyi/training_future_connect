"""
Problem Statement:
Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).

Questions:
- Which operator you will use in order to execute this code?
"""

for i in range(1,101):
  if i % 15==0:
    print("FizzBuzz")
  elif i % 3==0:
      print("Fizz")
  elif i % 5==0:
        print("Buzz")
  else:
          print(i)

