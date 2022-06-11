import re
from datetime import datetime as dt

def check_string_is_alphabetic(input):
    if not (re.match("^[a-zA-Z\s]+$", input) and len(input.strip()) !=0):
        raise ValueError
    return input

def check_input_is_numeric(input):
    return float(input)

def check_input_is_positive(input):
    if input <= 0:
        raise ValueError
    return input

def check_date_format(input):
    if not dt.strptime(input, '%Y-%m-%d'):
        raise ValueError
    return input

def check_expenses_category(input):
    item_category = ("party", "grocery", "charity", "misc", "clothing", "cosmetic", "transport", "insurance")
    if input not in item_category:
        raise ValueError
    return input

def validate_input(prompt, validation_functions_list=[]):
    while True:
        general_input = input(prompt)
        has_failed = False
        for func in validation_functions_list:
            try:
               general_input = func(general_input)
            except ValueError:
                print("\nInvalid input, please try again! ")
                has_failed = True
                break # stop the validations
        if has_failed:
            continue # go back to start of the while loop
        break
    return general_input

if __name__ == '__main__':
    validate_input('Enter your Name: ', [check_string_is_alphabetic])
    validate_input('Enter the amount spent in Euros: ', 
                    [check_input_is_numeric, check_input_is_positive])
    validate_input('Enter date of expenditure in YYYY-MM-DD: ', [check_date_format])
    validate_input("Choose a category e.g cosmetic, party, charity, grocery, clothing, transport, insurance, misc: ",
                    [check_expenses_category])
