import sys
import os
import pathlib2
from pytest import MonkeyPatch
sys.path.insert(0, os.path.abspath(os.curdir))
from src import user_validation as u_val

def test_validate_input_name(monkeypatch: MonkeyPatch) -> None:
    inputs = ["AHMED James", "peters joyce", "grace"]
    expected_values = ["AHMED James", "peters joyce", "grace"]
    
    for values in expected_values:
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        assert u_val.validate_input('Enter your Name: ', 
                                    [u_val.check_string_is_alphabetic]) == values
    
def test_validate_input_date(monkeypatch: MonkeyPatch) -> None:
    inputs = ["2022-02-12", "2022-5-25"]
    expected_values = ["2022-02-12", "2022-5-25"]
    
    for values in expected_values:
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        assert u_val.validate_input('Enter date of expenditure in YYYY-MM-DD: ', 
                                    [u_val.check_date_format]) == values
       
def test_validate_input_cost(monkeypatch: MonkeyPatch) -> None:
    inputs = ["120", "245.08", "0.47", "0.08"]
    expected_values = ["120", "245.08", "0.47", "0.08"]
    
    for values in expected_values:
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        assert u_val.validate_input('Enter the amount spent in Euros: ', 
                                    [u_val.check_input_is_numeric, u_val.check_input_is_positive]) == float(values)

def test_validate_input_category(monkeypatch: MonkeyPatch) -> None:
    inputs = ["cosmetic", "party", "charity", "grocery", 
              "clothing", "transport", "insurance", "misc"]
    expected_values = ["cosmetic", "party", "charity", "grocery", 
              "clothing", "transport", "insurance", "misc"]
    
    for values in expected_values:
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        assert u_val.validate_input("Choose a category", [u_val.check_expenses_category]) == values
    
def test_create_folder() -> None:
    inputs = ["data01", "data02", "data03"]
    expected_values = pathlib2.Path(os.curdir)
    
    for values in inputs:
        assert u_val.creat_folder(values) == expected_values / values