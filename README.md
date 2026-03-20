# Customer Order Management System

## Project Description
This project is a Python-based customer order management system developed to register customers, register products, create orders, consult registered orders, calculate daily income, and generate a final sales report.

## System Architecture
The system is organized into independent modules, each responsible for a specific functionality:

- `main.py`: Main menu and program execution flow
- `customers.py`: Customer registration
- `products.py`: Product registration
- `orders.py`: Order creation and order query
- `reports.py`: Daily income and final report generation

## Features
- Register customers
- Register products
- Create orders
- View registered orders
- Calculate daily income
- Generate final report

## Data Structures Used
This project uses only the following data structures:

- **Dictionaries**: Used to store customers and orders
- **Tuples**: Used to represent product information

Example product tuple:
```python
(product_id, product_name, unit_price)
