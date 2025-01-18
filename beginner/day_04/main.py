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
print("Computer choice is:", computer_choice)

human_choice = random.choice(game)
print("Human choice is:", human_choice)

# computer wins
if computer_choice == 'rock' and human_choice == 'scissors':
    print("Computer Wins. You lose.")

elif computer_choice == 'paper' and human_choice == 'rock':
    print("Computer Wins. You lose.")

elif computer_choice == 'scissors' and human_choice == 'paper':
    print("Computer Wins. You lose.")

# human wins
elif human_choice == 'rock' and computer_choice == 'scissors':
    print("Congratulations. You Win.")

elif human_choice == 'paper' and computer_choice == 'rock':
    print("Congratulations. You Win.")

elif human_choice == 'scissors' and computer_choice == 'paper': 
    print("Congratulations. You Win.")

# draw game
else:
    print("It's a draw!")
