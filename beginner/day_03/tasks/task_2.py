# Modulo
'''
The modulo operator gives you the remainder of a division.

6 % 2 #will be 0
6 % 5 #will be 1
6 % 4 #will be 2
'''
# 1 - What is 10 % 3?
# What do you think this will output?

print(10 % 3) #will be 1

# 2 - Check Odd or Even
'''
Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".'''
number = int(input("Please enter an integer: "))
if number % 2:
    print("Odd")
else:
    print("Even")
