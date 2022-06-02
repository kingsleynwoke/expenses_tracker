from datetime import date

# App that takes in individual expeneses, 
# give categories and caculates remaining income
# defining variables / classes
# init for each person using the app
class User:
    def __init__(self, name, income):
        self.name = name
        self.income = income
# run Programm _Test
Person1 = User("Maro", 2000)
print(Person1.name, Person1.income)

# # !! ask for income
# # !! save income to a list?

# Ask for the budget of each category
expenses_fixed_budget= input("what is your budget for total budget for expenses in Euros?")
expenses_fixed_budget= input("what is your budget for total budget for expenses in Euros?")
grocery_budget = input("what is your budget for groceries in Euros?")
# # !!! add for all categories

class Expenses:
    def __init__(self, user, expense_text, expense_value, expenses_rem_budget= expenses_fixed_budget):
        self.user = user     
        self.name = expense_text
        self.value = expense_value
        self.rem_budget = int(expenses_rem_budget) - int(self.value)
    def alert(self):
        if self.rem_budget <= self.value:
            print("You have exceeded your budget limit")
# #!!! save each entry to a list in expenses and give the remaining budget from this list bzw. dict

# run programm_ test
# calling methods
Person1_expenses = Expenses(Person1, "BREAD", 5)
print(Person1_expenses.user, Person1_expenses.name, Person1_expenses.value, Person1_expenses.rem_budget)
Person1_expenses = Expenses(Person1, "meat", 10)
print(Person1_expenses.user, Person1_expenses.name, Person1_expenses.value, Person1_expenses.rem_budget)


# subclasses for the expenses categories 
class Groceries(Expenses):
    def __init__(self, user, expense_text, expense_value, grocery_rem_budget= grocery_budget):
        super().__init__(user, expense_text, expense_value)
        self.rem_budget = int(grocery_rem_budget) - int(self.value)
## !! save each entry to a list and give remaining budget from this list bzw. dict
## !! add the rest of categories as subclasses
# run programm_ test
Person1_grocery_expenses = groceries(Person1, "bread", 5)
print(Person1_grocery_expenses.name, Person1_grocery_expenses.value, Person1_grocery_expenses.rem_budget)


# separate method "main".. method at the bottom of the file 
# If it is x, create a new variable called 'expense_type' and assign the subclass
def main():
    choice = input( "Please choose a category: a) groceries, b) entertainment, c) health, d) clothing, e) miscellanous, f) kids, g) travel, h) special occasions, i) hobbies j) transportation k) cosmetic and wellness l) charity, m) others")
    if choice == "a":
        expense_type = Groceries()
    elif choice == "b":
        expense_type = entrertainment()
##!! add the rest of categories