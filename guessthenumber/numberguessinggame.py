# Number guessing game.
# Use while loop, if-else, ...


import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)

while 1<2:
    choice = input()
    if choice == "easy":
        attempts = 10
        break
    elif choice == "hard":
        attempts = 5
        break
    else:
        print("please type again")

while 1<2:
  print(f"You have {attempts} attempts remaining to guess the number.")
  print("Make a guess:")
  choice2 = input()
  choice2 = int(choice2)
  if choice2 == number:
    print("Congrats! You won!")
    break
  else:
    attempts -= 1
    if attempts == 0:
      print("Sorry. You losed!")
      break
    else:
      if choice2 < number:
        print("Too low. Pls try again!")
      else:
        print("Too high. Pls try again!")

exit()
