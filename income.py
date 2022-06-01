def income_expense():
    """
    Take income from user and allocate amount for expenses
    """
    income = float(input("Please enter your income for the year: "))
    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    return expenses, saving

if __name__ == '__main__':
    print(income_expense())
