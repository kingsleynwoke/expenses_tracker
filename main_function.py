import random 
import pandas as pd
import numpy as np
from datetime import datetime as dt
from random import choice
from matplotlib import pyplot as plt
import json

from add_expense import add_expense_with_category
from read_and_write import txt_read_from_file
from sum_category import print_sum_category_expenses

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
    Based on user input above execute the if statements.
    """
    user_choice = display_options()
    while user_choice not in ["a", "b", "c", "d"]:
        print("Your choice is incorrect, please choose from a, b, c, d or q")
        user_choice = input('Please enter your choice: ')
        print()
    if user_choice == "a":
        add_expense_with_category()
    elif user_choice == "b":
        print("These are the records so far: \n")
        txt_read_from_file()
    elif user_choice == "c":
        print("The sum of expenses so far are: \n")
        print_sum_category_expenses()
    elif user_choice == "d":
        print("Enter your income in numbers e.g 37561, 45000 etc.\n")
        plots()

def final_function():
    """
    This is the calling code, also know known as the main function.
    It calls all the codes above it.
    """
    #user_choice = display_options()
    summary()
    print("press e to continue")
    print("press q to quit\n")
    new_input = input("Enter your choice: ")

    while new_input not in ["e", "q"]:
        print("Your choice is incorrect, please choose e or q")
        new_input = input('Please enter your choice: ')
        print()
    if new_input == "e":
        summary()
    elif new_input == "q": 
        print("You have exited the program.")
    return

if __name__ == "__main__":
  final_function()
  