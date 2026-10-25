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
from inspect import stack


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        self.st = [] # Initialize and create List st

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Appending adds to the end (top) of the list, ensuring the newest item is the first one removed by pop() (LIFO)
        self.st.append(value)


    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # If the stack is empty, there is nothing to pop(), in that case we want to raise an error message to exception handle in main
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        # Here I am doing a manual implementation of pop functionality to help me reinforce my learning
        # We are storing the variable (value) -> (top item in the list) by using pythons negative indexing list functionality
        # then we are doing a delete call to remove that item from said list, and we return the result
        else:
            value = self.st[-1]
            del self.st[-1]
            return value


    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        # Peek returns the last value in the list, here I display this by using negative index again (we are telling python to return at very last item in sequence)
        else:
            return self.st[-1]


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        # If list is empty, return true, if not return false
        return not self.st


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # Initialize and create queue
        self.q = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # This operation supports FIFO behavior because a queue functions similarly a line at a store
        # The corresponding node which came in first is appended to the first place in the queue and subsequent are handled in itierative order
        self.q.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Here we guard against calling dequeue on an empty queue by raising an error for exception to handle in main
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        # .popleft() removes and returns the oldest element in O(1) time because it immediately accesses the value it needs to delete every time
        return self.q.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Here we guard against calling front on an empty queue by raising an error for exception to handle in main
        # front similarly to peek returns the item in the ds, but it returns the earliest added item
        if self.is_empty():
            raise IndexError("Front from empty queue")
        # Index 0 looks at the earliest-added item without removing it
        return self.q[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self.q


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
        stacky.push(i+1)

    print("Here we've created a stack object and pushed 4 values to it:", stacky.st)

    # 3. Improve the print statements so they clearly explain what is happening.
    if not stacky.is_empty():
        for i in range (len(stacky.st)):
            stacky.pop()
    print("Here we run a loop to pop all items in the stack:", stacky.st)
    # 4. Demonstrate LIFO behavior.

    print("Next we will push 2 items to the stack to demonstrate its behavior")
    # append two items to stack
    stacky.push(44)
    stacky.push(65)
    # show stack
    print("Stack current state:", stacky.st)
    # pop an item from stack
    stacky.pop()
    print("Stack after one pop (see how 65 is gone):", stacky.st)
    # show stack

    # 5. Show what happens when pop() is used on an empty stack.
    stacky.pop()

    print("Now what will happen if we pop on an empty stack?")
    try:
        stacky.pop()
    except IndexError as e:
        print("ERROR:", e)

    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    print("Now what will happen if we peek on an empty stack?")
    try:
        stacky.peek()
    except IndexError as e:
        print("ERROR:", e)

    # 7. Create a stack with only one item, remove it,
    stack = Stack()
    stack.push(40)
    print("Create a new stack with only one item:", stack.st)
    stack.pop()
    print("Stack after pop:", stack.st)
    #    and verify the stack is empty afterward.

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.

# 2. Add at least 4 values to the queue.

# 3. Improve the print statements so they clearly explain what is happening.

# 4. Demonstrate FIFO behavior.

# 5. Show what happens when dequeue() is used on an empty queue.
#

# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.

# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

if __name__ == "__main__":
    main()
