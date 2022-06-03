import pandas as pd
import numpy as np
from datetime import datetime as dt
import json
import re

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
        
        users_list = { "name": np.random.choice(['Peter James', 'Saba Angella','Jonny Trump', 
                                                'Barack Ade', "Mahar Schmidt", 'James Kingsley', 
                                                'Jonny Udoh', "Muhamed Sani"]),
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
    categ = ("cosmetic", "party", "charity", "grocery", "clothing", "transport", "insurance", "misc")

    print("How many data do you want to add, note 0 --> nothing to added.")
    number_of_expenditure = int(input("Enter your choice e.g 0, 1, 2, etc.: "))
    
    if number_of_expenditure == 0:
        print("\n###################################")
        print("  !!!  You added no record.  !!!")
        print("###################################")
    else:
        for i in range(number_of_expenditure):
            while True:
                name = input("\nEnter your name: ")
                if not (re.match("^[a-zA-Z\s]+$", name) and len(name.strip()) !=0):
                    print("Invalid entry, name must be alphabetical letter(s).")
                    continue
                break
            while True:
                date = input("Enter date of expenditure in YYYY-MM-DD: ")
                try:
                    dt.strptime(date, '%Y-%m-%d')
                except ValueError:
                    print("\nInvalid date format, date must be in this form YYYY-MM-DD: ")
                    continue
                break
            while True:
                cost_in_Euros = input("Enter the amount spent in Euros: ")
                if cost_in_Euros.isnumeric() or type(cost_in_Euros)==float:
                    cost_in_Euros = float(cost_in_Euros)
                try:
                    cost_in_Euros = float(cost_in_Euros)
                except ValueError:
                    print("\nInvalid entry, amount must be number: ")
                    continue
                break
            while True:
                category = input("Choose a category e.g cosmetic, party, charity, grocery, clothing, transport, insurance, misc: ")
                if category not in categ:
                    print("\nInvalid entry, please choose from the listed category: ")
                    continue
                break
            entry = {"name": name.title(), "date": date, "cost_in_Euros": cost_in_Euros, "category": category}
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
    print()
    return list_of_entries

if __name__ == "__main__":
  add_expense_with_category()