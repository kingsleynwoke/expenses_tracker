from read_and_write import json_read_from_file
from datetime import date


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
    Sum amount of each category expenses
    """
    sum_dictionary = {}
    data = create_category_data()
    for key in data.keys():
        sum_dictionary[key] = round(sum(data[key]), 2)
    return sum_dictionary


def print_sum_category_expenses():
    """Print sum of expenses for each category"""
    for key, value in sum_category_expenses().items():
        print(f"{key.title()}: €{value:,}")
    print(f"\nTotal accumulated expenses up till the date of {date.today()} is €{round(sum(sum_category_expenses().values()), 2):,}")


if __name__ == '__main__':
    print_sum_category_expenses()
