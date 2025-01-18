import time
from clearScreen import clear_screen
from redBlueYellow import red_blue_yellow


def swim_or_wait():
    choice = input("Would you rather 'swim' across or 'wait' for a boat? ").lower() 

    if choice == 'swim':
        print("You've been attacked by a trout. Game Over.")
        return

    elif choice == 'wait':
        print("You are now before three doors!")
        time.sleep(2)
        clear_screen()
        red_blue_yellow()

    else: 
        print("Invalid input. Please enter 'swim' or 'wait'.")
        time.sleep(2)
        clear_screen()
        swim_or_wait()
