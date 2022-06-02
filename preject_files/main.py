def income_expense_01():
    """
    Take income from user, allocate amount for expenses,
    divide expenses budget into different categories
    """
    income = float(input("Please enter your income for the month: "))
    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    fun_budget = 0.3 * expenses  # 30% of expenses
    cosmetic_budget = 0.1 * expenses  # 10% of expenses
    grocery_budget = 0.6 * expenses  # 60% of expenses

    return fun_budget, cosmetic_budget, grocery_budget

def add_expense_with_category():
    """
    Create database for each expenses according to their category.
    We just artificially created 1 list for each category, we then
    update it through user input. This is to reduce presentation
    time
    """
    list_of_entries = [{'date': '22-3-2022', 'description': 'concert ticket', \
                        'amount': 195.01, 'category': 'fun'},
                       
                       {'date': '23-3-2022', 'description': 'lipstick', \
                        'amount': 80.09, 'category': 'cosmetic'},
                       
                       {'date': '24-3-20222', 'description': 'Aldi shopping diverse',\
                        'amount': 350.15, 'category': 'grocery'}]

    number_of_expenditure = int(input("Please enter how many times you spent money for each category: "))
    print()
    for i in range(number_of_expenditure):
        description = str(input("Please enter a description of purchased items: "))
        amount = float(input("Please enter the amount spent in Euros: "))
        category = str(input("Please choose a category e.g cosmetic, fun, grocery: "))
        date = input("Please enter date of expenditure in DD-MM-YYYY: ")
        print()
        entry = {"date": date, "description": description, "amount": amount, "category": category}
        list_of_entries.append(entry)

    return list_of_entries


# add_expense_with_category() -->  [{'date': '22-3-2022', 'description': 'concert ticket', 'amount': 95.01, 'category': 'fun'},
#                                   {'date': '23-3-2022', 'description': 'lipstick', 'amount': 50.09, 'category': 'cosmetic'},
#                                   {'date': '24-3-20222', 'description': 'Aldi shopping diverse', 'amount': 150.15, 'category': 'grocery'}]

def create_category_data01():
    """
    Create a dictionary containing only categories of expenses
    as key and their respective amount as values.
    """
    list_of_entries2 = add_expense_with_category()
    new_category = []

    for index_value in list_of_entries2:
        new_category.append(index_value['category'])

    category_data01 = {}
    for name in new_category:
        temp_data = []
        for element in list_of_entries2:
            if element['category'] == name:
                temp_data.append(element['amount'])
        category_data01[name] = temp_data

    return category_data01

# create_category_data01()  -->  {'cosmetic': [50.09, 15.0], 'fun': [95.01, 25.45], 'grocery': [150.15]}

def sum_category_expenses():
    """
    sum amount of each category expenses
    """
    category_expense = create_category_data01()
    sum_dictionary = {}
    for key in category_expense.keys():
        sum_dictionary[key] = round(sum(category_expense[key]), 2)

    return sum_dictionary

# sum_category_expenses()  -->  {'cosmetic': 65.09, 'fun': 120.46, 'grocery': 150.15}

def check_budget():
    """
    Compare budget allocation against expenses for each category.
    """
    fun_budget, cosmetic_budget, grocery_budget = income_expense_01()
    from_sum_dictionary = sum_category_expenses()

    def print_budget(input_budget, main_dict, test_key):
        if input_budget < main_dict[test_key]:
            remaining_amount = input_budget - main_dict[test_key]
            print(f"You have exceeded your {test_key} budget by \
                  -€{abs(remaining_amount):.2f}")
        else:
            remaining_amount = input_budget - main_dict[test_key]
            print(f"You still have €{remaining_amount:.2f} for {test_key} budget")

    for key in from_sum_dictionary:
        if key == "fun":
            print_budget(fun_budget, from_sum_dictionary, key)

        elif key == "cosmetic":
            print_budget(cosmetic_budget, from_sum_dictionary, key)

        elif key == "grocery":
            print_budget(grocery_budget, from_sum_dictionary, key)

def display_options():
    """
    Create a menu like option to aid user input.
    """
    print("\nWelcome to expense tracker!\n")
    print("Press a to add new record or view balance.")
    print("Press b to view sum of category expenses.")
    print("Press c to view record.")
    print("Press q to quit. \n")

    user_input = input('Please enter your choice: ')
    user_input = user_input.lower()

    print()
    return user_input

def summary():
    """
    Based on user input above execute the if statements.
    """
    user_choice = display_options()
    while user_choice not in ["a", "b", "c", "q"]:
        print("Your choice is incorrect, please choose from a, b, c or q")
        
        user_choice = input('Please enter your choice: ')
        print()
        user_choice = user_choice.lower()

    if user_choice == "a":
        check_budget()

    elif user_choice == "b":
        print(f"The sum of expenses in Euros for each category is: {sum_category_expenses()}")

    elif user_choice == "c":
        print("The expenses records are: ", *add_expense_with_category(), sep="\n")

    elif user_choice == "q":
        print("You have exited the program.")

def final_function():
    """
    This is the calling code, also know known as the main function.
    It calls all the codes above it.
    """
    result = summary()
    return result

if __name__ == "__main__":
  final_function()