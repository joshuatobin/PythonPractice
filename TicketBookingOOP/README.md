# Task

Design a Ticket Booking System  

---

## Objective  

Reinforce object-oriented design principles by implementing relationships, encapsulation, and class interactions. Focus on designing reusable classes and methods to efficiently manage ticket reservations.  

---

## Instructions  

1. **Problem Overview:**  
   Design a system to manage ticket bookings. The system should:  
   - Allow users to book tickets for events.  
   - Keep track of available seats.  
   - Support cancellations and refunds.  

2. **Key Features to Implement:**  
   - **Classes:**  
     - `TicketBookingSystem`: Manages event listings and ticket reservations.  
     - `Event`: Represents an individual event with attributes like `name`, `date`, and `available_seats`.  
     - `User`: Represents a person making a reservation.  
     - `Reservation`: Tracks ticket purchases and cancellations.  
   - **Methods:**  
     - `TicketBookingSystem`:  
       - List available events.  
       - Book a ticket for a user.  
       - Cancel a reservation and free up seats.  
     - `Reservation`:  
       - Store reservation details.  
       - Process refunds if applicable.  

3. **Constraints:**  
   - A user cannot book more tickets than available seats.  
   - Cancellations should update seat availability.  

4. **Stretch Goals:**  
   - Implement different seat categories (e.g., VIP, General, Balcony).  
   - Support dynamic pricing based on demand.  

Take 30 minutes to start implementing the solution. Focus on structuring your classes and ensuring proper reservation tracking.  
