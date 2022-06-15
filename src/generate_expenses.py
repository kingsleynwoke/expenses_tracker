import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime as dt
import json
import re
import pathlib2
sys.path.insert(0, os.path.abspath(os.curdir))

from src import user_validation as u_val

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

def update_existing_data():
    """
    Take user input for each category of expenses, then update the
    create_random_data() function with these informations.

    Manipulate the data using pandas, read and write it to json and text files.
    """
    list_of_entries = create_random_data()

    print("How many data do you want to add, note 0 --> nothing to added.")
    while True:
        number = input("Enter your choice e.g 0, 1, 2, etc.: ")
        if number.isnumeric():
            number_of_expenditure = int(number)
        else:
            print("\nInvalid, entry must be a number: ")
            continue
        break
    if number_of_expenditure == 0:
        print("\n################################################################################")
        print("  !!!  You added no record, check 'output' directory for existing records  !!!")
        print("################################################################################")
    else:
        for i in range(number_of_expenditure):
            name = u_val.validate_input('\nEnter your Name: ', [u_val.check_string_is_alphabetic])
            
            date = u_val.validate_input('Enter date of expenditure in YYYY-MM-DD: ', [u_val.check_date_format])
            cost_in_Euros = u_val.validate_input('Enter the amount spent in Euros: ', 
                                            [u_val.check_input_is_numeric, u_val.check_input_is_positive])
           
            category = u_val.validate_input("Choose a category e.g cosmetic, party, charity, grocery, clothing, transport, insurance, misc: ",
                                      [u_val.check_expenses_category])

            entry = {"name": name.title(), "date": date, "cost_in_Euros": cost_in_Euros, "category": category}
            list_of_entries.append(entry)
        print("\n############################################################")
        print(" !!!   Check 'output' directory for updated records  !!!! ")
        print("##########################################################")

    user_names = [element[key] for element in list_of_entries for key in element.keys() if key == "name"]

    pandas_data = pd.DataFrame(list_of_entries, index=user_names ,
                          columns=["date", "cost_in_Euros", "category" ])                         
    sorted_data = pandas_data.sort_values(by="date", ascending=True)
    excel_sorted = pd.DataFrame(list_of_entries, columns=["name", "date", "cost_in_Euros", "category" ])
    excel_sorted_data = excel_sorted.sort_values(by="date", ascending=True)

    #create and write to excel file
    directory_name = "output"
    file_name0 = u_val.creat_folder(directory_name)/"expenses_record.xlsx"
    excel_sorted_data.to_excel(file_name0, index=False) 
     
    #create and write to txt file
    file_name1 = u_val.creat_folder(directory_name)/"expenses_record.txt"
    with open(file_name1, 'w') as file:
        file.write(sorted_data.to_string())

    #create and write to json file
    file_name2 = u_val.creat_folder(directory_name)/"expenses_record.json"
    with open(file_name2, "w") as create_file:
        json.dump(list_of_entries, create_file)
    print()
    return list_of_entries

if __name__ == "__main__":
    update_existing_data()