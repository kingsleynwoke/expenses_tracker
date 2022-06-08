def income_expense():
    """
    Take income from user and allocate amount for expenses
    """
    while True:
        income = input("Please enter your income for the year: ")
        try:
            income = float(income)
        except ValueError:
            print("\nInvalid entry, must be must be numbers: ")
            continue # go back to start of the while loop
        if income <=0:
            validation_choice = input("You have entered a null or negative income value. Are you sure??? [y/N] ")
            if validation_choice != 'y':
                continue # go back to start of the while loop
        break
    saving = 0.2 * income  # 20% of income
    expenses = 0.8 * income  # 80% of income
    return expenses, saving

if __name__ == '__main__':
    print(income_expense())
