import random 
import pandas as pd
import numpy as np
from datetime import datetime as dt
from random import choice
import json

def income_expense():
    """
    Take income from user and allocate amount for expenses
    """
    income = float(input("Please enter your income for the year: "))
    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    return expenses

def create_random_data():
    """"
    We need data to do our analysis, since we don't have any we randomely 
    generated one using numpy random module.
    """
    #np.random.seed(0)
    start_date = dt.strptime("2022-01-01", "%Y-%m-%d")
    end_date = dt.strptime("2022-12-31", "%Y-%m-%d")
    create_date = pd.date_range(start_date, end_date)
    date = create_date.strftime("%Y-%m-%d")
    
    data_list = []
    for element in range(120):
        
        users_list = { "name": np.random.choice(['Peter James', 'Saba Sartipi',
                    'Jonny Trump', 'Barack Obama', 
                                       "Mahar Ali", 'James King', 'Gabriel Udoh', "Muhamed Ali"]),
                      "cost_in_Euros": np.round(np.random.uniform(0.55, 450.24), 2),
                      "date": np.random.choice(date),
                      "category": np.random.choice(["party", "grocery", "charity", "misc",
                                                "clothing", "cosmetic", "transport", "insurance"])
                    }
        data_list.append(users_list)
    return data_list

def add_expense_with_category():
    """
    Take user input for each category of expenses, then update the
    create_random_data() function with these informations.

    Manipulate the data using pandas, read and write it to json and text files.
    """
    list_of_entries = create_random_data()
    print("How many data do you want to add, note 0 --> nothing to added.")
    number_of_expenditure = int(input("Enter your choice e.g 0, 1, 2, etc.: "))
    
    if number_of_expenditure == 0:
        print("You added no record.")
    else:
        for i in range(number_of_expenditure):
            name = input("Enter your name: ")
            date = input("Enter date of expenditure in YYYY-MM-DD: ")
            cost_in_Euros = float(input("Enter the amount spent in Euros: "))
            category = str(input("Choose a category e.g cosmetic, party, charity, grocery, clothing, transport, insurance, misc: "))
            entry = {"name": name, "date": date, "cost_in_Euros": cost_in_Euros, "category": category}
            list_of_entries.append(entry)

    user_names = [element[key] 
                    for element in list_of_entries
                    for key in element.keys() 
                    if key == "name"]
    pandas_data = pd.DataFrame(list_of_entries, index=user_names ,
                          columns=["date", "cost_in_Euros", "category" ])                         
    sorted_data = pandas_data.sort_values(by="date", ascending=True)

    file_name = "expenses_record.txt"
    with open(file_name, 'w') as file:
        file.write(sorted_data.to_string())

    file_name = "expenses_record.json"
    with open(file_name, "w") as create_file:
        json.dump(list_of_entries, create_file)

    return list_of_entries

if __name__ == "__main__":
  add_expense_with_category()