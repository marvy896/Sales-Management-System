# $This will help Business track expenses
# first we need to create a dictionary of expenses, will contain the amount spent, what is what spent for and the
# category. 
# Additionally, we will create a function to add expenses, view expenses, and delete expenses.

expenses = []
expense = {
    "description": "transportation",
    "amount": 50,
    "category": "travel"
}
expense1 = {
    "description": "food",
    "amount": 30,
    "category": "meal"
}
expenses.append(expense)
expenses.append(expense1)

total = 0
for expense in expenses:
    total += expense["amount"]

print(f"Welcome to the Business Expense Tracker! \n"
      f"See your expenses below: {expenses}")
print(f"Total expenses: ${total}")