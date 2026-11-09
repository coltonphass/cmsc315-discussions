# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

---

# My Implementation

## Real-World Example: Student ID Lookup

My BST is a student ID lookup, like a school's registration system. Each node stores one student ID. The program can check if a student ID exists (search) and print the class roster sorted by ID (in-order traversal).

I inserted Casey's ID (10533) first on purpose. It's in the middle of the range, so the tree came out balanced, with 4 students on each side and a height of 3.

```
           -----------------(10533)-----------------
           |                                       |
        (10248)                                 (10744)
       /        \                              /        \
(10115)         (10372)                 (10619)         (10867)
                        \                                       \
                        (10456)                                 (10992)
```

(This is the program's own printout. Smaller IDs go left and larger IDs go right, at every node.)

## How a BST Works

A BST follows one rule at every node: **everything in the left subtree is smaller, and everything in the right subtree is larger.**

- **Insert** compares the new value with each node and goes left or right until it finds an empty spot. The recursive helper returns the node back to its parent, which is how the new node gets connected.
- **Search** follows the same comparisons. Each comparison rules out a whole subtree, so a search through my 9 students never takes more than 4 comparisons (height + 1). A linear search could take 9.
- **In-order traversal** visits the left subtree, then the node, then the right subtree. Because of the BST rule, that order is always sorted. My IDs were inserted in a scrambled order and came out smallest to largest.

**Duplicate rule:** if an ID is already in the tree, `insert` ignores it, because every student ID must be unique.

**Extension:** I added a `height()` method and a `print_tree()` helper that draws the tree top-down with `( )` around each value. The root sits centered in a `---( )---` bracket with `|` lines dropping onto its children, and the other levels use `/ \` branches. `print_tree()` places nodes in in-order sequence, so smaller values land further left, the same way you'd draw a BST by hand.

## Edge Cases

| Edge case | What happened | Why |
| --- | --- | --- |
| Empty roster | In-order returned `[]`, search returned `False`, height was -1 | The root is `None`, so the base case runs right away and nothing crashes. |
| One student (ID 10001) | In-order returned `[10001]`, search found it, height was 0 | The root is also the only leaf. |
| Duplicate: adding ID 10372 again | The tree still had 9 students | My insert ignores equal values, since IDs must be unique. A real registration system would show an error. |
| Same 9 IDs added in enrollment order | Height went from 3 to 8, and finding 10992 took 9 comparisons instead of 4 | Schools hand out IDs in order, so they arrive already sorted. Every ID went right, the tree became a straight line like a linked list, and search became O(n). |

The last edge case taught me the most: the **same data** can make a fast tree or a slow one, depending only on insertion order. Since real IDs are usually assigned in order, a plain BST would end up in its worst shape, which is why real systems use self-balancing trees.

## Reflection

While completing this assignment I learned how a binary search tree keeps data organized just by where it places each value. Writing insert, search, and in-order traversal recursively showed me that every method follows the same pattern: handle the empty spot, handle the match, otherwise go left or right and let recursion handle the smaller tree.

My biggest challenge was understanding why insert uses `node.left = self._insert_recursive(node.left, value)` instead of just calling the function. I traced a few inserts on paper and saw that the returned node is what connects a new node to its parent. I also built `show_search_path()` to print every comparison so I could see the search actually skipping subtrees.

A BST's ordering is what makes it efficient. Each comparison removes a whole subtree from consideration, so a balanced tree searches in O(log n). An unsorted list needs O(n) to search, and a sorted list needs O(n) to insert because items shift over. A BST does both in O(log n) while it stays balanced. My sorted-order edge case showed the catch: a degenerate tree loses that advantage.

## Sample Output

Run `unit4_discussion.py` to see the full output. Key results:

- In-order traversal: `[10115, 10248, 10372, 10456, 10533, 10619, 10744, 10867, 10992]`
- Search for 10456: `True` in 4 comparisons
- Search for 10500: `False` in 4 comparisons
- Balanced height 3 vs. enrollment-order height 8

### AI Attribution

I used Claude (Opus 5.5) as a study aid to review BST concepts and to help draft and check this code and README.