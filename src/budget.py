import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.curdir))
from redi_project.src.sum_expenses_data import sum_of_expenses
from redi_project.src.income import income_expense
from redi_project.src import user_validation as u_val

def check_budget():
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

    def print_budget(input_budget, main_dict, test_key):
        if input_budget < main_dict[test_key]:
            remaining_amount = input_budget - main_dict[test_key]
            balance_dict[test_key] = round(remaining_amount, 2)
            #print(f"You have exceeded your {test_key} budget by -€{abs(remaining_amount):.2f}")
        else:
            remaining_amount = input_budget - main_dict[test_key]
            balance_dict[test_key] = round(remaining_amount, 2)
            #print(f"You still have €{remaining_amount:.2f} for {test_key} budget")

    for key in from_sum_expenses:
        for ind, category in enumerate(item_category):
            if key == category:
                print_budget(budget_category[ind], from_sum_expenses, key)

    return balance_dict

if __name__ == '__main__':
    print(check_budget())