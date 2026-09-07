# Sales Management System

A beginner-friendly Python Sales Management System built progressively while learning Python, SQL, SQLite, file handling, validation, reporting, and basic automation.

## Project Overview

This project started as a simple Python program for recording sales and gradually evolved into a persistent SQLite-based sales management application.

The system allows a user to:

- Add sales
- Display sales
- Search for sales by customer
- Edit existing sales
- Delete sales
- Calculate sale totals automatically
- Generate daily sales reports
- Back up the SQLite database
- Automatically clean up old backups

## Technologies Used

- Python 3
- SQLite
- SQL
- `sqlite3`
- `datetime`
- `os`
- `shutil`

No external Python packages are required for the core application.

## Database Structure

The application uses a SQLite database called:

```text
sales.db
```

The main table is:

```sql
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    item TEXT,
    quantity INTEGER,
    price REAL,
    total REAL,
    datetime TEXT DEFAULT CURRENT_TIMESTAMP
);
```

### Fields

| Field | Description |
|---|---|
| `sale_id` | Unique ID for each sale |
| `customer` | Name of the customer |
| `item` | Product or service sold |
| `quantity` | Number of units sold |
| `price` | Price per unit |
| `total` | Quantity × price |
| `datetime` | Date and time the sale was recorded |

## Main Features

### 1. Add Sale

The user can enter:

- Customer name
- Item
- Quantity
- Price

The system automatically calculates:

```text
Total = Quantity × Price
```

and stores the sale in SQLite.

### 2. Display Sales

All recorded sales can be displayed in a structured table showing:

```text
Sale ID
Customer
Item
Quantity
Price
Total
Date/Time
```

### 3. Search Sales

Sales can be searched by customer name.

The search was designed to be case-insensitive, meaning:

```text
Marvel
marvel
MARVEL
```

can match the same customer.

### 4. Edit Sale

An existing sale can be edited using its `sale_id`.

The user can leave a field blank when they do not want to change it.

For example:

```text
Enter new customer name (leave blank to keep current):
```

The system keeps the existing value when the user presses Enter without entering a new value.

The total is recalculated automatically after editing:

```text
total = quantity × price
```

### 5. Delete Sale

A sale can be deleted by entering its unique `sale_id`.

The system first checks whether the sale exists before deleting it.

### 6. Daily Sales Report

The application can calculate statistics for the current day, including:

- Total transactions
- Total items sold
- Total revenue
- Average sale
- Highest sale
- Lowest sale

Example:

```text
==================================================
              SALES REPORT FOR 2026-09-07
==================================================
Total Transactions : 10
Total Items Sold   : 25
Total Revenue      : ₦250,000.00
Average Sale       : ₦25,000.00
Highest Sale       : ₦70,000.00
Lowest Sale        : ₦5,000.00
==================================================
```

The report can also be saved as a text file in:

```text
reports/
```

with a filename such as:

```text
sales_report_2026-09-07.txt
```

## Database Backup

The project includes automated database backup functionality.

Backups are stored inside:

```text
backup/
```

Example:

```text
backup/
├── sales_backup_2026-09-05.db
├── sales_backup_2026-09-06.db
└── sales_backup_2026-09-07.db
```

The backup system checks whether today's backup already exists before creating another one.

## Backup Cleanup

To prevent the backup folder from growing indefinitely, the system keeps the most recent five backups.

Older backups are automatically deleted.

This introduces an important real-world software engineering concept:

> Data should be backed up, but backups should also be managed.

## Report Generation

Daily reports can be generated automatically and saved as text files.

The application creates the `reports` directory when necessary and writes the report using UTF-8 encoding so that the Nigerian Naira symbol (`₦`) displays correctly.

## Project Structure

A typical project structure looks like:

```text
sales-management-system/
│
├── sales_management.py
├── sales.db
│
├── backup/
│   ├── sales_backup_YYYY-MM-DD.db
│   └── ...
│
└── reports/
    ├── sales_report_YYYY-MM-DD.txt
    └── ...
```

The exact Python filename may differ depending on how the project was saved.

## Concepts Learned

This project was built as a learning project and covered several important Python and programming concepts.

### Python

- Variables
- Functions
- Lists and dictionaries
- Conditional statements
- Loops
- User input
- Exception handling
- Input validation
- String formatting
- File handling
- Modules
- Date and time handling

### SQL

- `CREATE TABLE`
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`
- `WHERE`
- `LOWER()`
- Aggregate functions
- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`
- Parameterized queries

### SQLite

- Creating a database
- Connecting to SQLite
- Creating tables
- Executing SQL statements
- Fetching records
- Committing changes
- Closing database connections

### File Management

- Creating directories
- Writing reports to files
- Checking whether files exist
- Copying database files
- Removing old backup files

## Important Lessons

### 1. Always Fetch Query Results

A database cursor is not the same thing as the result of a query.

For example:

```python
cursor.execute("SELECT COUNT(*) FROM sales")
result = cursor.fetchone()
```

### 2. Use Parameterized Queries

Instead of directly inserting user input into SQL:

```python
cursor.execute(
    "SELECT * FROM sales WHERE customer = ?",
    (customer,)
)
```

This is safer and helps prevent SQL injection.

### 3. Validate User Input

The application validates values such as:

- Customer names
- Quantities
- Prices

This prevents invalid data from entering the database.

### 4. Handle Empty Database Results

Aggregate queries can return `None` when there are no records.

Using:

```python
total_revenue = result[0] or 0
```

ensures the program can safely format the result.

### 5. Calculate Derived Values

The total sale is calculated from:

```python
total = quantity * price
```

rather than asking the user to manually enter the total.

This reduces errors.

## Future Improvements

Possible next versions of the project could include:

- User authentication
- Product/inventory management
- Multiple users
- Customer database
- Stock management
- Monthly and yearly reports
- Sales charts
- CSV/Excel export
- PDF reports
- Profit and loss calculations
- Expenses tracking
- Dashboard interface
- Web interface
- REST API
- Cloud database
- AI-powered sales analysis
- Natural-language business assistant

## Learning Journey

The project evolved through several stages:

```text
Python List
    ↓
Dictionary-based Sales Records
    ↓
CRUD Operations
    ↓
Input Validation
    ↓
JSON Persistence
    ↓
SQLite Database
    ↓
Search & Edit
    ↓
Sales Reports
    ↓
Automated Backups
    ↓
Automated Reports
    ↓
Future: AI-Powered Sales Intelligence
```

## Goal

The ultimate goal is not simply to create a sales application, but to use the project as a practical way to learn software development.

The next major evolution is an **AI-Powered Sales Intelligence System** capable of analyzing sales data and providing useful business insights.

---

## Author

Built as a practical Python learning project.

**Technologies:** Python + SQLite + SQL

**Project:** Sales Management System
