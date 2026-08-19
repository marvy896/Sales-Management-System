# This will be able to record each sales, add new sales, remove sales, view sales, and display the total sales amount.

sales = []
next_id = 1
# the sales will be collected in a dictionary with the following keys: 'item', 'quantity', 'price'
# lets add an id to each sales, itll be a unique id for each sale.
# lets add date and time to each sale, so we can track when the sale was made.

from datetime import datetime
# Now lets advance into using Json to save file instead of using a list, so we can easily read and write data to the file.
import json

# lets teach python to save sales to a JSON file
def save_sales():
    with open("sales.json", "w") as file:
        json.dump(sales, file, indent=4)

def load_sales():
    global sales
    global next_id
  
    try:
        with open("sales.json", "r") as file:
            sales = json.load(file)
    except FileNotFoundError:
        sales = []
    if sales:
        next_id = max(int(sale['sale_id']) for sale in sales) + 1

# Let's create helper functions that'll reduce the length of the add sales
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
    
    sales_data = {
    'sale_id': str(next_id),
    'customer': customer,
    'item': item,
    'quantity': quantity,
    'price': price,
    'total': quantity * price,
    'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}
    sales.append(sales_data)
    next_id += 1
    save_sales()  # Save the sales data to the JSON file after adding a new sale
    print("Sale added successfully!")

def display_sale(sale):
    print(f"Sale ID: {sale['sale_id']}, Customer's Name: {sale['customer']}, Item Sold: {sale['item']}, Quantity Sold: {sale['quantity']}, Price: ₦{sale['price']:,.2f}, Total Sale Amount: ₦{sale['total']:,.2f}, Date and Time: {sale['date_time']}")

def view_sales():
    if not sales:
        print("No sales recorded yet.")
        return
    for sale in sales:
        display_sale(sale)
        # print(f"Sale ID: {sale['sale_id']}, Customer's Name: {sale['customer']}, Item Sold: {sale['item']}, Quantity Sold: {sale['quantity']}, Price: ₦{sale['price']}, Total Sale Amount: ₦{sale['total']}, Date and Time: {sale['date_time']}")
        # # To display the total sale amount, we can multiply the quantity sold by the price of the item and display it.
        # # print(f"Total Sale Amount: ${sale['quantity'] * sale['price']}")

def get_total_sales():
    total_sales = 0
    for sale in sales:
        total_sales += sale['total']
    print(f"Total Sales Amount: ₦{total_sales:,.2f}")

def remove_sale():
    sales_id = input("Enter the ID of the sale you want to remove: ")
    for sale in sales:
        if sale['sale_id'] == sales_id:
            sales.remove(sale)
            save_sales()  # Save the sales data to the JSON file after removing a sale
            print("Sale removed successfully!")
            return
    print("Sale not found.")
def search_sale():
    if not sales:
        print("No sales recorded yet.")
        return
    customer_name = input("Enter the customer's name to search for sales: ").strip().lower()
    found = False
    for sale in sales:
        if sale['customer'].lower() == customer_name:
            display_sale(sale)
            found = True
    if not found:
        print("Sale not found.")
        
def sales_report():
    if not sales:
        print("No sales recorded yet.")
        return
    total_transactions = len(sales)
    total_items = 0
    for sale in sales:
        total_items += sale['quantity']
                
    total_items_sold = total_items
    total_revenue = 0
    for sale in sales:
        total_revenue += sale['total']
    average_sale_amount = total_revenue / total_transactions if total_transactions > 0 else 0
    print("=" * 40)
    print("SALES MANAGEMENT SYSTEM".center(40))
    print(f'Total Transactions: {total_transactions}')
    print(f'Total Items Sold: {total_items_sold}')
    print(f'Total Revenue: ₦{total_revenue:,.2f}')
    print(f'Average Sale Amount: ₦{average_sale_amount:,.2f}')
    print("=" * 40)


def main():
    
    while True:
        print("\nPlease select an option:")
        print("1. Add Sale")
        print("2. View Sales")
        print("3. Get Total Sales")
        print("4. Remove Sale")
        print("5. Search Sale")
        print("6. Sale Report")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            add_sale()
        elif choice == '2':
            view_sales()
        elif choice == '3':
            get_total_sales()
        elif choice == '4':
            remove_sale()
        elif choice == '5':
            search_sale()
        elif choice == '6':
            sales_report()
        elif choice == '7':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

load_sales()
main()