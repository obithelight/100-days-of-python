import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

myletters = ''
mynumbers = ''
mysymbols = ''

for _ in range(nr_letters):
    myletters += random.choice(letters)
# print(myletters)

for _ in range(nr_numbers):
    mynumbers += random.choice(numbers)
# print(mynumbers)

for _ in range(nr_symbols):
    mysymbols += random.choice(symbols)
# print(mysymbols)

# Easy Level: print the password sequentially
password = myletters + mynumbers + mysymbols
print("Easy Level:", password)

# Hard Level: randomly rearrange the password 
password = list(password)
random.shuffle(password)

password = "".join(password)
print("Hard Level:", password)
