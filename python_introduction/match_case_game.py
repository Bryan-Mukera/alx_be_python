
import random

while True:
  secret_number = random.randint(1,10)
  guess = int(input("Guess a number between 1 and 10: "))


  match (guess > secret_number, guess < secret_number):
    case (False, False):   # guess == secret_number
      print("Congratulations, you guessed it!")
    case (True, False):
      print("Oops, your guess is a bit high. Try again!")
    case (False, True):
      print("Nope, your guess is abit low. Give it another shot!")
  continuation = input("Do you want to play again (Yes or No):")
  if continuation == "Yes":
    print("You can play again.")
  else:
    print("ThankYou for playing.")
    break
