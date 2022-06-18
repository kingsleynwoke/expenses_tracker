import sys
import os
sys.path.insert(0, os.path.abspath(os.curdir))
from src import sum_expenses_data

def test_create_key_data() -> None:
    expenses_type = ["cosmetic", "party", "charity", "grocery", 
                  "clothing", "transport", "insurance", "misc"]
    
    for key, value in sum_expenses_data.create_key_data().items():
        for val in value:
            assert type(val) is (float or int)
        assert key in expenses_type
        assert key.isalpha()
        assert type(value) is list
    assert type(sum_expenses_data.create_key_data()) is dict
    
def test_sum_of_expenses() -> None:
    expenses_type = ["cosmetic", "party", "charity", "grocery", 
                  "clothing", "transport", "insurance", "misc"]
    
    for key, value in sum_expenses_data.sum_of_expenses().items():          
        assert key in expenses_type
        assert key.isalpha()
        assert type(value) is (float or int)
    assert type(sum_expenses_data.create_key_data()) is dict
    