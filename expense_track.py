import random 
import pandas as pd
import numpy as np
from datetime import datetime as dt
from random import choice
from matplotlib import pyplot as plt
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
    We need data to do analysis, since we don't have any we randomely 
    createdone random values for date, amount(cost_in Euros),name and categories. 
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
    Take user input for each category of expenses, then update 
    create_random_data() function with these informations.

    Manipulate the data using pandas, read and write it to json and text files.

    """
    list_of_entries = create_random_data()
    number_of_expenditure = int(input("How many sets of data do you want to add e.g 0, 1, 2 etc.: "))
    print()
    for i in range(number_of_expenditure):
        name = input("Enter your name: ")
        date = input("Enter date of expenditure in YYYY-MM-DD: ")
        cost_in_Euros = float(input("Enter the amount spent in Euros: "))
        category = str(input("Choose a category e.g cosmetic, party, charity, grocery, clothing, transport, insurance, misc: "))
        print()
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

def txt_read_from_file():
    """Read text files"""
    file_name = "expenses_record.txt" 
    with open(file_name, 'r') as f:
        print(f.read())

def json_read_from_file():
    """Read json files"""
    file_name = "expenses_record.json"
    with open(file_name) as saved_file:
        file_result = json.load(saved_file)
    return file_result

def create_category_data():
    """
    Create a dictionary containing only categories of expenses
    as key and their respective amount as values.
    """
    expenses_with_category = json_read_from_file()
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

def sum_category_expenses():
    """
    sum amount of each category expenses
    """
    sum_dictionary = {}
    data = create_category_data()
    for key in data.keys():
        sum_dictionary[key] = round(sum(data[key]), 2)
    return sum_dictionary

def print_sum_category_expenses():
    """Print sum of expenses for each category"""
    for key, value in sum_category_expenses().items():
        print(f"{key}: €{value:,}")

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

def plots():
    """
    Plots bar and pie chart for visualising summary of remaing
    balance and summary ofexpenses
    """
    #Create figures
    plt.style.use(['science', 'notebook', 'grid'])
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 1
    fig0, ax0 = plt.subplots(figsize=(10,8), tight_layout=True)
    fig1, ax1 = plt.subplots(figsize=(10,8), tight_layout=True)

    #Create values for plotting using the following functions
    sum_category_value = sum_category_expenses()
    check_budget_value = check_budget()

    bar_category = [key for key in check_budget_value.keys()]
    bar_values = [value for value in check_budget_value.values()]
    pie_category = [key for key in sum_category_value.keys()]
    pie_values = [value for value in sum_category_value.values()]

    #Plotting begins here.
    #(1) Pie chart
    colors = ["steelblue", "peru", "olive", "silver", 
              "cadetblue", "dimgray", "sienna", "darkgreen"]
    ax0.pie(pie_values, labels=pie_category, autopct='%.1f%%', colors=colors,
            wedgeprops={'linewidth': 1.0, 'edgecolor': 'black'})
    ax0.set_title("Summary of expenses in percentage", fontsize=20, pad=20, color="r", fontweight="bold")
    
    #(2) Bar chart
    new_bar = ax1.bar(bar_category, bar_values, ec="black")
    ax1.set_title("Remaining balance", fontsize=20, pad=20, color="r", fontweight="bold")
    ax1.tick_params(rotation=45)
    ax1.set_xlabel("Categories", labelpad=15)
    ax1.set_ylabel("Expenses in Euros", labelpad=15 )
    ax1.bar_label(new_bar, padding=3, fontsize='x-large')
    ax1.margins(y=0.2)
    
    plt.show()
    fig0.savefig("expenses_pie_chart.jpg", dpi=200)
    fig1.savefig("expenses_bar_chart.jpg", dpi=200)

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
  