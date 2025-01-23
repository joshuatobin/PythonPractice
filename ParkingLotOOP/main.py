

from enum import Enum 

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
            if spot.status == ParkingSpotStatus.AVAILABLE:
                spot.set_taken()
                print("Found an available spot.")
                break
                
        print(f"{len(self.spots)} parking spots left")
                
    def remove():
        """ Remove vehicles from the parking lot. 
        """
        pass
    
    def fee():
        """ Add a fee based on the duration of stay.
        """
        pass
    
class ParkingSpot():
    """
    """
    def __init__(self):
        self.status = ParkingSpotStatus.AVAILABLE

    def __repr__(self):
        return f"<ParkingSpot: {self.status.value}>"
    
    def is_available(self):
        self.status = ParkingSpotStatus.AVAILABLE
        
    def set_taken(self):
        self.status = ParkingSpotStatus.TAKEN
    
class Vehicle():
    """
    """
    
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
    total_spots = 5
    lot = ParkingLot(total_spots)
    
    lot.add(vehicle="foo")
if __name__ == "__main__":
    main()
