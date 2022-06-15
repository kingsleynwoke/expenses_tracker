import pathlib2
import sys
import typing

cwd_path = pathlib2.Path.cwd().resolve()
# src_path = cwd_path.parent/"src"
#sys.path.insert(0, r"C:\Users\Chimezie Kingsley\Desktop\Redi_School_Python Foundation\final_redi_project")
sys.path.insert(0, str(cwd_path.parent))
# if __name__ == '__main__':
#     print(uv.expenses_budget)
import src.income as vc
print(vc.income_expense())
#import src.budget



print(cwd_path.parent)