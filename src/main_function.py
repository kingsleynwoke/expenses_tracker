import sys
import os
sys.path.insert(0, os.path.abspath(os.curdir))

from src.generate_expenses import update_existing_data
from src.read_file import read_from_txt
from src.sum_expenses_data import print_summary_of_expenses
from src.plotting import plots

def welcome_message():
    print("\n#########################################################")
    print("   !!!        Welcome to expenses tracker         !!! ")
    print("   !!! Kindly follow instructions on your screen  !!!")
    print("#########################################################")

def display_options():
    """
    Create a menu like option to aid user input.
    """
    print("\nEnter a to add new record.")
    print("Enter b to check record.")
    print("Enter c to check sum of expenses for each category.")
    print("Enter d to visualize balance and expenses.\n")
    user_input = input('Please enter your choice: ')
    print()
    return user_input

def summary():
    """
    Based on user input execute the following.
    """
    user_choice = display_options()
    while user_choice not in ["a", "b", "c", "d"]:
        print("Your choice is incorrect, please choose from a, b, c, d")
        user_choice = input('Please enter your choice: ')
        print()
    if user_choice == "a":
        update_existing_data()
      
    elif user_choice == "b":
        print("########################################################")
        print("     !!!   These are the records so far   !!!!     ")
        print("########################################################\n")
        read_from_txt()
        print()
    elif user_choice == "c":
        print("Enter your income in numbers e.g 37561, 45000 etc.")
        print_summary_of_expenses()
    elif user_choice == "d":
        print("Enter your income in numbers e.g 37561, 45000 etc.")
        plots()

def final_function():
    """
    This is the calling code, also know known as the main function.
    It calls all the codes above it.
    """
    welcome_message()
    while True:
        summary()
        print("Enter e to continue")
        print("Enter q to quit\n")
        new_input = input("Please enter your choice: ")

        while new_input not in ["e", "q"]:
            print("Your choice is incorrect, please choose e or q")
            new_input = input('Please enter your choice: ')
            print()
        if new_input == "e":
            pass
        elif new_input == "q": 
            print("\nYou have exited the program.")
            return
        continue

if __name__ == "__main__":
    final_function()