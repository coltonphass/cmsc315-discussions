# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation Summary

I built a mock zoo data entry program in Python to demonstrate basic OOP concepts. I chose a zoo because it maps naturally to inheritance: every animal shares some basic information, but different types of animals have their own details and behaviors.

### Class Design

**`Animal` (parent class)**
- Class variables: `zoo_name` and `total_animals`. These were shared by every animal. `total_animals` went up by one each time a new animal was created.
- Instance variables: `name`, `species`, `age`, `diet`, `_health`, and `feeding_log`. Each animal got its own copy of these.
- I put an underscore on `_health` to mark it as an internal attribute, which is how Python handles encapsulation.
- `feeding_log` started as a new empty list inside `__init__` so each animal had its own log instead of sharing one.
- Methods: `make_sound()` returned a generic sound, `feed()` checked food against the animal's diet and recorded it, and `get_info()` returned a readable summary of the animal.

**`Penguin` (child class)**
- Inherited from `Animal`.
- Added a new class variable, `habitat_name`, and two new instance variables, `swim_speed` and `is_molting`.
- Used `super().__init__()` so `Animal` set up its own variables. This kept me from retyping the parent's setup code.
- Added a new method, `swim()`.
- Overrode `make_sound()` to return "squawk." Because Python searches the object, then the child class, then the parent class, penguins found their own version first.

### Namespaces

I created two penguins, Waddles and Theodore, and the output showed:
- Reading `habitat_name` through the `Penguin` class and through Waddles both returned "Igloo," because Waddles did not have his own copy and Python found it on the class.
- I added `favorite_keeper` to only Waddles. Looking it up on Theodore raised an `AttributeError`, which I caught and printed.
- Printing each object's `__dict__` showed only that object's instance variables. Class variables like `habitat_name` and `zoo_name` were not there because they lived on the classes.
- The class namespaces showed that `Penguin` only held what it defined itself (`habitat_name`, `swim`, `make_sound`), while `zoo_name`, `feed`, and `get_info` lived on `Animal`.
- When I set `waddles.habitat_name = "Pool"`, it created a new instance variable on Waddles only. Theodore and the `Penguin` class still showed "Igloo." This is called shadowing.

### Shallow Vs. Deep Copy

I created a penguin named Isaac, fed him once, then made a shallow copy and a deep copy. After feeding Isaac again:
- Isaac's feeding log showed both foods.
- The shallow copy's log also showed both foods, because a shallow copy creates a new object but still shares the same inner lists as the original.
- The deep copy's log only showed the first food, because a deep copy makes its own copies of every nested list.

I used the `is` operator to prove it. The shallow copy shared Isaac's exact list (`True`) and the deep copy did not (`False`). I also noticed the final animal count did not include the copies, because `copy()` and `deepcopy()` build new objects without running `__init__`.

### Student Extension

My extension was the feeding system. None of the TODOs asked for it, but I added:
- A `diet` list for each animal that stored the foods it was allowed to eat.
- A `feeding_log` list that recorded what each animal actually ate.
- Validation in `feed()` that raised a `ValueError` when the food was not on the animal's diet.

I also wrote a small helper function, `show_class_namespace()`, that printed a class's own attributes while skipping Python's built-in `__dunder__` entries, so the class namespaces were readable in the terminal.

### Edge Cases

- **Invalid food:** Feeding Peter (a dog) pizza raised a `ValueError` because pizza was not on his diet. I caught it with `try/except`, so the program printed "Feeding blocked" with the allowed foods instead of crashing.
- **Missing attribute:** Looking up `favorite_keeper` on Theodore raised an `AttributeError` because only Waddles was given that attribute. I caught it and printed a message explaining why.

### Real-World Use

This design matches how zoo or veterinary record software could work. Every animal shares a base record (name, species, age, diet, health, feeding history), and each type of animal adds its own details. Validating food before logging it also helps keep records accurate, since a bad entry gets caught right away instead of quietly ending up in an animal's history.

### Challenges

I faced multiple challenges in this discussion. The first one was preparation. I was on vacation during this discussion and did not allow myself enough study time.

I was challenged by reassigning vs. mutating in the copy demo. At first I replaced Isaac's feeding log with a new list, which did not show the shallow copy's shared list at all. I had to append to the existing list instead.

Another thing that threw me off was `self.` vs. `Animal.` for the counter. It helped to frame it in OOP terms: each instance is its own separate animal object, so the `Animal` class as a whole needed to be responsible for storing the counter.

`swim()` also returned a tuple at first. It had been a while since I used Python, so string concatenation and converting values with `str()` needed a refresher.

I also had a typo where I looked up `favorite_kepper` instead of `favorite_keeper`. The test still raised an error, so it looked like it worked, but it was failing for the wrong reason. That taught me a test should only fail for the reason I am actually testing.

Overall, writing object-oriented code again was a challenge, and I found myself looking up a lot of syntax. Next time I want to plan more time for these discussions and work on them iteratively instead of doing it all in one or two days.

### How to Run

Right-click `unit1_discussion.py` in IntelliJ and select **Run**.

---
#### AI Attribution

I used Claude *(Opus 5.5)* throughout this assignment to break down the requirements, and explain concepts to me like namespaces and shallow vs. deep copying. I had it help me develop the `show_class_namespace()` helper since the terminal output was cluttered. All other code was written manually.