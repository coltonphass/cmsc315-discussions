"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.

STUDENT NOTES:
My scenario is ONE PIECE themed: Sanji's DINNER LINE on the Thousand Sunny.
The Straw Hats line up for food, and the list keeps track of who's next.
  - Sanji always serves the ladies first   -> insert at the FRONT
  - Luffy sneaks into the middle of the line -> insert in the MIDDLE
  - Late crew members join the back          -> insert at the END
  - People get served, wander off, or fall asleep (Zoro) -> deletions
  - Sanji checks where someone is in line    -> search

It works just like a real restaurant waitlist app.

A Python list is an ARRAY-BASED list. Its items sit next to each other
in memory, which is why:
  - reading by index is fast:  O(1)
  - adding/removing at the END is fast: O(1)
  - adding/removing at the FRONT or MIDDLE is slower: O(n),
    because every item after that spot has to shift over by one.
"""

import time


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # If the index is too small, use the front of the line.
    if index < 0:
        index = 0

    # If the index is too big, use the back of the line.
    if index > len(lst):
        index = len(lst)

    # insert() puts the crew member at the index. Everyone who was at that
    # index or after it moves one spot back to make room.
    #
    # Speed depends on WHERE we insert:
    #   - front (index 0): everyone moves back -> slow, O(n)
    #   - middle:          about half move     -> O(n)
    #   - end:             nobody moves        -> fast, O(1)
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check that the index is valid BEFORE removing anything.
    # Without this check, lst.pop(99) on a short line would cause an
    # IndexError and crash the program. One bad request shouldn't
    # sink the whole ship.
    #
    # I also block negative numbers. Python allows -1 to mean "last item,"
    # but in a dinner line a negative spot is probably a mistake.
    if index < 0:
        return None
    if index >= len(lst):
        return None

    # pop() removes the crew member and gives them back to us.
    # Everyone after them moves up one spot to fill the gap.
    #   - remove from the end:   nobody moves   -> fast, O(1)
    #   - remove from the front: everyone moves -> slow, O(n)
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a LINEAR search. The line isn't in alphabetical order, so the
    # person could be anywhere. Sanji has to check each spot one at a time,
    # starting at the front (index 0).
    #   - Best case: they're first in line -> 1 check
    #   - Worst case: they're last or not in line -> checks everyone, O(n)
    for i in range(len(lst)):
        if lst[i] == value:
            return i   # found them, so stop looking

    # The loop checked everyone and didn't find them.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("=== Sanji's Dinner Line on the Thousand Sunny ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Step 1: Three crew members are already waiting for dinner.
    # Index 0 is the front of the line (next to get food).
    dinner_line = ["Usopp", "Zoro", "Franky"]
    print("Original dinner line:", dinner_line)

    # Step 2: Insert at the BEGINNING (index 0).
    # Sanji always serves the ladies first, so Nami goes to the front.
    # Usopp, Zoro, and Franky all move back one spot.
    insert_at(dinner_line, 0, "Nami")
    print("Sanji puts Nami at the front:", dinner_line)

    # Step 3: Insert in the MIDDLE.
    # Luffy can't wait and sneaks into the middle of the line.
    # len(dinner_line) is 4, and 4 // 2 is 2, so the middle is index 2.
    # (// divides and drops the decimal.)
    middle = len(dinner_line) // 2
    insert_at(dinner_line, middle, "Luffy")
    print("Luffy sneaks into the middle:", dinner_line)

    # Step 4: Insert at the END.
    # Brook shows up late and joins the back. Nobody has to move.
    insert_at(dinner_line, len(dinner_line), "Brook")
    print("Brook joins at the end:", dinner_line)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete from the BEGINNING: Nami gets her food first.
    # Everyone left in line moves up one spot.
    removed = delete_at(dinner_line, 0)
    print("Served first:", removed)
    print("Line now:", dinner_line)

    # Delete from the MIDDLE: Zoro falls asleep and drops out of line.
    middle = len(dinner_line) // 2
    removed = delete_at(dinner_line, middle)
    print("Fell asleep and left the line:", removed)
    print("Line now:", dinner_line)

    # Delete from the END: Brook wanders off to play his violin.
    # The last index is always len - 1.
    last_index = len(dinner_line) - 1
    removed = delete_at(dinner_line, last_index)
    print("Wandered off to play music:", removed)
    print("Line now:", dinner_line)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a crew member who IS in line.
    position = search_value(dinner_line, "Franky")
    print("Searching for Franky... index:", position)
    if position != -1:
        # Add 1 because people count from 1, not 0.
        print("Franky is number", position + 1, "in line.")

    # Search for someone who is NOT in line.
    # The loop checks every person before returning -1.
    position = search_value(dinner_line, "Buggy")
    print("Searching for Buggy... index:", position)
    if position == -1:
        print("Buggy is not on the Thousand Sunny. No food for him.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Delete with an index that is too big.
    # There is no spot 50 in a line of 3. delete_at() returns None
    # instead of crashing.
    result = delete_at(dinner_line, 50)
    print("1) Serve spot 50:", result)
    print("   Line is unchanged:", dinner_line)

    # Edge case 2: Delete with a negative index.
    # My function blocks negative numbers on purpose.
    result = delete_at(dinner_line, -1)
    print("2) Serve spot -1:", result)

    # Edge case 3: Delete from an EMPTY line.
    # Before the dinner bell rings, nobody is in line, so every
    # index is invalid.
    empty_line = []
    result = delete_at(empty_line, 0)
    print("3) Serve from empty line:", result)

    # Edge case 4: Search an EMPTY line.
    # The loop never runs, so the function returns -1.
    result = search_value(empty_line, "Luffy")
    print("4) Search empty line for Luffy:", result)

    # Edge case 5: Insert into an EMPTY line.
    # Index 0 is both the front and the back, so this works.
    insert_at(empty_line, 0, "Chopper")
    print("5) Chopper is first after the dinner bell:", empty_line)

    # Edge case 6: Insert with an index that is too big.
    # insert_at() changes 99 to the back of the line.
    insert_at(empty_line, 99, "Robin")
    print("6) Robin added at spot 99:", empty_line)

    # Edge case 7: Duplicate names.
    # Luffy got back in line for seconds, so he's in the list twice.
    # search_value() only finds the FIRST Luffy. A real app would give
    # each person in line a unique ticket number to tell them apart.
    seconds_line = ["Luffy", "Usopp", "Luffy"]
    result = search_value(seconds_line, "Luffy")
    print("7) Luffy is in line twice:", seconds_line)
    print("   Search finds index", result, "(first match only)")

    # ===============================
    # STUDENT EXTENSION: PERFORMANCE
    # ===============================
    # What if the line had 100,000 people (like a Marine base)?
    # I time 1000 inserts at the front vs. 1000 at the end.

    print("\n=== PERFORMANCE CHECK ===")

    # Insert at the FRONT 1000 times.
    big_line = list(range(100000))
    start = time.time()
    for i in range(1000):
        big_line.insert(0, i)
    front_time = time.time() - start

    # Insert at the END 1000 times.
    big_line = list(range(100000))
    start = time.time()
    for i in range(1000):
        big_line.append(i)
    end_time = time.time() - start

    print("Front inserts took:", round(front_time * 1000, 2), "ms")
    print("End inserts took:  ", round(end_time * 1000, 2), "ms")
    print("Front is slower because everyone in line has to move back each time.")


if __name__ == "__main__":
    main()