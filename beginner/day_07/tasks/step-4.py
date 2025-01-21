import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for _ in chosen_word:
    placeholder += '_'
print(placeholder)
'''
1: Create a variable called lives to keep track of the number of lives left.
Set lives to equal 6.
'''
lives = 6

'''
2: If guess is not a letter in the chosen_word, Then reduce lives by 1.
If lives goes down to 0 then the game should end, and it should print "You lose."
'''
gameover = False
container = []

while not gameover: 
    guess = input('Guess a letter: ').lower()

    if guess in container:
        print(f"You have already guessed letter '{guess}'")

    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            container.append(guess)
        elif letter in container:
            display += letter
        else:
            display += '_'

    print(f"Word to guess: {display}")

    if '_' not in display:
        gameover = True
        print("You win!")
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 1:
            print(f"You have only {lives}/6 life left.")
        else:
            print(f"You have {lives}/6 lives left.")
        if lives == 0:
            gameover = True
            print(f"The word was {chosen_word}. Game Over. You lose")
    print(stages[lives])
'''
3: Print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.
'''
