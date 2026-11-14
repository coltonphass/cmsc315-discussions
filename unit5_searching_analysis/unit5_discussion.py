"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # iterate in list and compare to target
    for index in range(len(lst)):
        if lst[index] == target:
            print("  [Linear] Found target in " + str(index + 1) + " iteration(s)")
            return index

     #target not found
    print("  [Linear] Target not found after " + str(len(lst)) + " iteration(s)")
    return -1




def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1
    iteration = 0

    while low <= high:
        # delcare middle
        iteration +=1
        mid = (low + high) // 2

        # Check right
        if lst[mid] < target:
           low = mid + 1
        # Check left
        elif lst[mid] > target:
            high = mid - 1
        # Check if target
        elif lst[mid] == target:
            print("  [Binary] Found target in " + str(iteration) + " iteration(s)")
            return mid
    # number not found
    print("  [Binary] Target not found after " + str(iteration) + " iteration(s)")
    return -1

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.


    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")


    lst = list(range(1, 11))

    print("Small dataset (1-10):", lst)
    print("\nSearching for 7 (exists):")
    print("-> Linear index:", linear_search(lst, 7))
    print("-> Binary index:", binary_search(lst, 7))
    print("\nSearching for 54 (missing):")
    print("-> Linear index:", linear_search(lst, 54))
    print("-> Binary index:", binary_search(lst, 54))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    large_lst = list(range(1, 201))

    print("Large dataset (1-200): [1, 2, 3, 4, 5, ... 200]")
    print("\nSearching for 94 (exists):")
    print("-> Linear index:", linear_search(large_lst, 94))
    print("-> Binary index:", binary_search(large_lst, 94))
    print("\nSearching for 5000 (missing):")
    print("-> Linear index:", linear_search(large_lst, 5000))
    print("-> Binary index:", binary_search(large_lst, 5000))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Empty list (0 iterations for both; safely returns -1)
    empty_lst = []
    print("\nEdge Case 1 - Empty List", empty_lst, "(searching for 5):")
    print("  -> Linear index:", linear_search(empty_lst, 5))
    print("  -> Binary index:", binary_search(empty_lst, 5))

    # Edge Case 2: Single-element list (1 iteration for both; returns index 0)
    single_lst = [42]
    print("\nEdge Case 2 - Single-Element List", single_lst, "(searching for 42):")
    print("  -> Linear index:", linear_search(single_lst, 42))
    print("  -> Binary index:", binary_search(single_lst, 42))

if __name__ == "__main__":
    main()