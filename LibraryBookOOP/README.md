# Task

Design a basic library management system using object-oriented principles.

## Objective

- Practice creating and using classes, inheritance, and polymorphism.
- Implement functionality that mimics real-world systems to enhance problem-solving skills.

## Instructions

1. **Create a `Library` class**:
   - Attributes: a list of books, library name, and location.

2. **Define a `Book` class**:
   - Attributes: title, author, and availability status.

3. **Add methods to the `Library` class**:
   - Adding a new book.
   - Checking out a book (change its status to unavailable).
   - Returning a book (change its status to available).

4. **Use inheritance**:
   - Create subclasses for specialized book types, such as `EBook` and `PrintedBook`.
   - Add unique attributes (e.g., file format for `EBook`, physical condition for `PrintedBook`).

5. **Demonstrate functionality**:
   - Write a script to show how books can be added, checked out, and returned.

## Stretch Goal

- Add a `Member` class to represent library members.
- Include methods for borrowing and returning books while adhering to borrowing limits.

## Bonus

- Implement exception handling:
  - Attempting to check out an unavailable book.
  - Returning a book not in the system.

**Focus**:  
- Clear, reusable code.  
- Adherence to SOLID principles.
