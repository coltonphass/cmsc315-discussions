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
    habitat_name = "Igloo"

    def __init__(self, name, species, age, diet, swim_speed, is_molting):

        super().__init__(name, species, age, diet)

        self.swim_speed = swim_speed
        self.is_molting = is_molting

    def swim(self):
        return self.name, "swims at a swim speed of: ", self.swim_speed

    #@override
    def make_sound(self):
        return "squawk"

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

    waddles = Penguin("Waddles", "Penguin", 5, ["Fish"], 2.5, True)
    theodore = Penguin("Theodore", "Penguin", 7, ["Fish"], 3.5, False)

    print("Penguin Class habitat:", Penguin.habitat_name)
    print("Waddles habitat:", waddles.habitat_name)

    waddles.habitat_name = "Pool"

    waddles.favorite_keeper = "Colton"

    print("Waddles favorite keeper is:", waddles.favorite_keeper)

    try:
        print("Thedores favorite keeper is:", theodore.favorite_kepper)
    except AttributeError as error:
        print("Here we can see theodore does not have a favorite keeper:", error)

    #print(theodore.favorite_keeper) - Will throw attribute error, as it should.

    print(waddles.__dict__)
    print(theodore.__dict__)
    print(Penguin.__dict__)


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

    # create penguin and feed it once

    isaac = Penguin("Isaac", "Penguin", 10, ["Fish", "Shrimp"], 6.5, False)
    isaac.feed("Shrimp")

    # make a shallow and deep copy with store variable names
    shallow_copy = copy(isaac)
    deep_copy = deepcopy(isaac)

    print("Before changing the original:")
    print("  Original log:    ", isaac.feeding_log)
    print("  Shallow copy log:", shallow_copy.feeding_log)
    print("  Deep copy log:   ", deep_copy.feeding_log)

    isaac.feed("Fish")

    print("\nAfter feeding the original again:")
    print("  Original log:    ", isaac.feeding_log)
    print("  Shallow copy log:", shallow_copy.feeding_log)
    print("  Deep copy log:   ", deep_copy.feeding_log)

    print("\nShallow copy shares Isaac's list:", isaac.feeding_log is shallow_copy.feeding_log)
    print("Deep copy shares Isaac's list:   ", isaac.feeding_log is deep_copy.feeding_log)

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

    demonstrate_namespaces()
    demonstrate_copying()

    peter = Animal("Peter", "Dog", 5, ["Kibble", "Steak"])
    print(peter)
    peter.feed("Kibble")
    print(peter.get_info())

    try:
        peter.feed("pizza")
    except ValueError as error:
        print("Feeding blocked: ", error)

    print("Total animals", Animal.total_animals)


    waddles = Penguin("Waddles", "Penguin", 5, ["Fish"], 2.5, True)
    print(waddles)

    print(waddles.get_info())
    print(waddles.swim())

if __name__ == "__main__":
    main()