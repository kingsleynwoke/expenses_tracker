import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.curdir))
from src import generate_expenses
from src import read_file

def test_create_random_data() -> None:
    list_of_keys = ("name", "cost_in_Euros", "date", "category")
    value_type = (str, float, int, np.str_, np.float64)
    
    functions = [generate_expenses.create_random_data,
                 read_file.read_from_json]
            
    for dictionary in generate_expenses.create_random_data():
        for key, value in dictionary.items():
            assert key in list_of_keys
            assert type(value) in value_type 
        assert type(dictionary) is dict
    assert type(generate_expenses.create_random_data()) is list
    
def test_update_existing_data() -> None:
    """
    The return value of update_existing_data() returns a list whose 
    elements contains keys that had been tested in test_user_validation.
    The return writen as json file will be rather be tested.
    """
    list_of_keys = ("name", "cost_in_Euros", "date", "category")
    value_type = (str, float, int, np.str_, np.float64)
    
    for element in read_file.read_from_json():
        for key, value in element.items():
            assert element["name"] == element["name"].title()
            assert key in list_of_keys
            assert type(value) in value_type
        assert type(element) is dict
    assert type(read_file.read_from_json()) is list
    
   
