# Task

Design an Inventory Management System  

---

## Objective  

Reinforce object-oriented design by implementing relationships, encapsulation, and class interactions. Focus on designing reusable classes and methods that handle real-world inventory tracking.  

---

## Instructions  

1. **Problem Overview:**  
   Design a system to manage an inventory of products. The system should:  
   - Keep track of available products and their stock levels.  
   - Allow adding and removing stock.  
   - Search for products by name or category.  

2. **Key Features to Implement:**  
   - **Classes:**  
     - `Inventory`: Manages a collection of products and tracks stock levels.  
     - `Product`: Represents an individual product, including attributes like `name`, `category`, and `quantity`.  
   - **Methods:**  
     - `Inventory`:  
       - Add a product to the inventory.  
       - Remove a product from the inventory.  
       - Search for products by name or category.  
       - Update stock levels.  
     - `Product`:  
       - Store details like `name`, `category`, and `quantity`.  

3. **Constraints:**  
   - A product can only be removed if it exists in the inventory.  
   - Stock levels should not drop below zero.  

4. **Stretch Goals:**  
   - Implement low-stock alerts when quantity falls below a threshold.  
   - Support bulk operations to add or remove multiple products at once.  

Take 30 minutes to start implementing the solution. Focus on designing clear class structures and methods, ensuring that each class has a well-defined responsibility.  
