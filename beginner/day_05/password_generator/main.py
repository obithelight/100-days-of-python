from clearScreen import clear_screen
import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
time.sleep(1)

while True:
    nr_letters = input("How many letters should be present in your password? ")
    if not nr_letters.isdigit():
        clear_screen()
        print("Wrong input. Please enter a number.")
    else:
        break
    
while True:
    nr_numbers = input("How many numbers should be present in your password? ")
    if not nr_numbers.isdigit():
        clear_screen()
        print("Wrong input. Please enter a number.")
    else:
        break

while True:
    nr_symbols = input("How many symbols should be present in your password? ")
    if not nr_symbols.isdigit():
        clear_screen()
        print("Wrong Input. Please enter a number.")
    else:
        break

nr_letters = int(nr_letters)
nr_numbers = int(nr_numbers)
nr_symbols = int(nr_symbols)

mypassword = ''

for _ in range(nr_letters):
    mypassword += random.choice(letters)
# print(mypassword)

for _ in range(nr_numbers):
    mypassword += random.choice(numbers)
# print(mypassword)

for _ in range(nr_symbols):
    mypassword += random.choice(symbols)
# print(mypassword)

# Easy Level: Print the password sequentially
clear_screen()
print("Easy Level Password:", mypassword)

# Hard Level: randomly rearrange the password 
# step 1: convert string to list and shuffle the list
mypassword = list(mypassword)
random.shuffle(mypassword)

# step 2: convert the list back to string and concatenate
mypassword = "".join(mypassword)
print("Hard Level Password:", mypassword)
