import time
from clearScreen import clear_screen

def red_blue_yellow():
    door = input("Which door would you rather go through?\n'Red', 'Blue' or 'Yellow': ").lower()

    if door == 'red':
        print("You've been burned by fire. Game Over.")
        return
            
    elif door == 'blue':
        print("You've been eaten by beasts. Game Over.")
        return
        
    elif door == 'yellow':
        print("You found the treasure. Congratulations, You Win!")
        return

    else:
        print("Invalid input. Please enter 'red', 'blue' or 'yellow'.")
        time.sleep(2)
        clear_screen()
        red_blue_yellow()
