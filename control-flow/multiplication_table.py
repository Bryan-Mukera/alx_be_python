number = int(input("Enter a number to see its multiplication table:"))

iterator = range (1, 11)

for num in iterator:
  result = number * num
  print(f"{number} * {num} = {result}")