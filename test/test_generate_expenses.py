import sys
import os
import numpy as np
from pytest import MonkeyPatch
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
    
def test_update_existing_data(monkeypatch: MonkeyPatch) -> None:
    """
    the inputs are:
    number_of_expenditure, name. date, cost, category
    """
    inputs = ["1", "Peter James", "2022-04-28", "125.87", "charity"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    assert generate_expenses.update_existing_data() == read_file.read_from_json()

   
