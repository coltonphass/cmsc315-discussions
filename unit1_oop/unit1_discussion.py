"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Animal:
    zoo_name = "Plumpton Park"
    total_animals = 0

    # maybe add type hinting so the input remains clear?
    def __init__(self, name, species, age, diet, health=100):
        self.name = name
        self.species = species
        self.age = age
        self._health = health
        self.diet = diet
        self.feeding_log = []
        Animal.total_animals += 1

    def make_sound(self):
        return "..."

    def feed(self, food):
        if food not in self.diet:
            raise ValueError(self.name + " can't eat " + str(food) + ". Allowed: " + str(self.diet))
            self.feeding_log.append(food)
            return self.name + " ate " + str(food) + "."


    def get_info(self):
        return (self.name + " the " + self.species + ", age " + str(self.age) +
                " | health: " + str(self._health) +
                " | fed: " + str(self.feeding_log) +
                " | zoo: " + self.zoo_name)
# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Penguin(Animal):
    pass


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    print("\nTODO: Create and test your child object")

    demonstrate_namespaces()
    demonstrate_copying()

    peter = Animal("Peter", "Dog", 5, ["Kibble", "Steak"])
    print(peter)

    print(peter.get_info())

    try:
        peter.feed("pizza")
    except ValueError as error:
        print("Feeding blocked: ", error)

    print("Total animals", Animal.total_animals)

if __name__ == "__main__":
    main()