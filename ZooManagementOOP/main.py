
class Zoo():
    """
    `Zoo`: Represents the entire zoo and contains a collection of animals.
    """
    def __init__(self, name: str):
        # The zoo is a collection of animals. Initialize a list to "collect" all of the animals
        self.animals = []
        self.name = name 
    
        def __repr__(self):
            return(f"Zoo={self.name}")

    def add(self, species):
        """
        The add() method here would add an animal to the zoo’s internal list.
        """
        
        # NOTE: This works because Python is dynamically typed and does not enforce a specific type for the parameter species in your add() method
        # Python doesn’t care that the parameter is named species; it just treats species as whatever you pass in, whether that’s a Mammal, Animal, or any other object.
        self.animals.append(species)

    def remove(self, name):
        """
        The remove() method would remove an animal by some unique identifier (like name or species).
        """

        print(f'Removing the animal called: {name}')

        # Remember this overrides the list so there no need to call remove from the list
        self.animals = [animal for animal in self.animals if animal.name != name ]

        # Note: A for loop or list comprehension in Python doesn’t raise an exception if an element isn’t found. It just returns a new list so there is no need 
        # to wrap in try/except logic

    def all(self):
        """
        List all animals, grouped by category (Mammals, Birds, Reptiles).
        """
        for animal in self.animals:
            if isinstance(animal, Mammal):
                print(f"Mammals: {animal}")
            elif isinstance(animal, Bird):
                print(f"Birds: {animal}")
            elif isinstance(animal, Reptile):
                print(f"Reptile: {animal}")
            else:
                print("ERROR not found")
            

class Animal():
    """
    `Animal` (base class): Represents a generic animal.
    
    Remember: Animal class is more about defining the attributes and behaviors of an individual animal, nothing todo with the zoo it belongs in. 
    """
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def __repr__(self):
        return(f"Animal={self.species}-name={self.name}-age={self.age}")

    def speak(self):
        """
        """
        pass
    
class Mammal(Animal):
    """
    """
    def __init__(self, name, species, age):
        super().__init__(name, species, age)
    
class Bird(Animal):
    """
    """
    def __init__(self, name, species, age):
        super().__init__(name, species, age)
    

class Reptile(Animal):
    """
    """
    def __init__(self, name, species, age):
        super().__init__(name, species, age)
    

def main():
    """
    Design a Zoo Management System
    """
    # First instantiate the Zoo
    zoo = Zoo("The Bronx Zoo")
    
    # Next instantiate an animal to be able to add them to the zoo
    lion = Mammal(name="lion", species="lion", age=5)

    # Add an instance of the lion from the zoo
    zoo.add(lion)
    
    # Remove the lion but by using the species itself, not the instance class. 
    zoo.remove(lion.name)

    lion = Mammal(name="lion", species="lion", age=5)
    bird = Bird(name="bird", species="bird", age=6)
    gator = Reptile(name="gator", species="gator", age=7)

    # Add all animals 
    zoo.add(lion)
    zoo.add(bird)
    zoo.add(gator)

    zoo.all()
    
    zoo.remove('foo')
    
if __name__ == "__main__":
    main()
    
    