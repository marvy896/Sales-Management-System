# This will be able to record each sales, add new sales, remove sales, view sales, and display the total sales amount.

sales = []

# the sales will be collected in a dictionary with the following keys: 'item', 'quantity', 'price'
sales_data = {
    'item': '',
    'quantity': 0,
    'price': 0.0,
    'Total Sale Amount': 0.0
}
def add_sale():
    item = input("Enter the item sold: ")
    quantity = int(input("Enter the quantity sold: "))
    price = float(input("Enter the price of the item: "))
    sales_data['item'] = item
    sales_data['quantity'] = quantity
    sales_data['price'] = price
    sales_data['Total Sale Amount'] = quantity * price
    sales.append(sales_data.copy())
    print("Sale added successfully!")

def view_sales():
    for sale in sales:
        print(f"Item Sold: {sale['item']}, Quantity Sold: {sale['quantity']}, Price: ${sale['price']}, Total Sale Amount: ${sale['Total Sale Amount']}")
        # To display the total sale amount, we can multiply the quantity sold by the price of the item and display it.
        # print(f"Total Sale Amount: ${sale['quantity'] * sale['price']}")

def get_total_sales():
    total_sales = 0
    for sale in sales:
        total_sales += sale['Total Sale Amount']
    print(f"Total Sales Amount: ${total_sales}")

def remove_sale():
    item = input("Enter the item sold you want to remove: ")
    for sale in sales:
        if sale['item'] == item:
            sales.remove(sale)
            print("Sale removed successfully!")
        else:
            print("Sale not found.")

def main():
    while True:
        print("Welcome to the Sales Tracker!")
        print("Please select an option:")
        print("1. Add Sale")
        print("2. View Sales")
        print("3. Get Total Sales")
        print("4. Remove Sale")
        print("5. Exit")
        choice = input()
        if choice == '1':
            add_sale()
        elif choice == '2':
            view_sales()
        elif choice == '3':
            get_total_sales()
        elif choice == '4':
            remove_sale()
        elif choice == '5':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

main()