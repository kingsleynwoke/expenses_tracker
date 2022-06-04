import json
import pandas as pd

def txt_read_from_file():
    """Read text files"""
    file_name = "expenses_record.txt" 
    with open(file_name, 'r') as f:
        print(f.read())

def json_read_from_file():
    """Read json files"""
    file_name = "expenses_record.json"
    with open(file_name) as saved_file:
        file_result = json.load(saved_file)
    return file_result

def xlsx_read_file():
    file_name = "expenses_record.xlsx"
    excel_sheet = pd.read_excel("expenses_record.xlsx")
    print(excel_sheet)

if __name__ == "__main__":
  txt_read_from_file()
  #xlsx_read_file()