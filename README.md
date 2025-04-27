# BGU Mart Management System 🛒

A Python-based supermarket management system designed to track inventory, employees, suppliers, and activities (sales and deliveries) using a SQLite database.

## 📚 Project Overview

This system provides:
- **Employee Management**: Names, salaries, assigned branches.
- **Supplier Management**: Contact information.
- **Inventory Management**: Product stock and prices.
- **Activity Management**: Tracking sales and deliveries by date.

Key features:
- Full SQLite database design.
- Multiple Python modules handling different operations.
- Automated reports for employees, activities, and inventory status.

## 🚀 Technologies Used
- Python 3.9+
- SQLite3 (Embedded Database)
- SQL Queries (SELECT, JOIN, INSERT, UPDATE)

## 🛠️ How to Build and Run

### Initiate the Database
```bash
python3 src/initiate.py config.txt
```
Where config.txt contains the initial data for employees, suppliers, products, and branches.

# Perform Actions (Sales/Deliveries)
```bash
python3 src/action.py actions.txt
```
Where actions.txt contains sales and deliveries.

# Print the Database State
python3 src/printdb.py

# 🧠 Key Features
- Automated database setup from configuration files.
- Full transaction processing for product sales and restocks.
- Employee and activity detailed reports.
- Ordered outputs according to requirements.

# ✨ Skills Demonstrated
- Database Schema Design
- SQL Query Writing and Optimization
- File Parsing and Processing
- Modular Python Programming
