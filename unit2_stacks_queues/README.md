# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## What I Built

I completed every `TODO (Student)` block in `unit2_discussion.py` and kept the original prompts in place.

**Stack class**
- Used a Python `list` as the internal storage, with the end of the list acting as the top of the stack.
- `push()` used `append()` to add to the top, so the newest item was always the first one removed (LIFO).
- `pop()` was written manually instead of calling `list.pop()`. It grabbed the top item with negative indexing (`[-1]`), deleted it, and returned it. I did this to reinforce how the operation works.
- `peek()` returned the top item without removing it.
- `is_empty()` returned `True` when the list had no items.
- Added a `size()` method that returned the number of items.

**Queue class**
- Used `collections.deque` as the internal storage, because a deque removes from the front in O(1) time. A regular list would have needed `pop(0)`, which shifts every remaining item over (O(n)).
- `enqueue()` used `append()` to add to the back of the line.
- `dequeue()` used `popleft()` to remove from the front, so the first item in was the first item out (FIFO).
- `front()` returned the next item in line without removing it.
- `is_empty()` returned `True` when the deque had no items.
- Added a `size()` method that returned the number of items.

## Design Decisions

**Empty structure handling:** `pop()`, `peek()`, `dequeue()`, and `front()` all raised an `IndexError` when called on an empty structure. I chose this over returning `None` because:

- It made the problem obvious instead of failing silently.
- A returned `None` could be confused with a `None` value that was actually stored.
- It matched how Python's own `list.pop()` behaves.

The tradeoff was that every risky call in `main()` had to be wrapped in a `try/except` block to keep the program from crashing.

**Readable output:** The demos printed each value as it was removed, so the output showed the LIFO order (4, 3, 2, 1) and FIFO order (1, 2, 3, 4) directly instead of just showing an empty structure at the end.

## Edge Cases Tested

| Test | Result |
| --- | --- |
| `pop()` on an empty stack | Raised `IndexError: Pop from empty stack`, caught and printed |
| `peek()` on an empty stack | Raised `IndexError: Peek from empty stack`, caught and printed |
| One-item stack: push, pop, check | Popped 40, `is_empty()` returned `True` |
| `dequeue()` on an empty queue | Raised `IndexError: Dequeue from empty queue`, caught and printed |
| `front()` on an empty queue | Raised `IndexError: Front from empty queue`, caught and printed |
| One-item queue: enqueue, dequeue, check | Dequeued 40, `is_empty()` returned `True` |

## Real-World Scenario: Text Editor

I added a `text_editor_scenario()` function that used both structures the way a real text editor might:

- **Undo history (Stack):** Three edits were pushed onto the stack. Pressing Undo popped the most recent edit first, then the one before it, which is exactly how undo works in real editors.
- **Save jobs (Queue):** Three save requests were enqueued. They were processed in the same order they were requested, so the first file asked to be saved was saved first.

## Memory Usage

Both structures grew linearly, O(n). Each new item took up one more slot, and nothing was pre-allocated to a fixed size, so the only real limit was available memory.

- A Python list over-allocates a little extra space so most `append()` calls stay fast.
- A deque grows in fixed-size blocks linked together.
- Removing items freed that space again.

Because neither class had a capacity limit, there was no risk of stack overflow or a "full queue" like there would be with a fixed-size array implementation.

## How to Run

```
python unit2_discussion.py
```

---
#### AI Attribution

I used Claude *(Opus 5.5)* to help structure this README and provide examples of real world scenarios, provide study guide for core concepts, as well as tighten up some wording.