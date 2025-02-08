from clear_screen import clearscreen


def get_number(prompt):
    '''Gets a number input from user'''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            clearscreen()
            print("Input Error. Please enter a valid number.")
