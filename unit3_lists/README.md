# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

---

## What I Implemented

I themed the assignment around **One Piece**: Sanji's dinner line on the Thousand Sunny. The Straw Hats lined up for food, and the list tracked who was next. Index 0 was the front of the line. Each list operation matched something that happened in the line:

| What happened | List operation | Position | Cost |
|---|---|---|---|
| Sanji served the ladies first, so Nami went to the front | `insert_at(lst, 0, ...)` | Beginning | O(n) |
| Luffy snuck into the middle of the line | `insert_at(lst, middle, ...)` | Middle | O(n) |
| Brook showed up late and joined the back | `insert_at(lst, len(lst), ...)` | End | O(1) |
| Nami got served first | `delete_at(lst, 0)` | Beginning | O(n) |
| Zoro fell asleep and dropped out of line | `delete_at(lst, middle)` | Middle | O(n) |
| Brook wandered off to play his violin | `delete_at(lst, len(lst) - 1)` | End | O(1) |
| Sanji checked where someone was in line | `search_value(lst, name)` | Anywhere | O(n) |

### `insert_at(lst, index, value)`
I used `list.insert()` to place the crew member. Before inserting, I used two `if` checks: an index below 0 became 0 (the front), and an index past the end became `len(lst)` (the back), so a bad position never crashed the program. I commented on how everyone at or after the index moved back one spot, which was why inserting at the front cost O(n) and adding to the end cost O(1).

### `delete_at(lst, index)`
I checked the index first and returned `None` if it was out of range, then used `list.pop(index)` to remove and return the crew member. I blocked negative indexes on purpose. Python normally treats `-1` as "the last item," but in a dinner line a negative spot was more likely a mistake, and removing the wrong person would have been worse than doing nothing.

### `search_value(lst, value)`
I wrote the linear search as a `for` loop instead of calling `lst.index()`, so the step-by-step scan was easy to see. The line wasn't sorted, so the function checked index 0, then 1, then 2, and so on, returning the first match or `-1` if it reached the end. `lst.index()` would have crashed with a `ValueError` on a missing name, which the assignment didn't want.

### Student extension: performance check
I added a timing test using `time.time()` and two `for` loops: one inserted 1,000 people at the front of a 100,000-person line (about the size of a Marine base), and the other added 1,000 people to the end. On my run, the front inserts took about **22 ms** and the end inserts took less than **0.1 ms**.

## Edge Cases Tested

| # | Case | What happened | Why |
|---|---|---|---|
| 1 | Serve spot 50 in a line of 3 | Returned `None`, line unchanged | The index check caught it before `pop()` could crash |
| 2 | Serve spot -1 | Returned `None` | I blocked negative indexes on purpose |
| 3 | Serve from an empty line (before the dinner bell) | Returned `None` | The length was 0, so every index was invalid |
| 4 | Search an empty line for Luffy | Returned `-1` | The loop ran zero times and went straight to `return -1` |
| 5 | Add Chopper to an empty line | Worked | Index 0 was both the front and the back |
| 6 | Add Robin at spot 99 | Added to the end | The `if` check changed 99 to `len(lst)` |
| 7 | Luffy got back in line for seconds (in the list twice) | Returned the first Luffy only | A real limitation; a real app would give each person a unique ticket number |

## Sample Output (abridged)

```
=== Sanji's Dinner Line on the Thousand Sunny ===

=== INSERTION TESTS ===
Original dinner line: ['Usopp', 'Zoro', 'Franky']
Sanji puts Nami at the front: ['Nami', 'Usopp', 'Zoro', 'Franky']
Luffy sneaks into the middle: ['Nami', 'Usopp', 'Luffy', 'Zoro', 'Franky']
Brook joins at the end: ['Nami', 'Usopp', 'Luffy', 'Zoro', 'Franky', 'Brook']

=== DELETION TESTS ===
Served first: Nami
Fell asleep and left the line: Zoro
Wandered off to play music: Brook
Line now: ['Usopp', 'Luffy', 'Franky']

=== SEARCH TESTS ===
Searching for Franky... index: 2
Franky is number 3 in line.
Searching for Buggy... index: -1
Buggy is not on the Thousand Sunny. No food for him.

=== PERFORMANCE CHECK ===
Front inserts took: 22.05 ms
End inserts took:   0.03 ms
```

## How Lists Work (and When a Linked List Wins)

A Python `list` is an **array-based** list. Its items were stored next to each other in memory, so jumping to any index was instant (O(1)), but inserting or deleting anywhere except the end forced every later item to shift.

A **linked list** stores each item in a node that points to the next node. Nothing has to shift; you just reconnect a couple of pointers. A linked list beat an array-based list when:

- the app inserted or removed at the **front** constantly (like this dinner line), or
- the app already **had the node** it wanted to change (like the "current song" in a playlist or the current page in browser history), so it could insert or delete next to it in O(1).

The trade-off was that a linked list couldn't jump straight to index 500; it had to walk from the start, which cost O(n). It also used more memory per item because every node stored a pointer (two, for a doubly linked list). For a line that mostly serves from the front, Python's `collections.deque` would have been a better fit than a plain list.

## Real-World Use Case

The dinner line worked exactly like a restaurant waitlist app, a ride-share driver queue, or a support-ticket queue: people join at the back, priority guests skip ahead, people drop out from the middle, and staff search by name. With a few people, a plain list was fine. With thousands, the cost of adding and removing at the front would have become noticeable, which is when a deque or linked list pays off.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

### My Reflection

This assignment made the cost of "where" concrete for me. I knew Python lists could insert anywhere, but I hadn't thought about the fact that inserting at index 0 makes every other item shift over. Theming it as Sanji's dinner line helped: when Nami goes to the front, everyone else literally has to step back. Timing it showed the same thing in numbers: about 22 ms at the front versus under 0.1 ms at the end on a 100,000-item list.

My main challenge was deciding how strict the functions should be. Python quietly accepts negative and oversized indexes, so it would've been easy to let those through. I decided a negative spot in line was more likely a bug than an intent, so I returned `None`. I also caught a bug where I searched for a crew member I'd already removed, which reminded me to trace the list through the whole program.

In real applications, these costs add up. A queue or feed that constantly changes at the front should use a deque or linked list, while anything read by position benefits from an array-based list.
