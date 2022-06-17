import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.curdir))
from src import generate_expenses as ge, read_file as fe

def test_create_random_data() -> None:
    list_of_keys = ("name", "cost_in_Euros", "date", "category")
    value_type = (str, float, int, np.str_, np.float64)
    
    for dictionary in ge.create_random_data():
        for key, value in dictionary.items():
            assert key in list_of_keys
            assert type(value) in value_type 
            
        assert type(dictionary) is dict
    assert type(ge.create_random_data()) is list
   
