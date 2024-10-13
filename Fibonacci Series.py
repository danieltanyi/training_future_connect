"""Activity 4: Fibonacci Series
Problem Statement:
Write a code in python which will give you a Fibonacci series to a number when you enter it.

Questions:
- How you will you deal when a user inputs ‘0’?
- How the user will deal when a user inputs ‘1’?
- Which loops and statements do you use for the iterations?"""

while True:
  n = int(input("Enter the lenghth of the Fibonancci series:"))
  a, b = 0, 1
  count=0
  while True:
    if n<=0:
      print("Enter a positive integer:")
    elif n==1:
      print("Fibonacci Series upto ", n, ":",a)
    else:
      print("Fibonacci Sequence:")
    while count < n:
        print(a)
        nth =a+b
        a = b
        b = nth
        count += 1
    break