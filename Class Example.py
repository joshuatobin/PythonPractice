#!/usr/bin/env python3

"""
Example of a simple Python script with basic object-oriented design.

Usage:
    python boilerplate.py
"""

class Animal:
    """
    A base class that represents an animal.
    """

    def __init__(self, name: str):
        """
        Initializes an Animal with a name.
        
        :param name: The name of the animal
        """
        self.name = name

    def make_sound(self) -> str:
        """
        A placeholder method meant to be overridden by subclasses.
        
        :return: A string representing the animal's sound.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class Dog(Animal):
    """
    A Dog class that inherits from Animal.
    """

    def make_sound(self) -> str:
        """
        Returns the sound a dog makes.
        """
        return "Woof!"


class Cat(Animal):
    """
    A Cat class that inherits from Animal.
    """

    def make_sound(self) -> str:
        """
        Returns the sound a cat makes.
        """
        return "Meow!"


def main():
    """
    Main entry point of the program.
    """
    # Create instances of Dog and Cat
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Print their names and the sounds they make
    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")

    # Optionally, store the animals in a list for further operations
    animals = [dog, cat]
    for animal in animals:
        print(f"{animal.name} is an instance of {type(animal).__name__}")


if __name__ == "__main__":
    main()
