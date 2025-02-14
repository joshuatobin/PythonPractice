import csv
from datetime import datetime

class Product():
    """
    """
    def __init__(self, id, product, quantity, price, date):
        self.id = id
        self.product = product
        self.quantity = int(quantity)
        self.price = float(price)
        self.date = datetime.strptime(date, '%Y-%m-%d')
        

def writeCSV(filename, data):
     with open(filename, "w", encoding="utf-8") as csv_file:
         csv_file.write(data)

def main():
    """
    1. Reads the CSV file and extracts relevant fields.
    2. Computes the following insights:
        - The total sales per product.
        - The top 3 best-selling products by revenue.
        - The total revenue generated for each month.
    """
    
    salesData="""TransactionID,Product,Quantity,Price,Date 
    101,Widget A,5,10.00,2024-01-15 
    102,Widget B,2,20.00,2024-01-17 
    103,Widget A,3,10.00,2024-02-01 
    104,Widget C,1,50.00,2024-02-10 
    105,Widget A,7,10.00,2024-02-15 
    106,Widget B,5,20.00,2024-03-05
    """

    fileName="salesdata.csv"
    writeCSV(fileName, salesData)

    products = {}

    with open('salesdata.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        header = next(csv_reader)
        
        for row in csv_reader:
            row = [x.strip() for x in row]
            if not any(row):
                continue
            
            prod = Product(id=row[0], product=row[1], quantity=int(row[2]), price=float(row[3]), date=row[4])

            # If the product doesn't exist, create an empty list
            # Otherwise append the products name, to a list within the dictionary. 
            if prod.product not in products:
                 products[prod.product] = []
            products[prod.product].append(prod)

        # The total sales per product.
        # Remember we need the price * quantity
        # Use the items() on dict
        for product_name, obj in products.items():
            total_revenue = sum(p.price * p.quantity for p in obj)
            print(f"Product: {product_name} | Total Revenue: {total_revenue}")
        
        # You could also use values
        for product in products.values():
            total_revenue = sum(p.price * p.quantity for p in product)
            print(f"Product: {product[0].product} | Total Revenue: {total_revenue}")
        
        
         # The top 3 best-selling products by revenue.
         
        best_selling = []
        for product_name, obj in products.items():
            total_revenue = sum(p.price * p.quantity for p in obj)
            
            best_selling.append((product_name, total_revenue))
        
        sorted_revenue = sorted(best_selling, key=lambda x: x[1], reverse=True)

        # Get the top 3 best-selling products by revenue
        top_three = sorted_revenue[:3]

        # Print the results
        print("Top 3 Best-Selling Products by Revenue:")
        for product_name, revenue in top_three:
            print(f"{product_name}: ${revenue:.2f}")
         
if __name__ == "__main__":
    main()
    