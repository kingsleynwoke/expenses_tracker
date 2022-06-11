import json
import pandas as pd
from pathlib2 import Path

#Enter file path
path_ = "C:\\Users\\Chimezie Kingsley\\Desktop\\Redi_School_Python Foundation\\final_redi_project\\output\\"
path_name = Path(path_) # Path is from in-built python pathlib

def read_from_txt():
    """Read text files"""
    file_name = path_name/"expenses_record.txt"
    with open(file_name, 'r') as f:
        print(f.read())

def read_from_json():
    """Read json files"""
    file_name = path_name/"expenses_record.json"
    with open(file_name) as saved_file:
        file_result = json.load(saved_file)
    return file_result

def read_from_xlsx():
    file_name = path_name/"expenses_record.xlsx"
    excel_sheet = pd.read_excel(file_name)
    print(excel_sheet)

if __name__ == "__main__":
    #read_from_txt()
    read_from_xlsx()
    #read_from_json()
    