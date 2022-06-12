import user_validation as u_val

def income_expense():
    """
    Take income from user and allocate amount for expenses
    """
    income = validate_input('Please enter your annual income: ', 
                            [u_val.check_input_is_numeric, u_val.check_input_is_positive])

    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    return expenses, saving

if __name__ == '__main__':
    print(income_expense())
