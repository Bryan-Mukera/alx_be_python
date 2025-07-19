
import random

while True:
  secret_number = random.randint(1,10)
  guess_count = 0
  
  while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guess_count += 1

    match (guess > secret_number, guess < secret_number):
      case (False, False):   # guess == secret_number
        print(f"Congratulations, you guessed it {guess_count} attempt(s)!")
        break
      case (True, False):
        print("Oops, your guess is a bit high. Try again!")
      case (False, True):
        print("Nope, your guess is abit low. Give it another shot!")
  continuation = input("Play again? (yes/no):")
  if continuation == "yes":
    print("You can play again.")
  else:
    print("ThankYou for playing.")
    break

