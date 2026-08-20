Inventory Management System

A command-line inventory management application developed in Python using object-oriented programming, JSON persistence, and CSV export.

Overview

This project is a modular inventory management system designed to manage products through a simple command-line interface.

It allows users to add, view, search, update, and delete products, while also providing data persistence through JSON files and inventory export to CSV format.

Features
Add new products
View all products
Search products by ID
Update product price and quantity
Delete products
Validate product information
Save inventory data to JSON
Load previously saved inventory
Export inventory to CSV
Command-line interface
Technologies
Python 3
Object-Oriented Programming (OOP)
Classes and Objects
JSON
CSV
Exception Handling
Python Modules
Project Structure
inventory-management-system/
│
├── main.py
├── product.py
├── inventory.py
├── inventory.json
├── inventory.csv
└── README.md
Main Files

main.py
Contains the command-line interface and controls the main program flow.

product.py
Contains the Product class and methods for managing individual products.

inventory.py
Contains the Inventory class and the main inventory management operations.

inventory.json
Stores inventory data so it can be loaded when the application starts.

inventory.csv
Contains an exported version of the inventory that can be opened with spreadsheet software such as Microsoft Excel.

How to Run
Requirements
Python 3 installed on your computer.
Installation

Clone the repository:

git clone https://github.com/jorgebueno-u/inventory-management-system.git

Move into the project directory:

cd inventory-management-system

Run the application:

python main.py
Usage

After starting the program, the following menu is displayed:

===== INVENTORY MANAGEMENT SYSTEM =====
1. Add product
2. View products
3. Search product
4. Update product
5. Delete product
6. Save inventory
7. Export inventory to CSV
8. Exit

The user can select an option by entering the corresponding number.

Data Persistence

The application uses JSON to store inventory information.

When the program starts, previously saved inventory data is automatically loaded from:

inventory.json

The inventory can also be exported to:

inventory.csv

This CSV file can be opened and analyzed using Excel or other spreadsheet applications.

Example

Example product:

ID: 1 | Name: Arduino Uno | Category: Electronics | Price: $25000.00 | Quantity: 10
Learning Outcomes

This project helped me practice and strengthen:

Object-oriented programming in Python
Classes, objects, and methods
Modular programming
File handling
JSON serialization and deserialization
CSV file generation
Input validation
Exception handling
Basic software organization
Future Improvements

Possible future improvements include:

Product categories and filters
Inventory statistics
Low-stock notifications
Graphical user interface
Database integration
Excel automation
Data analysis with Pandas
Author

Jorge Bueno

Mechatronics Engineering Student
Universidad Militar Nueva Granada

GitHub: jorgebueno-u
