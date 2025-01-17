# Heads or Tails
'''
Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.
'''

import random

coin = random.randint(1, 2)

if coin == 1:
    print("Heads")
else:
    print("Tails")


