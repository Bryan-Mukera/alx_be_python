fav_fruits = ["grapes", "tangerines", "banana", "avocado", "mango"]
print(fav_fruits[1])

fav_book = {"title" : "Bible", "author" : "God", "genre" : "religious"}
print(fav_book.get("genre"))
print(fav_book.keys())

import random
def generate_random_set():
  number_list = [random.randint(1,10) for _ in range(10)]
  unique_numbers = set(number_list)
  print("Original list (may have duplicates):", number_list)
  print("Unique numbers:", unique_numbers)
  return unique_numbers
generate_random_set()