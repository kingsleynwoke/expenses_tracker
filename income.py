def income_expense():
    """
    Take income from user and allocate amount for expenses
    """
    while True:
        income = input("Please enter your income for the year: ")
        if income.isnumeric() or type(income)==float:
            income = float(income)
        try:
            income = float(income)
        except ValueError:
            print("\nInvalid entry, must be must be numbers: ")
            continue
        break
    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    return expenses, saving

if __name__ == '__main__':
    print(income_expense())
