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
    # Class variables: defined on the class, ONE copy is shared by every animal
    zoo_name = "Plumpton Park"
    total_animals = 0

    def __init__(self, name, species, age, diet, health=100):
        # Instance variables: each animal gets its own copy
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet            # List of foods animal is allowed to eat
        self._health = health       # underscore = internal attribute (encapsulation)
        self.feeding_log = []       # fresh empty list for each animal (never shared)
        Animal.total_animals += 1   # Update counter through class name, since if it was instance it wouldnt store properly

    def make_sound(self):
        # Generic sound; child override to make own sound
        return "..."

    def feed(self, food):
        # Guard clause: reject any food not in diet.
        if food not in self.diet:
            raise ValueError(self.name + " can't eat " + str(food) + ". Allowed: " + str(self.diet))
        # Valid food: record in feeding log
        self.feeding_log.append(food)
        return self.name + " ate " + str(food) + "."


    def get_info(self):
        # Returns one readable summary string
        # self.zoo_name works because python first checks the object, then the class
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
    # New class variable shared by all penguins
    habitat_name = "Igloo"

    def __init__(self, name, species, age, diet, swim_speed, is_molting):
        # Super runs Animals init so we can set up those variables (DRY)
        super().__init__(name, species, age, diet)
        # New instance variables only penguins have
        self.swim_speed = swim_speed
        self.is_molting = is_molting

    def swim(self):
        # New method: reads data stored on self, no need parameters
        return self.name + " swims at a swim speed of: " + str(self.swim_speed) + "MPH."

    def make_sound(self):
        # Override: same method name Python searches obj -> Penguin -> Animal so penguin is found first.
        return "squawk"

# HELPER FUNCTION FOR DICT DISPLAY:
def show_class_namespace(cls):
    # Helper for TODO 3: prints a class's own attributes.
    # Python's built-in "__dunder__" entries (like __module__, __init__) are skipped
    # to keep the output readable.
    names = []
    for key in cls.__dict__:
        if not key.startswith("__"):
            names.append(key)
    print(" ", cls.__name__, "namespace:", names)


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

    # Two penguin objects: each gets its own instance namespace
    waddles = Penguin("Waddles", "Pygoscelis antarcticus", 5, ["Fish"], 2.5, True)
    theodore = Penguin("Theodore", "Eudyptes chrysocome", 7, ["Fish"], 3.5, False)

    # Class variable read through the class and through an object.
    # Waddles has no habitat_name of his own, so Python finds it on the Penguin class.
    print("Penguin Class habitat:", Penguin.habitat_name)
    print("Waddles habitat:", waddles.habitat_name)

    # Add an attribute to ONLY Waddles, after he was created
    waddles.favorite_keeper = "Colton"
    print("Waddles favorite keeper is:", waddles.favorite_keeper)

    # Theodore never got this attribute, so looking it up raises an AttributeError
    try:
        print("Thedore favorite keeper is:", theodore.favorite_kepper)
    except AttributeError as error:
        print("Here we can see theodore does not have a favorite keeper:", error)

    print("\nWaddles' namespace:", waddles.__dict__)
    print("Theodore's namespace:", theodore.__dict__)

    # Class namespaces: Penguin only holds what it defines itself.
    # zoo_name, feed, and get_info live on Animal, which Python searches next.
    print("\nClass namespaces:")
    show_class_namespace(Penguin)
    show_class_namespace(Animal)

    # Shadowing: assigning through an object creates a NEW instance variable.
    # The class variable is unchanged, so Theodore and the class still see "Igloo".
    waddles.habitat_name = "Pool"
    print("\nAfter setting waddles.habitat_name = 'Pool':")
    print("  Waddles' habitat:", waddles.habitat_name)
    print("  Theodore's habitat:", theodore.habitat_name)
    print("  Penguin class habitat:", Penguin.habitat_name)
    print("  habitat_name now in Waddles' namespace:", "habitat_name" in waddles.__dict__)


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

    # Isaac contains nested mutable data: his diet and feeding_log lists.
    # Feed him once so his feeding_log has an entry before copying.
    isaac = Penguin("Isaac", "Eudyptes robustus", 10, ["Fish", "Shrimp"], 6.5, False)
    isaac.feed("Shrimp")

    # Shallow copy: a NEW Penguin object, but its lists are the SAME list
    # objects as Isaac's. Only references to the nested data are copied.
    shallow_copy = copy(isaac)
    # Deep copy: a NEW Penguin object with its OWN copies of every nested list.
    deep_copy = deepcopy(isaac)

    # Before any change, all three look identical
    print("Before changing the original:")
    print("  Original log:    ", isaac.feeding_log)
    print("  Shallow copy log:", shallow_copy.feeding_log)
    print("  Deep copy log:   ", deep_copy.feeding_log)

    # MUTATE the original's nested list: feed() appends to the existing list.
    # (Reassigning with isaac.feeding_log = [...] would NOT show the effect,
    # because it would point Isaac at a new list instead of changing the shared one.)
    isaac.feed("Fish")

    print("\nAfter feeding the original again:")
    print("  Original log:    ", isaac.feeding_log)
    print("  Shallow copy log:", shallow_copy.feeding_log)
    print("  Deep copy log:   ", deep_copy.feeding_log)

    # Proof: 'is' checks whether two names point to the exact same object in memory
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

    # Parent class object
    peter = Animal("Peter", "Dog", 5, ["Kibble", "Steak"])
    # Child class object
    waddles = Penguin("Waddles", "Pygoscelis papua", 5, ["Fish"], 2.5, True)

    print("\n--- Parent and child objects ---")
    # __str__ lets print() show a readable summary
    print("Peter:", peter.get_info())
    # get_info() is only defined in Animal; Waddles inherits it
    print("Waddles (inherited get_info):", waddles.get_info())

    print("\n--- Inherited and new methods ---")
    print("Peter eats (Animal method):", peter.feed("Kibble"))
    print("Waddles eats (inherited feed):", waddles.feed("Fish"))
    print("Waddles swims (Penguin-only method):", waddles.swim())

    print("\n--- Method override ---")
    print("Peter's make_sound (Animal version):", peter.make_sound())
    print("Waddles' make_sound (Penguin override):", waddles.make_sound())

    print("\n--- Edge case: invalid food ---")
    # feed() raises ValueError for food that is not on the diet.
    # Catching it here prints a friendly message instead of crashing.
    try:
        peter.feed("Pizza")
    except ValueError as error:
        print("Feeding blocked:", error)

    print("\nTotal animals created so far:", Animal.total_animals)

    demonstrate_namespaces()
    demonstrate_copying()

    # Copies are not counted: copy() and deepcopy() build objects without running __init__
    print("\nFinal animal count:", Animal.total_animals)


if __name__ == "__main__":
    main()