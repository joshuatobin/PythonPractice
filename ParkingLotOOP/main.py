
from enum import Enum 
import time


class ParkingSpotStatus(Enum):
    AVAILABLE = "available"    
    TAKEN = "taken"
    


class ParkingLot():
    """
    - Design a system to manage a parking lot.  
    - The parking lot should accommodate different types of vehicles (e.g., cars, motorcycles, trucks).  
    - The system should keep track of parking spots, vehicle assignments, and parking lot capacity. 
    """
    
    def __init__(self, total_spots):
        self.spots = [ParkingSpot() for _ in range(total_spots)]

    def __repr__(self):
        return f"ParkingLot with {len(self.spots)} spots: {self.spots}"

    def add(self, vehicle):
        """ Add vehicles from the parking lot.  
        """
        for spot in self.spots:
            if spot.is_available():
                spot.set_vehicle(vehicle)
                
                break

        print(f"{self.available_spots()} parking spots left")
                
    def remove(self):
        """ Remove vehicles from the parking lot. 
        
        # Could use list comprehension here too but not as straight forward
        s = [spot for spot in self.spots if not spot.is_available()]
        if s:
            s[0].remove_vehicle()
        """

        for spot in self.spots:
           if not spot.is_available():
               spot.remove_vehicle()
               break
        
        print(f"{self.available_spots()} parking spots left")
            
    def fee(self, rate=20.0):
        """ Add a fee based on the duration of stay.
        """
        for spot in self.spots:
            if not spot.is_available():
                # Shorthand for adding 10 hours to test
                # spot.start_time = spot.start_time - 36000
                spot.start_time -= 36000
                elapsed_time = time.time() - spot.start_time
                elapsed_hours = elapsed_time / 3600
                fee = rate * elapsed_hours
                
                print(f"Spot {spot}: Vehicle owes ${fee:.2f}")
            
    
    def available_spots(self):
        """Long form way to find available spots
        
        Using list comprehension:
        
        available_spots = [spot for spot in self.spots if spot.is_available()]
        return len(available_spots)
        """
        available = []
        for spot in self.spots:
            if spot.is_available():
                available.append(spot)

        return len(available)                
    
    
class ParkingSpot():
    """
    """
    def __init__(self):
        self.status = ParkingSpotStatus.AVAILABLE
        self.current_vehicle = None

    def __repr__(self):
        return f"<ParkingSpot: {self.status.value}>"
    
    def is_available(self):
        """
        Could also be written shorthand: 
        return self.current_vehicle is None
        """
        
        if self.current_vehicle is None:
            return True
        else:
            return False
        
    def set_vehicle(self, vehicle):
        self.start_time = time.time()
        self.current_vehicle = vehicle 
        self.status = ParkingSpotStatus.TAKEN
        
    def remove_vehicle(self):
        self.current_vehicle = None
        self.status = ParkingSpotStatus.AVAILABLE
    
class Vehicle():
    """
    """
    def __init__(self):
        pass

class Car(Vehicle):
    """
    """
    #def super().init()

class MotorCycle(Vehicle):
    """
    """
    #def super().init()

class Truck(Vehicle):
    """
    """
    #def super().init()
    
    
def main():
    # Instantiate a vehicle
    vehicle = Vehicle()

    # Define the total number of spots your Parklot can handle
    total_spots = 5

    # Instantiate the parking lot
    lot = ParkingLot(total_spots)

    # Add a vehicle to a spot in the lot! 
    lot.add(vehicle)   

    lot.fee()
    # Remove a vehicle from a spot in the lot! 
    lot.remove()   

if __name__ == "__main__":
    main()
