import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
mylist = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. "))
print(f"You chose: {mylist[user_choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose: {mylist[computer_choice]}")
if user_choice == computer_choice:
  print("its a draw!")
elif user_choice==0 :
  if computer_choice == 1:
    print("You lose!")
  else:
    print("You win!")
elif user_choice == 1:
  if computer_choice == 0:
    print("You win")
  else:
    print("you lose!")
elif user_choice == 2:
  if computer_choice == 0:
    print("You lose")
  else:
    print("You win")
    


