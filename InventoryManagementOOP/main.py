
class Inventory():
    """
    - Add a product to the inventory.  
    - Remove a product from the inventory.  
    - Search for products by name or category.  
    - Update stock levels.  
    """
    
    def __init__(self):
        self.inventory = []

    def add(self, product):
        self.inventory.append(product)
        return self.inventory

    def remove(self, product):
        # Here we're removing the product instance, not the name of the product
        p = [p for p in self.inventory if p == product]

        if p:
            self.inventory.remove(p[0])
    
    def search(self, name):
        if self.inventory:
            product = [p for p in self.inventory if p.name == name]
            return product[0]
        else:
            return None
    
    def update(self, name, quantity):
        p = self.search(name=name)
        
        if quantity == 0:
            return None
        
        if p and p.quantity >=1:
            p.quantity = quantity
        else:
            return None
    
    def all(self):
        return self.inventory

class Product():
    """
    Represents an individual product, including attributes like `name`, `category`, and `quantity`. 
    """
    
    def __init__(self, name, category, quantity):
        self.name = name
        self.category = category
        self.quantity = quantity 
    
    
    def __repr__(self):
        return f"Product: name:{self.name}, category:{self.category}, quantity:{self.quantity}"
    
class main():
    """
    Design an Inventory Management System  

    Reinforce object-oriented design by implementing relationships, encapsulation, and class interactions. Focus on designing reusable classes and methods that handle real-world inventory tracking.  
    """

if __name__ == "__main__":

    # Instantiate the inventory class    
    i = Inventory()

    # Instantiate a product instance
    p = Product(name="Widget", category="toy", quantity=1)
    
    # Add a product to the inventory
    inventory = i.add(p)

    # Search for a product within the inventory
    product = i.search(name="Widget")
    
    # Validate 
    print(i.all())
    
    i.update(name="Widget", quantity=10)
    print(i.all())

    # Remove a product from the inventory
    i.remove(p)

    print(i.all())

    main()
