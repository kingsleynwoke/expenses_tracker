import sys
import os
sys.path.insert(0, os.path.abspath(os.curdir))

from src.read_file import read_from_json
from src.income import income_expense

def create_key_data():
    """
    Create a dictionary containing only categories of expenses
    as key and their respective amount as values.
    """
    expenses_with_category = read_from_json()

    new_category = []
    for index_value in expenses_with_category:
        new_category.append(index_value['category'])

    category_data = {}
    for name in new_category:
        temp_data = []
        for element in expenses_with_category:
            if element['category'] == name:
                temp_data.append(element['cost_in_Euros'])
        category_data[name] = temp_data
    return category_data

def sum_of_expenses():
    """
    Sum amount of each category expenses
    """
    sum_dictionary = {}
    data = create_key_data()
    for key in data.keys():
        sum_dictionary[key] = round(sum(data[key]), 2)
    return sum_dictionary

def print_summary_of_expenses():
    """Print sum of expenses for each category"""
    expense_amt, saved_amt = income_expense()
    print("\n################################################################")
    print(" !!! The allocated savings and sum of expenses so far are  !!!")
    print("################################################################\n")

    for key, value in sum_of_expenses().items():
        print(f"{key.title()}  = €{value:,}")
    summ = round(sum(sum_of_expenses().values()), 2)

    print("\n--------------------------------------------------------------")
    print(f"Amount allocated for expenses = €{round(expense_amt, 2):,}")
    print(f"Amount allocated for savings  = €{round(saved_amt, 2):,}")
    print(f"Total expenditure             = €{summ:,}")
    print(f"Expenses balance              = €{round(expense_amt - summ, 2):,}")
    
    print("--------------------------------------------------------------\n")

if __name__ == '__main__':
    print_summary_of_expenses()