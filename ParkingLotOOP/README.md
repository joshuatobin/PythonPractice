# Task  
Design a Parking Lot Management System  

---

## Objective  
To practice object-oriented design principles, including class design, relationships, inheritance, and encapsulation, in a problem-solving context that simulates a real-world scenario.  

---

## Instructions  

**Problem Overview:**  
- Design a system to manage a parking lot.  
- The parking lot should accommodate different types of vehicles (e.g., cars, motorcycles, trucks).  
- The system should keep track of parking spots, vehicle assignments, and parking lot capacity.  

**Key Features to Implement:**  
- **Classes:**  
  - `ParkingLot`: Represents the entire parking lot.  
  - `ParkingSpot`: Represents individual parking spots.  
  - `Vehicle` (base class): Represents a generic vehicle.  
    - Subclasses: `Car`, `Motorcycle`, `Truck`.  
- **Methods:**  
  - Add/remove vehicles from the parking lot.  
  - Check if a parking spot is available for a specific vehicle type.  
  - Calculate parking fees based on the duration of the stay.  

**Constraints:**  
- Each parking spot can only fit one vehicle.  
- A motorcycle can park in any spot, while trucks require larger designated spots.  
- Cars can only park in regular or large spots.  

**Hints:**  
- Use inheritance for vehicle types.  
- Encapsulate parking spot availability logic within the `ParkingSpot` class.  
- Use a dictionary or list in the `ParkingLot` class to manage parking spots.  

**Stretch Goals:**  
- Implement an interface or abstract class for calculating parking fees.  
- Add functionality for reserving parking spots in advance.  

Take 1 hour to try implementing the solution. Focus on creating clear, reusable classes and methods.  
