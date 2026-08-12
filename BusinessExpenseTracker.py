# $This will help Business track expenses
# first we need to create a dictionary of expenses, will contain the amount spent, what is what spent for and the
# category. 
# Additionally, we will create a function to add expenses, view expenses, and delete expenses.
# so basically, create a dictionary of expenses, appended it to a list and then create functions to add, view and delete expenses.

expenses = []
# expense = {
#     "description": "transportation",
#     "amount": 50,
#     "category": "travel"
# }
# expense1 = {
#     "description": "food",
#     "amount": 30,
#     "category": "meal"
# }
# expenses.append(expense)
# expenses.append(expense1)

# Now we will create a function to add expenses,instead of hardcoding the expenses, we will ask the user to input the expenses.
def add_expense():
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category of the expense: ")
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully!")
    print(f"Updated expenses: {expenses}")

# now lets create a function to add all the expenses and get the total amount spent.
def getTotal():
    total = 0
    for expense in expenses:
        total += expense["amount"]
        print(f"Total expenses: ${total}")

# Now lets create a function to view all the expenses, we will print the description, amount and category of each expense.
def view_expenses():
    for expense in expenses:
        print(f"Description: {expense['description']}, Amount: ${expense['amount']}, Category: {expense['category']}")

# lets add the delete expense function, we will ask the user to input the description of the expense they want to delete and we will remove it from the expenses list.
def delete_expense():
    description = input("Enter the description of the expense you want to delete: ")
    for expense in expenses:
        if expense["description"] == description:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            print(f"Updated expenses: {expenses}")
            return
    print("Expense not found.")

while True:
    print("Welcome to the Business Expense Tracker!")
    print("Please select an option:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Get total expenses")
    print("4. Delete an expense")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        getTotal()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Thank you for using the Business Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")

