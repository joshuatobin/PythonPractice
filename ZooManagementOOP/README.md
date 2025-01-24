# Task

Design a Zoo Management System

---

## Objective

Reinforce object-oriented design fundamentals by implementing relationships, inheritance, and encapsulation. Focus on solving a real-world problem in an interview-style format while keeping the design scalable and clear.

---

## Instructions

1. **Problem Overview**:
   - Design a system to manage animals in a zoo.
   - Animals can belong to different categories, such as Mammals, Birds, or Reptiles.
   - Each animal has common attributes like name, species, and age, but some may have unique traits (e.g., birds can fly, mammals nurse their young).

2. **Key Features to Implement**:
   - **Classes**:
     - `Zoo`: Represents the entire zoo and contains a collection of animals.
     - `Animal` (base class): Represents a generic animal.
       - Subclasses: `Mammal`, `Bird`, `Reptile`.
   - **Methods**:
     - Add an animal to the zoo.
     - Remove an animal from the zoo by name.
     - List all animals, grouped by category (Mammals, Birds, Reptiles).

3. **Constraints**:
   - The zoo should enforce that only one animal with the same name can exist.
   - The system should support the addition of future categories without extensive rewrites.

4. **Stretch Goals**:
   - Add methods to handle specific behaviors, such as flying (`Bird`) or swimming (`Reptile`).
   - Implement a way to track when animals were added to the zoo and list them in order of arrival.

Take 30 minutes to implement as much as possible. Focus on creating clear, reusable classes and methods. Avoid overthinking edge cases but keep the design extensible for future changes.
