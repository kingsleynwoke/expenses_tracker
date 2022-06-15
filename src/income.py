#import user_validation as u_val
import sys
import os
sys.path.insert(0, os.path.abspath(os.curdir))

from redi_project.src import user_validation as u_val
from typing import Callable, Dict

def income_expense() -> Dict[float, float]:
    """
    Take income from user and allocate amount for expenses
    """
    income = u_val.validate_input('Please enter your annual income: ', 
                            [u_val.check_input_is_numeric, u_val.check_input_is_positive])

    saving: float = 0.2 * income  # 20% of income
    expenses: float = 0.8 * income  # 80% of income
    return expenses, saving

if __name__ == '__main__':
    print(income_expense())
