""" class ExpenseTracker:
    def __init__(self):
        income = float(input("Please enter your income for the month: "))
        self.income = 0.2 * income 
        self.expenses = 0.8 * income
        

    def budgets(self):
        fun_budget = 0.3 * self.expenses  # 30% of expenses
        cosmetic_budget = 0.1 * self.expenses  # 10% of expenses
        grocery_budget = 0.6 * self.expenses  # 60% of expenses

        return fun_budget, cosmetic_budget, grocery_budget
a = ExpenseTracker()
print(a.budgets())
 """
class Something:
    def income_expense_01(self):
        """
        Take income from user, allocate amount for expenses,
        divide expenses budget into different categories
        """
        income = float(input("Please enter your income for the month: "))
        saving = 0.2 * income  # 20% of income
        expenses = 0.8 * income  # 80% of income
        fun_budget = 0.3 * expenses  # 30% of expenses
        cosmetic_budget = 0.1 * expenses  # 10% of expenses
        grocery_budget = 0.6 * expenses  # 60% of expenses

        return fun_budget, cosmetic_budget, grocery_budget

    def __call__(self):
        fun, cosmetic, grocery = self.income_expense_01()
        return f"Fun budget = {fun}, cosmetic = {cosmetic} and grocery = {grocery} "

a = Something()

b = Something()
print(tuple(range(10)))