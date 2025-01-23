# Task
Design a simple ride-hailing system using object-oriented principles.

---

## Objective
- Practice creating classes and leveraging inheritance, composition, and polymorphism.  
- Implement functionality that simulates typical ride-hailing scenarios, emphasizing real-world constraints and behaviors.

---

## Instructions
1. **Create a `RideHailingApp` class** to manage drivers, riders, and ride requests. It should maintain lists (or collections) of available drivers and registered riders.  
2. **Define a `User` base class** with common attributes such as `user_id`, `name`, and `location`.  
   - **Create subclasses** `Driver` and `Rider` extending `User`.  
     - `Driver` might include attributes such as `vehicle_details` and a `status` indicating availability.  
     - `Rider` might have methods to request a ride and track ongoing rides.  
3. **Ride Management**:  
   - Implement a method in `RideHailingApp` to **request a ride**, which:  
     1. Finds the nearest available driver.  
     2. Updates driver status to “busy.”  
     3. Creates a `Ride` object with information such as pickup and destination.  
   - Implement a method to **complete a ride**, updating driver status to “available.”  
4. **Use Polymorphism**:  
   - Consider different types of **`Vehicle`** classes (`Car`, `Bike`, `Van`) that drivers can have, each with unique attributes (e.g., max passenger capacity).  
   - Ensure your ride assignment logic handles these differences appropriately (for instance, a `Bike` cannot carry multiple passengers).  
5. **Script Demonstration**:  
   - In a driver script, instantiate multiple drivers and riders.  
   - Demonstrate requesting rides, assigning drivers, and completing rides.

---

## Stretch Goal
- **Add a Rating System** so that after each ride, the rider can rate the driver, and the app calculates average ratings.

---

## Bonus
- **Implement Exception Handling** to cover scenarios like:  
  - No available drivers for a request.  
  - Invalid ride requests (e.g., missing location data).  
- **Ensure Extensibility** by designing the classes in a way that allows adding new ride types (e.g., pooled rides vs. direct rides) with minimal changes to existing code.

---

## Focus on
- Separation of Concerns (each class should have a clear responsibility).  
- Reusability (easily adapt or extend the system).  
- Clear naming and structure to reflect real-world objects and interactions.
