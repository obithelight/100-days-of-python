import os

def clear_screen():
    # Clear screen based on the OS
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')


if __name__ == "__main__":
    clear_screen()
