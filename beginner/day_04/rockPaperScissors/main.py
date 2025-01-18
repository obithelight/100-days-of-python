import random

'''
You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

rock =
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

paper =
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


scissors =
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


Demo
https://appbrewery.github.io/python-day4-demo/
'''

game = ['rock', 'paper', 'scissors']
computer_choice = random.choice(game)

print("Welcome to the Rock-Paper-Scissors Game Show.")

while True:
    user_input = input("Make a choice. Enter 0 for 'rock', 1 for 'paper', or 2 for 'scissors': ")
    if user_input == '0' or user_input == '1' or user_input == '2':
        break

user_input = int(user_input)
user_choice = game[user_input]

print("Computer choice is:", computer_choice)
print("User choice is:", user_choice)

# computer wins
if computer_choice == 'rock' and user_choice == 'scissors':
    print("Computer Wins. You lose.")

elif computer_choice == 'paper' and user_choice == 'rock':
    print("Computer Wins. You lose.")

elif computer_choice == 'scissors' and user_choice == 'paper':
    print("Computer Wins. You lose.")

# user wins
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("Congratulations. You Win.")

elif user_choice == 'paper' and computer_choice == 'rock':
    print("Congratulations. You Win.")

elif user_choice == 'scissors' and computer_choice == 'paper': 
    print("Congratulations. You Win.")

# draw game
else:
    print("It's a draw!")
