# Loops in Python
# While Loop
i = 0
while i<5:
  print(i)
  if i ==2:
    print("Breaking Loop")
    break
  i = i + 1
# For Loop
# Break Example
for i in range(10):
    if i == 4:
       print("Breaking Loop")
    break
print(i)
# Continue Example
for i in range(10):
 if i == 4:
  print(f"Skipping {i}")
 continue
print(i)