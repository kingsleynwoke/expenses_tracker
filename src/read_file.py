import sys
import os
import json
import pandas as pd
import pathlib2
from typing import List, Dict

sys.path.insert(0, os.path.abspath(os.curdir))
from src import user_validation as u_val


folder = "output"
def read_from_txt() -> str:
    """Read text files"""
    file_name = u_val.creat_folder(folder)/"expenses_record.txt"
    with open(file_name, 'r') as f:
        return f.read()
     

def read_from_json() -> List[Dict]:
    """Read json files"""
    file_name = u_val.creat_folder(folder)/"expenses_record.json"
    with open(file_name) as saved_file:
        file_result = json.load(saved_file)
    return file_result

def read_from_xlsx() -> pd.DataFrame:
    file_name = u_val.creat_folder(folder)/"expenses_record.xlsx"
    excel_sheet = pd.read_excel(file_name)
    return excel_sheet

if __name__ == "__main__":
    print(type(read_from_json))
  
    