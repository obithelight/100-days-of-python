import os


def clearscreen():
    '''Clears the screen of a program'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
