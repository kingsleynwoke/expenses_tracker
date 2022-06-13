import pandas as pd
from add_expense import create_random_data
from add_expense import add_expense_with_category
import glob


 # create a function that merges two excel files in one
 # user has already a list of expenses and wants to upload to the existing data base

def merge_excel():
 path = input(" Please write the path name  in quotation eg. /Users/<username>/<rest of the path>")
 file_list = glob.glob(path + "/*.xlsx")
 excel_list = []

 for file in file_list:
  excel_list.append(pd.read_excel(file))
 # create a new dataframe to store the merged files
 excel_merged = pd.DataFrame()
 for excel_file in excel_list:
  excel_merged = excel_merged.append(excel_file, ignore_index=True)
  excel_merged.to_excel("total_expense_record.xlsx", index=True)


if __name__ == "__main__":
  merge_excel()