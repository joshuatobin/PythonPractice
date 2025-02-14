# Task

Design an Online Shopping Cart System  

---

## Objective  

Reinforce object-oriented design principles by implementing relationships, encapsulation, and class interactions. Focus on designing reusable classes and methods to manage an online shopping experience efficiently.  

---

## Instructions  

1. **Problem Overview:**  
   Design a system to manage an online shopping cart. The system should:  
   - Allow users to add and remove products from a cart.  
   - Track total cost based on items in the cart.  
   - Support checkout functionality.  

2. **Key Features to Implement:**  
   - **Classes:**  
     - `ShoppingCart`: Manages items in the cart.  
     - `Product`: Represents an individual product with `name`, `price`, and `quantity`.  
     - `Order`: Represents a finalized purchase with total cost.  
   - **Methods:**  
     - `ShoppingCart`:  
       - Add a product to the cart.  
       - Remove a product from the cart.  
       - Calculate the total cost.  
     - `Order`:  
       - Store order details.  
       - Process checkout.  

3. **Constraints:**  
   - A product’s quantity in the cart cannot exceed available stock.  
   - The checkout process should ensure the cart is not empty before finalizing an order.  

4. **Stretch Goals:**  
   - Implement discount codes for purchases.  
   - Add support for different payment methods.  

Take 30 minutes to start implementing the solution. Focus on structuring your classes and ensuring proper cart management.  
