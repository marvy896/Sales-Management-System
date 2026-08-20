import sqlite3
connection = sqlite3.connect('sales.db')
cursor = connection.cursor()
from datetime import datetime
next_id = 1

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
cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()
print(rows)

# cursor.execute('''
#                INSERT INTO sales (customer, item, quantity, price, total, datetime) VALUES (?, ?, ?, ?, ?, ?)
#                ''', ("John Doe", "Widget", 5, 10.0, 50.0, "2023-01-01 12:00:00"))
# connection.commit()
# print("Sale added successfully!")

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
    global next_id
    
    customer = get_valid_text("Enter your Name: ")
    item = get_valid_text("Enter the item sold: ")
    quantity = get_valid_quantity()
    price = get_valid_price()
    
    cursor.execute('''
               INSERT INTO sales (customer, item, quantity, price, total, datetime) VALUES (?, ?, ?, ?, ?, ?)
               ''', (customer, item, quantity, price, quantity * price, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    # sales.append(sales_data)
    # next_id += 1
    # save_sales()  # Save the sales data to the JSON file after adding a new sale
    print("Sale added successfully!")
add_sale()
