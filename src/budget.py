import numpy as np
from income import income_expense
from sum_expenses_data import sum_of_expenses

def check_budget():
    """
    Compare budget allocation against expenses for each category. The following 
    values were allocated as a percentage:
    party_bgt = 0.15,    grocery_bgt = 0.3,  charity_bgt = 0.05,   misc_bgt = 0.1,
    clothing_bgt = 0.1,  cosmetic_bgt = 0.1, transport_bgt = 0.1,  insurance_bgt = 0.1   
    """
    expense_data, saved_amount = income_expense()
    from_sum_expenses = sum_of_expenses()
    item_category = ("party", "grocery", "charity", "misc", "clothing", "cosmetic", "transport", "insurance")
    budget_category = tuple(np.array([0.15, 0.3, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1]) * expense_data)   
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