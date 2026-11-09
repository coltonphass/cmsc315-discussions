"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.

STUDENT NOTES:
My example is a student ID lookup, like a school registration system.
Search checks if an ID exists, and in-order traversal prints the roster
sorted by ID.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Store the student ID.
        self.value = value

        # Both children start empty.
        self.left = None    # smaller IDs go left
        self.right = None   # larger IDs go right


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # The tree starts empty. The first ID inserted becomes the root.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Placing smaller values left and larger values right keeps the tree in order.
        # Search can then follow the same comparisons to find the value later.
        # Saving the result to self.root also handles inserting into an empty tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Found an empty spot, so the new node goes here.
        if node is None:
            return Node(value)

        if value < node.value:
            # Smaller values go left.
            # Assigning the result back connects the new node to its parent.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values go right.
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate ID, so ignore it. Student IDs have to be unique.
            pass

        # Return the node so the parent stays connected to it.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Linear search may have to check every item.
        # A BST skips a whole side of the tree with each comparison,
        # so a balanced tree only needs about log n checks.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reached an empty spot, so the value isn't in the tree.
        if node is None:
            return False

        # Found it.
        if value == node.value:
            return True

        # Only one side can have the value, so search that side.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Start with an empty list and let the helper fill it.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # This produces sorted output because at every node it adds
        # the smaller values first, then the node, then the larger values.

        # Nothing to add from an empty spot.
        if node is None:
            return

        self._inorder_recursive(node.left, values)   # smaller values
        values.append(node.value)                    # this value
        self._inorder_recursive(node.right, values)  # larger values

    # Extra method I added to show how tall the tree is.
    def height(self):
        # Height is the number of edges on the longest path from the root to a leaf.
        # A search takes at most height + 1 comparisons.
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        # An empty tree is -1, so a single node is 0.
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        # Add 1 to the taller side.
        return 1 + max(left_height, right_height)


# =========================================================
# Helper functions I added to make the output easier to follow
# =========================================================

def insert_and_explain(tree, name, student_id):
    # Follow the same path insert will take and record each left/right step.
    path = ""
    node = tree.root
    while node is not None:
        if student_id < node.value:
            path = path + str(node.value) + " -> left, "
            node = node.left
        elif student_id > node.value:
            path = path + str(node.value) + " -> right, "
            node = node.right
        else:
            path = path + "already enrolled, "
            break

    tree.insert(student_id)

    if path == "":
        print("   " + name + " (ID " + str(student_id) + ") becomes the ROOT")
    else:
        print("   " + name + " (ID " + str(student_id) + "): " + path + "placed")


def show_search_path(tree, value):
    # Same steps as search, but prints each comparison.
    # Returns the number of comparisons it took.
    node = tree.root
    steps = 0
    while node is not None:
        steps = steps + 1
        if value == node.value:
            print("      Step " + str(steps) + ": " + str(value) + " == " + str(node.value) + "  FOUND")
            return steps
        elif value < node.value:
            print("      Step " + str(steps) + ": " + str(value) + " < " + str(node.value) + "  go LEFT (skip the right side)")
            node = node.left
        else:
            print("      Step " + str(steps) + ": " + str(value) + " > " + str(node.value) + "  go RIGHT (skip the left side)")
            node = node.right
    print("      Reached an empty spot, so " + str(value) + " is not in the tree")
    return steps


def place_nodes(node, depth, slot, pieces):
    # Works out where each node and branch goes for print_tree.
    # Each piece is saved as [row, column, text].
    # It walks the tree in-order, so smaller values end up further left.
    # slot holds the next free column and is shared by every call.
    # Returns the node's center column, or -1 for an empty spot.
    if node is None:
        return -1

    # Place the left subtree first.
    left_center = place_nodes(node.left, depth + 1, slot, pieces)

    # Give this node the next free column and leave a space after it.
    label = "(" + str(node.value) + ")"
    column = slot[0]
    slot[0] = slot[0] + len(label) + 1
    center = column + len(label) // 2
    row = depth * 2                  # nodes go on rows 0, 2, 4, ...

    # Then place the right subtree.
    right_center = place_nodes(node.right, depth + 1, slot, pieces)

    if depth == 0:
        # The root gets a bracket that lines up with both children:
        #      -------(root)-------
        #      |                  |
        # If it has both children, center it between them.
        if left_center != -1 and right_center != -1:
            center = (left_center + right_center) // 2
            column = center - len(label) // 2

        # Draw dashes out to each child, then a | straight down to it.
        if left_center != -1:
            dashes = "-" * (column - left_center)
            pieces.append([row, left_center, dashes])
            pieces.append([row + 1, left_center, "|"])
        if right_center != -1:
            end_of_label = column + len(label)
            dashes = "-" * (right_center - end_of_label + 1)
            pieces.append([row, end_of_label, dashes])
            pieces.append([row + 1, right_center, "|"])
    else:
        # Other nodes use / and \ halfway between the node and each child.
        if left_center != -1:
            pieces.append([row + 1, (center + left_center) // 2, "/"])
        if right_center != -1:
            pieces.append([row + 1, (center + right_center) // 2 + 1, "\\"])

    # Save the label once its final column is known.
    pieces.append([row, column, label])

    return center


def print_tree(tree):
    # Prints the tree top-down with the root on top.
    values = tree.inorder()
    if len(values) == 0:
        print("   (empty tree)")
        return

    # Figure out where everything goes. slot ends up as the total width.
    pieces = []
    slot = [0]
    place_nodes(tree.root, 0, slot, pieces)

    # Make a blank grid with a row for each level and a row of branches between levels.
    number_of_rows = tree.height() * 2 + 1
    canvas = []
    for r in range(number_of_rows):
        canvas.append([" "] * (slot[0] + 2))

    # Copy each label and branch onto the grid one character at a time.
    for piece in pieces:
        row = piece[0]
        column = piece[1]
        text = piece[2]
        for i in range(len(text)):
            canvas[row][column + i] = text[i]

    # Print each row as a line of text.
    for row in canvas:
        print("   " + "".join(row).rstrip())


def find_name(students, student_id):
    # Linear search through the student list to match an ID to a name.
    for pair in students:
        if pair[1] == student_id:
            return pair[0]
    return "Unknown"


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Real-world example: looking up students by student ID")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # These represent students and their IDs in a class roster.
    # Casey's ID (10533) goes first because it's in the middle, which keeps the tree balanced.
    students = [
        ("Casey", 10533),
        ("Jordan", 10248),
        ("Riley", 10744),
        ("Alex", 10115),
        ("Morgan", 10372),
        ("Sam", 10619),
        ("Jamie", 10867),
        ("Taylor", 10456),
        ("Avery", 10992),
    ]

    roster = BST()
    for pair in students:
        insert_and_explain(roster, pair[0], pair[1])

    # Each comparison rules out one whole side of the tree.
    # For example, going left at 10533 skips the four larger IDs at once.
    print("\nThe tree (smaller IDs go left, larger IDs go right):")
    print_tree(roster)
    print("Height of the tree:", roster.height())
    print("So any search takes at most", roster.height() + 1, "comparisons for", len(students), "students.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # The IDs went in out of order, but in-order traversal returns them sorted
    # because it visits left, node, right at every node.
    insert_order = []
    for pair in students:
        insert_order.append(pair[1])
    print("Insertion order:   ", insert_order)

    sorted_ids = roster.inorder()
    print("In-order traversal:", sorted_ids)

    print("\nClass roster, sorted by student ID:")
    for student_id in sorted_ids:
        print("   " + str(student_id) + "  " + find_name(students, student_id))

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Search for IDs that exist.
    # Taylor is at the deepest level and still only takes 4 comparisons.
    print("Search for 10456 (Taylor):", roster.search(10456))
    show_search_path(roster, 10456)

    print("Search for 10619 (Sam):", roster.search(10619))
    show_search_path(roster, 10619)

    # Search for IDs that don't exist.
    # Reaching an empty spot means the ID isn't there, without checking every node.
    print("Search for 10500 (no such student):", roster.search(10500))
    show_search_path(roster, 10500)

    print("Search for 99999 (no such student):", roster.search(99999))
    show_search_path(roster, 99999)

    print("\nA linear search through the student list could need up to", len(students), "checks.")
    print("The BST never needed more than", roster.height() + 1, "comparisons.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: empty tree.
    # The root is None, so traversal returns an empty list and search returns False.
    print("\nEdge case 1: an empty roster (no students enrolled yet)")
    empty_roster = BST()
    print("   In-order traversal:", empty_roster.inorder())
    print("   Search for 10533:", empty_roster.search(10533))
    print("   Height:", empty_roster.height(), "(an empty tree has height -1)")
    print_tree(empty_roster)

    # Edge case 2: tree with one node.
    # The root is also the only leaf.
    print("\nEdge case 2: a roster with only one student")
    small_roster = BST()
    small_roster.insert(10001)
    print("   In-order traversal:", small_roster.inorder())
    print("   Search for 10001:", small_roster.search(10001))
    print("   Height:", small_roster.height(), "(the root is also the only leaf)")
    print_tree(small_roster)

    # Edge case 3: duplicate ID.
    # Insert ignores equal values, so the tree stays the same.
    # A real registration system would show an error instead.
    print("\nEdge case 3: adding ID 10372 a second time")
    before = len(roster.inorder())
    roster.insert(10372)
    after = len(roster.inorder())
    print("   Students before:", before, " Students after:", after)
    print("   The duplicate ID was ignored, because each student ID must be unique.")

    # Edge case 4: IDs inserted in sorted order.
    # Schools usually assign IDs in order, so each new ID is the largest and goes right.
    # The tree turns into a straight line and search becomes O(n).
    print("\nEdge case 4: the same 9 IDs added in enrollment order (smallest first)")
    sorted_roster = BST()
    for student_id in sorted_ids:
        sorted_roster.insert(student_id)
    print("   The tree is now a straight line going right:")
    print_tree(sorted_roster)
    print("   Balanced roster height:", roster.height())
    print("   Enrollment-order roster height:", sorted_roster.height())
    print("   Searching for Avery (10992) in the enrollment-order roster:")
    steps = show_search_path(sorted_roster, 10992)
    print("   Every left side above was EMPTY, so each step ruled out nothing.")
    print("   That took", steps, "comparisons instead of 4. Insertion order matters!")


if __name__ == "__main__":
    main()