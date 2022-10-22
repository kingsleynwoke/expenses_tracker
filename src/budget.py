import sys
import os
import numpy as np
from typing import Tuple, Dict, Any

sys.path.insert(0, os.path.abspath(os.curdir))
from src.sum_expenses_data import sum_of_expenses
from src.income import income_expense
from src import user_validation as u_val

def check_budget() -> dict:
    """
    Compare budget allocation against expenses for each category. The following 
    values were allocated as a percentage:
    party_bgt = 0.15,    grocery_bgt = 0.3,  charity_bgt = 0.05,   misc_bgt = 0.1,
    clothing_bgt = 0.1,  cosmetic_bgt = 0.1, transport_bgt = 0.1,  insurance_bgt = 0.1   
    """ 
    expense_data, saved_amount = income_expense()
    from_sum_expenses = sum_of_expenses()
    item_category = u_val.expenses_categories()
    budget_category = tuple(u_val.expenses_in_percentage() * expense_data)      
    balance_dict = {}

    def print_budget(input_budget: float, main_dict: Dict, test_key: str):
        if input_budget < main_dict[test_key]:
            remaining_amount = input_budget - main_dict[test_key]
            balance_dict[test_key] = round(remaining_amount, 2)
        else:
            remaining_amount = input_budget - main_dict[test_key]
            balance_dict[test_key] = round(remaining_amount, 2)

    for key in from_sum_expenses:
        for ind, category in enumerate(item_category):
            if key == category:
                print_budget(budget_category[ind], from_sum_expenses, key)

    return balance_dict

if __name__ == '__main__':
    print(check_budget())