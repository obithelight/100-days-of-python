import os
import time
from swimWait import swim_or_wait

def left_or_right():
    direction = input("Would you like to go 'left' or 'right'? ").lower() 
    # os.system('clear')

    if direction == 'right':
        print("You fell into a hole. Game Over.")
        return

    elif direction == 'left':
        print("You've arrived at the lake.")
        time.sleep(2)
        os.system('clear')
        swim_or_wait()
    
    else:
        print("Invalid input. Please enter 'left' or 'right'.")
        time.sleep(2)
        os.system('clear')
        left_or_right()
