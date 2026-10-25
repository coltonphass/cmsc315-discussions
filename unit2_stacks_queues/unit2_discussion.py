"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        # A list works as a stack because adding/removing at the END of a list is O(1).
        # The end of the list is treated as the "top" of the stack.
        self.st = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # append() adds to the end (top) of the list, so the newest item is always
        # the first one removed by pop(). Last In, First Out (LIFO).
        self.st.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # If the stack is empty there is nothing to pop, so we raise an IndexError.
        # This makes the problem obvious to the caller instead of silently returning None
        # (which could be confused with a stored None value). main() handles it with try/except.
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        # Manual version of list.pop() to reinforce how it works:
        # 1. Grab the top item using negative indexing ([-1] = last item in the list)
        # 2. Delete that item from the list
        # 3. Return it
        value = self.st[-1]
        del self.st[-1]
        return value

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # peek() lets us LOOK at the top item without changing the stack.
        # Same empty-stack handling as pop() for consistency.
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.st[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        # An empty list is "falsy" in Python, so `not self.st` is True when the stack is empty.
        return not self.st

    def size(self):
        # Added: returns how many items are in the stack
        return len(self.st)


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # deque (double-ended queue) is built for fast adds/removes at BOTH ends.
        # A regular list would be slow here because list.pop(0) shifts every item left (O(n)).
        self.q = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # append() adds the new item to the BACK of the line, behind everyone already waiting.
        # Since items are removed from the FRONT, whoever arrived first is served first (FIFO).
        self.q.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Guard against dequeuing an empty queue by raising an IndexError for main() to handle.
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        # popleft() removes and returns the oldest item (the front) in O(1) time.
        # Unlike a list, a deque doesn't have to shift the remaining items over.
        return self.q.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # front() is the queue version of peek(): it shows who is "next in line"
        # (the earliest-added item) without removing it.
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.q[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        # An empty deque is "falsy," just like an empty list.
        return not self.q

    def size(self):
        # Added: returns how many items are in the queue
        return len(self.q)


def text_editor_scenario():
    # Added real-world scenario: a simple text editor that uses BOTH structures.
    #   - Stack: undo history. The most recent edit is undone first (LIFO).
    #   - Queue: save jobs. Files are saved in the order they were requested (FIFO).
    print("\n=== REAL-WORLD SCENARIO: TEXT EDITOR ===")

    undo_history = Stack()
    for edit in ["Typed 'Hello'", "Typed ' World'", "Bolded 'World'"]:
        undo_history.push(edit)
        print("Edit made:", edit)

    print("\nUser presses Undo twice:")
    print("  Undid:", undo_history.pop())  # newest edit is undone first
    print("  Undid:", undo_history.pop())
    print("  Next undo would be:", undo_history.peek())

    save_jobs = Queue()
    print()
    for file_name in ["notes.txt", "essay.docx", "todo.md"]:
        save_jobs.enqueue(file_name)
        print("Save requested:", file_name)

    print("\nProcessing save jobs in order:")
    while not save_jobs.is_empty():
        print("  Saved:", save_jobs.dequeue())  # first request is saved first


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("\n=== STACK DEMO ===")
    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    stacky = Stack()

    # 2. Add at least 4 values to the stack.
    for i in range(4):
        stacky.push(i + 1)
    print("Created a stack and pushed 4 values (top is on the right):", stacky.st)

    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # Printing each popped value shows the order: 4, 3, 2, 1 (reverse of how they went in)
    print("Popping every item. Notice they come out in REVERSE order (LIFO):")
    while not stacky.is_empty():
        print("  Popped:", stacky.pop())
    print("Stack is now empty:", stacky.st)

    print("\nPushing 44, then 65:")
    stacky.push(44)
    stacky.push(65)
    print("Current stack:", stacky.st)
    print("peek() shows the top without removing it:", stacky.peek())
    print("pop() removes the top item:", stacky.pop())
    print("Stack after one pop (65 is gone, 44 remains):", stacky.st)

    # 5. Show what happens when pop() is used on an empty stack.
    print("Popping the last item:", stacky.pop())
    print("\nWhat happens if we pop() an empty stack?")
    try:
        stacky.pop()
    except IndexError as e:
        print("  ERROR:", e)

    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    print("What happens if we peek() an empty stack?")
    try:
        stacky.peek()
    except IndexError as e:
        print("  ERROR:", e)

    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    one_item_stack = Stack()
    one_item_stack.push(40)
    print("\nNew stack with one item:", one_item_stack.st)
    print("Popped:", one_item_stack.pop())
    print("Is the stack empty now?", one_item_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    # Requirements:
    # 1. Create a Queue object.
    queue = Queue()

    # 2. Add at least 4 values to the queue.
    for i in range(4):
        queue.enqueue(i + 1)

    # 3. Improve the print statements so they clearly explain what is happening.
    print("Created a queue and enqueued 4 values (front is on the left):", list(queue.q))

    # 4. Demonstrate FIFO behavior.
    print("front() shows who is next in line:", queue.front())
    print("Dequeued:", queue.dequeue())
    print("Queue after one dequeue (1 was first in, so it left first):", list(queue.q))
    print("Think of it like a line: items join at the back (tail) and leave from the front (head).")

    print("\nDequeuing the rest. Notice they come out in the SAME order they went in (FIFO):")
    while not queue.is_empty():
        print("  Dequeued:", queue.dequeue())
    print("Queue is now empty:", list(queue.q))

    # 5. Show what happens when dequeue() is used on an empty queue.
    print("\nWhat happens if we dequeue() an empty queue?")
    try:
        queue.dequeue()
    except IndexError as e:
        print("  ERROR:", e)

    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    print("What happens if we call front() on an empty queue?")
    try:
        queue.front()
    except IndexError as e:
        print("  ERROR:", e)

    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    one_item_queue = Queue()
    one_item_queue.enqueue(40)
    print("\nNew queue with one item:", list(one_item_queue.q))
    print("Dequeued:", one_item_queue.dequeue())
    print("Is the queue empty now?", one_item_queue.is_empty())

    # Added: real-world scenario using both structures
    text_editor_scenario()


if __name__ == "__main__":
    main()