from user_validation import validate_input, check_input_is_numeric
from user_validation import check_input_is_positive

def income_expense():
    """
    Take income from user and allocate amount for expenses
    """
    income = validate_input('Please enter your annual income: ', 
                            [check_input_is_numeric, check_input_is_positive])

    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    return expenses, saving

if __name__ == '__main__':
    print(income_expense())
