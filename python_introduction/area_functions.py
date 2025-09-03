def area(length, width):
  area = length*width
  return area
print(area(5,3))

def user_name(name):
  greeting=f"Hello {name}!"
  print(greeting)

def even_odd_num(number):
  remainder = number % 2 
  if remainder == 0:
    result = "even"
  else:
    result = "odd"
  print(f"{number} is {result}")
even_odd_num(11)
even_odd_num(106)
