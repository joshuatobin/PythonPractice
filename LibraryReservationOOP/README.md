# Task

Create a Library Reservation System

---

## Objective

Reinforce object-oriented design fundamentals by building a system that allows users to reserve books from a library. The focus is on implementing classes, relationships between objects, and encapsulating logic in a structured and modular way.

---

## Instructions

1. **Problem Overview:**  
   Design a system that allows users to:
   - Search for available books by title or author.  
   - Reserve a book.  
   - Cancel a reservation.

2. **Key Features to Implement:**  
   - **Classes:**  
     - `Library`: Represents the entire library and maintains a catalog of books.  
     - `Book`: Represents a single book in the catalog, including attributes like title, author, and availability status.  
     - `Reservation`: Represents a reservation made by a user for a specific book.  
   - **Methods:**  
     - Search books by title or author.  
     - Reserve a book if it’s available.  
     - Cancel a reservation by referencing the book title.

3. **Constraints:**  
   - The system should ensure that a book can only be reserved if it’s currently available.  
   - A user cannot reserve the same book multiple times.

4. **Hints:**  
   - Start by defining the `Library` and `Book` classes.  
   - Add a list to `Library` that holds `Book` instances.  
   - Create a method in `Library` to iterate through the catalog and return only available books.  
   - Implement the `Reservation` class so that each reservation is linked to a specific `Book`.

5. **Stretch Goals:**  
   - Add a user class and track which user made each reservation.  
   - Introduce a reservation time limit, automatically canceling reservations that expire.

Take 30 minutes to start implementing the solution. Focus on defining clear class boundaries and methods that logically belong to each class. Don't worry about handling every edge case—just ensure the core logic is clear and encapsulated.
