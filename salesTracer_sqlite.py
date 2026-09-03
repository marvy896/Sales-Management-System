import sqlite3
connection = sqlite3.connect('sales.db')
cursor = connection.cursor()
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")
import shutil
import os

def backup_database():
    if not os.path.exists('sales.db'):
        print("No database file found to backup.")
        return
    os.makedirs('backup', exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    backup_file = f'backup/sales_backup_{timestamp}.db'
    shutil.copy2('sales.db', backup_file)
    print(f"Database backup created: {backup_file}")
    
def cleanup_backups():
    backup_dir = 'backup'
    if not os.path.exists(backup_dir):
        return
    backups = sorted(
        file for file in os.listdir(backup_dir) 
        if file.startswith('sales_backup_') and file.endswith('.db')
        )
    
    while len(backups) > 5:
        oldest_backup = backups.pop(0)
        os.remove(os.path.join(backup_dir, oldest_backup))
        print(f"Deleted old backup: {oldest_backup}")

def run_automation():
    backup_database()
    cleanup_backups()
    
    
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (sale_id INTEGER PRIMARY KEY AUTOINCREMENT, 
customer TEXT, 
item TEXT, 
quantity INTEGER, 
price REAL, 
total REAL,
datetime TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

connection.commit()

def display_sales():
    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()
    if not rows:
        print("No sales records found.")
        return
    print("=" * 80)
    print(f"{'Sale ID':<10}{'Customer':<20}{'Item':<20}{'Quantity':<10}{'Price':<10}{'Total':<10}{'Date/Time':<20}")
    print("=" * 80)
    for row in rows:
        sale_id, customer, item, quantity, price, total, date_time = row
        print(f"{sale_id:<10}{customer:<20}{item:<20}{quantity:<10}{price:<10.2f}{total:<10.2f}{date_time:<20}")
    print("=" * 80)
    
# now we have to get our addsale function to add sales to the database, 
# we will ask the user to input the sales data and we will insert it into the database.

def get_valid_quantity():
    while True:
            try:
                quantity = int(input("Enter the quantity sold: "))
                if quantity <= 0:
                    print("Quantity cannot be zero or negative. Please enter a valid number.")
                    continue
                return quantity
            
            except ValueError:
                print("Invalid input for quantity. Please enter a valid number.")
                continue

def get_valid_price():
    while True:
            try:
                price = float(input("Enter the price of the item: "))
                if price <= 0:
                    print("Price cannot be zero or negative. Please enter a valid number.")
                    continue
                return price
            except ValueError:
                print("Invalid input for price. Please enter a valid number.")
                continue

def get_valid_text(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("Input cannot be empty. Please enter a valid value.")
            continue
        return text
    
def add_sale():
  
    customer = get_valid_text("Enter your Name: ")
    item = get_valid_text("Enter the item sold: ")
    quantity = get_valid_quantity()
    price = get_valid_price()
    
    cursor.execute('''
               INSERT INTO sales (customer, item, quantity, price, total) VALUES (?, ?, ?, ?, ?)
               ''', (customer, item, quantity, price, quantity * price))
    connection.commit()
    print("Sale added successfully!")

# Next is to write the remove sale fuction
   
def remove_sale():
    sales_id = input("Enter the ID of the sale you want to remove: ")

    cursor.execute("SELECT * FROM sales WHERE sale_id = ?", (sales_id,))
    row = cursor.fetchone()

    if not row:
        print("No records found.")
        return

    cursor.execute("DELETE FROM sales WHERE sale_id = ?", (sales_id,))
    connection.commit()

    print("Sale removed successfully.")        

# lets add the search Fuction
def search_sale():
    search = input("Enter the Name of the customer you want to search: ")
    cursor.execute("SELECT * FROM sales WHERE LOWER(customer) = LOWER(?)", (search,))
    results = cursor.fetchall()
    
    if not results:
        print("No Customer found")
        return
    for row in results:
           sale_id, customer, item, quantity, price, total, date_time = row
           print(f"{sale_id:<10}{customer:<20}{item:<20}{quantity:<10}{price:<10.2f}{total:<10.2f}{date_time:<20}")
           print("=" * 80)
        

# Lets createhe edit function with validations
def get_optional_quantity(prompt):
    while True:
        quantity = input(prompt).strip()
        if quantity == "":
            return None
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Quantity cannot be zero or negative. Please enter a valid number.")
                continue
            return quantity
        except ValueError:
            print("Invalid input for quantity. Please enter a valid number.")
            continue
        
def get_optional_price(prompt):
    while True:
        price = input(prompt).strip()
        if price == "":
            return None
        try:
            price = float(price)
            if price <= 0:
                print("Price cannot be zero or negative. Please enter a valid number.")
                continue
            return price
        except ValueError:
            print("Invalid input for price. Please enter a valid number.")
            continue
        
def get_optional_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            return None
        return text
    
def edit_sale():
    sale_id = input("Enter the ID of the customer you want to edit: ")
    cursor.execute(
            "SELECT * FROM sales WHERE sale_id = ?",
            (sale_id,)
        )
    results = cursor.fetchone()
    
    if not results:
        print("No Sale found")
        return
    print("\nCurrent sale details:")
    print("=" * 80)
    print(f"Sale ID: {results[0]}")
    print(f"Customer: {results[1]}")
    print(f"Item: {results[2]}")
    print(f"Quantity: {results[3]}")
    print(f"Price: ₦{results[4]:,.2f}")
    print(f"Total: ₦{results[5]:,.2f}")
    print("=" * 80)

    print("\nEnter the new details for the sale.")
    print("Leave blank to keep the current value.\n")
       
    new_customer = get_optional_text("Enter the new customer's name: ")
    new_item = get_optional_text("Enter the new item sold: ")
    new_quantity = get_optional_quantity("Enter the new quantity sold: ")
    new_price = get_optional_price("Enter the new price: ")

    customer = results[1] if new_customer is None else new_customer
    item = results[2] if new_item is None else new_item
    quantity = results[3] if new_quantity is None else new_quantity
    price = results[4] if new_price is None else new_price
   

    # Recalculate total
    total = quantity * price
    
    cursor.execute("""
    UPDATE sales
    SET customer = ?,
        item = ?,
        quantity = ?,
        price = ?,
        total = ?
    WHERE sale_id = ?
""", (customer, item, quantity, price, total, sale_id))
    connection.commit()
    print("Sale edited successfully!")             
           
    
def sales_report():
    cursor.execute("""
        SELECT 
            COUNT(*),
            SUM(quantity),
            SUM(total),
            AVG(total),
            MAX(total),
            MIN(total)
        FROM sales
    """)

    result = cursor.fetchone()

    total_transactions = result[0]
    total_items = result[1]
    total_revenue = result[2]
    average_sale = result[3]
    highest_sale = result[4]
    lowest_sale = result[5]

    if total_transactions == 0:
        print("No sales records found.")
        return

    print("=" * 50)
    print("SALES REPORT".center(50))
    print("=" * 50)

    print(f"Total Transactions : {total_transactions}")
    print(f"Total Items Sold   : {total_items}")
    print(f"Total Revenue      : ₦{total_revenue:,.2f}")
    print(f"Average Sale       : ₦{average_sale:,.2f}")
    print(f"Highest Sale       : ₦{highest_sale:,.2f}")
    print(f"Lowest Sale        : ₦{lowest_sale:,.2f}")

    print("=" * 50)

def daily_sales_report():
    # getDate = input("Enter the date for the daily sales report (YYYY-MM-DD): ")
    cursor.execute(""" SELECT
                   COUNT(*),
                     SUM(quantity),
                     SUM(total),
                     AVG(total),
                     MAX(total),
                     MIN(total)
                     FROM sales
                     WHERE DATE(datetime) = ?""", (today,))
    daily_sales = cursor.fetchone()
    if not daily_sales or daily_sales[0] == 0:
        print("No sales records found for the specified date.")
        return
    total_transactions = daily_sales[0]
    total_items = daily_sales[1]
    total_revenue = daily_sales[2]
    average_sale = daily_sales[3]
    highest_sale = daily_sales[4]
    lowest_sale = daily_sales[5]
    
    print("=" * 50)
    print(f"SALES REPORT FOR {today}".center(50))        
    print("=" * 50)
    print(f"Total Transactions : {total_transactions}")
    print(f"Total Items Sold   : {total_items}")
    print(f"Total Revenue      : ₦{total_revenue:,.2f}")
    print(f"Average Sale       : ₦{average_sale:,.2f}")
    print(f"Highest Sale       : ₦{highest_sale:,.2f}")
    print(f"Lowest Sale        : ₦{lowest_sale:,.2f}")
    print("=" * 50)
                

def Customer_Report():
    customer = input("Put the customers Name: ").strip()
    cursor.execute(
        """SELECT COUNT(*), SUM(quantity), SUM(total), AVG(total),
                  MAX(total), MIN(total)
           FROM sales WHERE LOWER(customer) = LOWER(?)""",
        (customer,)
    )
    
    results = cursor.fetchone()
   
    if not results:
        print("No User found")
        return
    
    total_transactions = cursor.execute("SELECT COUNT(*) FROM sales WHERE customer = ?", (customer,))
    total_items = cursor.execute("SELECT SUM(quantity)) FROM sales WHERE customer = ?", (customer,))
    total_revenue = cursor.execute("SELECT SUM(total)) FROM sales  WHERE customer = ?", (customer,))
    average_sale = cursor.execute("SELECT AVG(total)) FROM sales  WHERE customer = ?", (customer,))
    highest_sale = cursor.execute("SELECT MAX(total) FROM sales  WHERE customer = ?", (customer,))
    lowest_sale = cursor.execute("SELECT MIN(total) FROM sales  WHERE customer = ?", (customer,))
    
        
    print("=" * 50)
    print(f"SALES REPORT FOR {customer}".center(50))        
    print("=" * 50)
    print(f"Total Transactions : {total_transactions}")
    print(f"Total Items Sold   : {total_items}")
    print(f"Total Revenue      : ₦{total_revenue:,.2f}")
    print(f"Average Sale       : ₦{average_sale:,.2f}")
    print(f"Highest Sale       : ₦{highest_sale:,.2f}")
    print(f"Lowest Sale        : ₦{lowest_sale:,.2f}")
    print("=" * 50)
            
def main():
    while True:
        print("=" * 40)
        print("SALES MANAGEMENT SYSTEM".center(40))
        print("1. Display Sales")
        print("2. Add Sale")
        print("3. Delete Sale")
        print("4. Search sale")
        print("5. Edit Sale")
        print("6. Sales Report")
        print("7. Customer Report")
        print("8. Daily Sales Report")
        print("9. Exit")
        print("=" * 40)
        choice = input("Enter your choice (1-9): ")
        
        if choice == "1":
            display_sales()
        elif choice == "2":
            add_sale()
        elif choice == "3":
            remove_sale()
        elif choice == "4":
            search_sale()
        elif choice == "5":
            edit_sale()
        elif choice == "6":
            sales_report()
        elif choice == "7":
            Customer_Report()
        elif choice == "8":
            daily_sales_report()
        elif choice == "9":
            print("Exiting the Sales Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

backup_database()
main()