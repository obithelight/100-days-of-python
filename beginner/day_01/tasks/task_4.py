'''
Variables 
'''
#Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.

# 1. Check the length of the user input
'''
Using what you have learnt about the len() function and the input() function. Try to print out the number of characters in the user input. Write everything in just 1 line of code.
'''
print(len(input("What is your name? ")))

# 2. Split everything into variables.
'''
Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation.
'''
username = input("What is your name? ")
length = len(username)
print(length)