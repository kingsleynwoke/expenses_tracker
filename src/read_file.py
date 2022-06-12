import json
import pandas as pd
import pathlib2
import user_validation as u_val

folder = "output"
def read_from_txt():
    """Read text files"""
    file_name = u_val.creat_folder(folder)/"expenses_record.txt"
    with open(file_name, 'r') as f:
        print(f.read())

def read_from_json():
    """Read json files"""
    file_name = u_val.creat_folder(folder)/"expenses_record.json"
    with open(file_name) as saved_file:
        file_result = json.load(saved_file)
    return file_result

def read_from_xlsx():
    file_name = u_val.creat_folder(folder)/"expenses_record.xlsx"
    excel_sheet = pd.read_excel(file_name)
    print(excel_sheet)

if __name__ == "__main__":
    #read_from_txt()
    read_from_xlsx()
    #read_from_json()
    