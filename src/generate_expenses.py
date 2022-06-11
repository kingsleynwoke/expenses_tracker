import pandas as pd
import numpy as np
from datetime import datetime as dt
import json, re
from pathlib2 import Path
from user_validation import validate_input, check_string_is_alphabetic
from user_validation import check_input_is_numeric, check_input_is_positive
from user_validation import check_date_format, check_expenses_category

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
        print("\n###################################")
        print("  !!!  You added no record.  !!!")
        print("###################################")
    else:
        for i in range(number_of_expenditure):
            name = validate_input('\nEnter your Name: ', [check_string_is_alphabetic])
            
            date = validate_input('Enter date of expenditure in YYYY-MM-DD: ', [check_date_format])
            cost_in_Euros = validate_input('Enter the amount spent in Euros: ', 
                                            [check_input_is_numeric, check_input_is_positive])
           
            category = validate_input("Choose a category e.g cosmetic, party, charity, grocery, clothing, transport, insurance, misc: ",
                                      [check_expenses_category])

            entry = {"name": name.title(), "date": date, "cost_in_Euros": cost_in_Euros, "category": category}
            list_of_entries.append(entry)
    
    user_names = [element[key] for element in list_of_entries for key in element.keys() if key == "name"]

    pandas_data = pd.DataFrame(list_of_entries, index=user_names ,
                          columns=["date", "cost_in_Euros", "category" ])                         
    sorted_data = pandas_data.sort_values(by="date", ascending=True)
    excel_sorted = pd.DataFrame(list_of_entries, columns=["name", "date", "cost_in_Euros", "category" ])
    excel_sorted_data = excel_sorted.sort_values(by="date", ascending=True)

    #get folder
    path_ = "C:\\Users\\Chimezie Kingsley\\Desktop\\Redi_School_Python Foundation\\final_redi_project\\output\\"
    path_name = Path(path_)  # Path is from in-built python pathlib

    #create and write to excel file
    file_name0 = path_name/"expenses_record.xlsx"
    excel_sorted_data.to_excel(file_name0, index=False) 
     
    #create and write to txt file
    file_name1 = path_name/"expenses_record.txt"
    with open(file_name1, 'w') as file:
        file.write(sorted_data.to_string())

    #create and write to json file
    file_name2 = path_name/"expenses_record.json"
    with open(file_name2, "w") as create_file:
        json.dump(list_of_entries, create_file)
    print()
    return list_of_entries

if __name__ == "__main__":
    update_existing_data()