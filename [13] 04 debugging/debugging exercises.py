def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
# ==> Change 20 to 21.

--------------------------------------------

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
# ==> change (1,6) to (0, 5).

--------------------------------------------

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
# ==> change to: 
while 1<2:
  year = int(input("What's your year of birth?"))
  if year > 1980 and year < 1994:
    print("You are a millenial.")
    break
  elif year > 1994:
    print("You are a Gen Z.")
    break
  else:
    print("Please re-entry: ")

--------------------------------------------

age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
# ==> change to: 
while 1<2:
  age = int(input("How old are you?"))
  if age > 18:
    print(f"You can drive at age {age}.")
    break
  else:
    print("please re-input another older age. Otherwise, you're not qualified to drive.")

--------------------------------------------

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
# ==> change "==" to "=".

--------------------------------------------

def mutate(a_list):
  b_list = []
  for i in a_list:
    new_item = i * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
# ==> add indentation to the line "b_list.append(new_item)".

--------------------------------------------

number = int(input()) # Which number do you want to check?

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  # ==> add "=" to "==".

--------------------------------------------

# # Which year do you want to check?
# year = input()

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  
# ==> solution (debugged):
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
--------------------------------------------

# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# ==> Solution: 
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

