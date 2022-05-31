import random 
import pandas as pd
import numpy as np
from datetime import datetime as dt
from random import choice
from matplotlib import pyplot as plt
import json

from income import income_expense
from sum_category import sum_category_expenses

def check_budget():
    """
    Compare budget allocation against expenses for each category. The following 
    values were allocated as a percentage of expenses for each category:
    party_bgt = 0.15,    grocery_bgt = 0.3,  charity_bgt = 0.05,   misc_bgt = 0.1,
    clothing_bgt = 0.1,  cosmetic_bgt = 0.1, transport_bgt = 0.1,  insurance_bgt = 0.1   
    """
    expense_data = income_expense()
    from_sum_dictionary = sum_category_expenses()
    budget = tuple(np.array([0.15, 0.3, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1]) * expense_data)   
    balance_dict = {}

    def print_budget(input_budget, main_dict, test_key):
        if input_budget < main_dict[test_key]:
            remaining_amount = input_budget - main_dict[test_key]
            balance_dict[test_key] = round(remaining_amount, 2)
        else:
            remaining_amount = input_budget - main_dict[test_key]
            balance_dict[test_key] = round(remaining_amount, 2)
    
    for key in from_sum_dictionary:
        if key == "party":
            print_budget(budget[0], from_sum_dictionary, key)
        elif key == "grocery":
            print_budget(budget[1], from_sum_dictionary, key)
        elif key == "charity":
            print_budget(budget[2], from_sum_dictionary, key)
        elif key == "misc":
            print_budget(budget[3], from_sum_dictionary, key)
        elif key == "clothing":
            print_budget(budget[4], from_sum_dictionary, key)
        elif key == "cosmetic":
            print_budget(budget[5], from_sum_dictionary, key)
        elif key == "transport":
            print_budget(budget[6], from_sum_dictionary, key)  
        elif key == "insurance":
            print_budget(budget[7], from_sum_dictionary, key)        
    return balance_dict

if __name__ == '__main__':
    check_budget()