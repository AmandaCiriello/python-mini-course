# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here
  choice = input("Enter Rock Scissors or Paper ")
  print("Your choice is " + choice)

  # if statement that checks if user's choise is correct
  if choice == "Rock" or choice == "Scissors" or choice == "Paper":
    print("Your response is valid")
  else:
    print("You're response is not valid")
  
# computer choice
  computer_choice = whatIsIt(computerChoice())
  print("computer choice: ")
  print(computer_choice)

# print tie if user and computer chouce is the same

  if choice == computer_choice:
    print("It's a tie!")
  else:
    print("It's not a tie")
    if choice == "Rock":
      if computer_choice == "Scissors":
        print("The user won!")
      if computer_choice == "Paper":
        print("The computer won!")
      elif choice == "Scissors":
        if computer_choice == "Paper":
          print("The user won!")
        if computer_choice == "Rock":
          print("The computer won!")
      elif choice == "Rock"


  

  #print random computer response
  # print(whatIsIt(computerChoice()))

rockScissorsPaper()


