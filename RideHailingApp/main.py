
from enum import Enum

class DriverStatus(Enum):
    AVAILABLE = "available"    
    BUSY = "busy"
    OFFLINE = "offline"

class RideHailingApp():
    """
    Class to manage drivers, riders, and ride requests. 
    It should maintain lists (or collections) of available drivers and registered riders
    """

    def __init__(self, available_drivers, registered_riders, requests):
        self.available_drivers = available_drivers
        self.registered_riders = registered_riders
        self.requests = requests
    
    def request_ride(self, rider):
        """
        - Implement a method in `RideHailingApp` to **request a ride**, which:  
            1. Finds the nearest available driver.  
            2. Updates driver status to “busy.”  
            3. Creates a `Ride` object with information such as pickup and destination.  
        
        - Implement a method to **complete a ride**, updating driver status to “available.” 
        """
                
        # Filter available drivers (those whose status == DriverStatus.AVAILABLE).
        available = [driver for driver in self.available_drivers if driver.status == DriverStatus.AVAILABLE]
        if not available:
            print(f"No drivers available for {rider.name}.")
            return None
        else:
            print(available)
        
        # Find the nearest by comparing each driver’s location to linda.location.
        
        # Update the chosen driver’s status to busy.
        
        # Create and store some representation of the ride (e.g., a dictionary or a Ride object).


    def complete_ride(self):
        """
        - Implement a method to **complete a ride**, updating driver status to “available.” 
        """
    
    def compute_distance(loc1, loc2):
        """ 
        Euclidean distance method
        """
        x1, y1 = loc1
        x2, y2 = loc2

        return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

class User():
    """
    Define a `User` base class** with common attributes such as `user_id`, `name`, and `location`. 
    """

    def __init__(self, user_id, name, location):
        self.user_id = user_id
        self.name = name
        self.location = location

class Driver(User):
    """
     - `Driver` might include attributes such as `vehicle_details` and a `status` indicating availability.  
    """
    def __init__(self, user_id, name, location, vehicle_details, status):
        super().__init__(user_id, name, location)
        self.vehicle_details = vehicle_details
        self.status = status
        
    def go_offline(self):
        self.status = DriverStatus.OFFLINE
    
    def go_online(self):
        self.status = DriverStatus.AVAILABLE
    
    def mark_busy(self):
        self.status = DriverStatus.BUSY
        
    def __repr__(self):
        """
        __repr__ object is for "representation". IE pretty print the object when called. 
        """
        
        return f"Driver(user_id={self.user_id}, name='{self.name}', vehicle='{self.vehicle_details}', status={self.status.value})"


class Rider(User):
    """
     - `Rider` might have methods to request a ride and track ongoing rides.
    """

    def __init__(self, user_id, name, location, ride, tracking):
        super().__init__(user_id, name, location)
        self.ride = ride
        self.tracking = tracking

    def request_ride(self):
       pass

    def track_ride(self):
       pass

def main():
    """
    Sample program for a ride share app. Define drivers and riders
    """

    # Drivers
    alice = Driver(
        user_id=1,
        name="Alice",
        location=(10, 5),
        vehicle_details="Toyota Camry",
        status=DriverStatus.AVAILABLE
    )
    
    bob = Driver(
        user_id=2,
        name="Bob",
        location=(3, 8),
        vehicle_details="Honda Civic",
        status=DriverStatus.OFFLINE
    )
    
    # Riders
    david = Rider(
        user_id=101,
        name = "david",
        location =(12,5),
        ride = None,
        tracking = None
    )
    
    linda = Rider(
        user_id=101,
        name = "linda",
        location =(5,5),
        ride = None,
        tracking = None
    )

    drivers = [alice, bob]
    riders = [david, linda]

    ride = RideHailingApp(
        available_drivers=drivers, 
        registered_riders=riders,
        requests=[]
    )
    
    ride.request_ride(linda)

if __name__ == "__main__":
    main()
