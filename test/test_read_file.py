import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.curdir))
from src import read_file


list_of_keys = ("name", "cost_in_Euros", "date", "category")
value_type = (str, float, int, np.str_, np.float64)

def test_read_from_json() -> None:    
    for element in read_file.read_from_json():
        for key, value in element.items():
            assert element["name"] == element["name"].title()
            assert key in list_of_keys
            assert type(value) in value_type
        assert type(element) is dict
    assert type(read_file.read_from_json()) is list
    