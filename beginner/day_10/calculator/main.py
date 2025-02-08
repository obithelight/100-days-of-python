#!/usr/bin/python3
"""A Python3 Module"""
import sys
import time
from calc_operations import operations, choice
from input_handler import get_number
from clear_screen import clearscreen


def calculator():
    """Main calculator function handling operations and continuation."""
    first_number = get_number("Enter your first number: ")

    while True:
        print("\nChoose one arithmetic sign from the list below:")
        print(choice)

        operator = input("Pick an operation to perform: ").strip()

        while operator not in choice or operator == "":
            clearscreen()
            print(f"Invalid input. Choose an operation from: {choice}")
            operator = input("Pick an operation to perform: ").strip()
        second_number = get_number("\nEnter your second number: ")
        result = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        should_continue = input("\nType 'y' to continue your calculation "
                                f"with {result}.\nType 'n' to start a new "
                                "calculation.\nType any other key "
                                "to quit the program.\n\n").lower()
        clearscreen()

        if should_continue == 'y':
            first_number = result
            print(f"Your first number is: {first_number}")
        elif should_continue == 'n':
            calculator()
        else:
            print("Shutting down calculator..")
            time.sleep(3)
            clearscreen()
            print("See you next time..")
            time.sleep(3)
            clearscreen()
            sys.exit()


if __name__ == "__main__":
    calculator()
