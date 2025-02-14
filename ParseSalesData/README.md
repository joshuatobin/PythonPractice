# Task

---

## Objective

Showcase your ability to parse and manipulate CSV data in Python. This task will reinforce your skills in data processing, aggregation, and structured problem-solving.

---

## Instructions

You have been given a CSV file containing sales transaction data. Your task is to write a Python script that:

1. Reads the CSV file and extracts relevant fields.
2. Computes the following insights:
   - The total sales per product.
   - The top 3 best-selling products by revenue.
   - The total revenue generated for each month.

---

## Sample CSV Data (`sales_data.csv`)
TransactionID,Product,Quantity,Price,Date 101,Widget A,5,10.00,2024-01-15 102,Widget B,2,20.00,2024-01-17 103,Widget A,3,10.00,2024-02-01 104,Widget C,1,50.00,2024-02-10 105,Widget A,7,10.00,2024-02-15 106,Widget B,5,20.00,2024-03-05


---

## Guidelines

- Use Python’s `csv` module to parse the file.
- Perform necessary type conversions (e.g., converting prices to `float` and dates to `datetime`).
- Use dictionaries or collections like `defaultdict` or `Counter` to efficiently track sales per product.
- Ensure your output is formatted in a readable manner.
- Sort the products by revenue when listing the top 3 best-selling products.

Try to solve this problem in under **30 minutes**.

---
