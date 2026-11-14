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

    """
    Linear search has a time complexity of O(n) because it searches every element in the list 
    until it finds the target or exhausts all options.
    """
    # Iterate through whole list
    for index in range(len(lst)):
        if lst[index] == target: # If the index has what we are looking for
            print("  [Linear] Found target in " + str(index + 1) + " iteration(s)")
            return index

    # We have searched entire list and have not found the target in index
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

    """
    How Binary Search works:
    Continue searching while a valid search window still exists.
    If low becomes greater than high, the window has collapsed to zero elements,
    meaning every possible location has been eliminated and the target is not in the list.
    """

    # Here we are going to loop until we have exhausted viable all options
    while low <= high: # Low should not be greater than high unless target is not in list
        iteration +=1 # Added iteration counter to visualize each pass
        mid = (low + high) // 2 # Middle is going to equal the low + high divided in half

        # The middle value is too small, so the target must be on the RIGHT side
        if lst[mid] < target:
           low = mid + 1 # Imagine the list index and placing the lowest side we start from one to the right of mid, this cuts the list in half

        # The middle value is too big, so the target must be on the LEFT side
        elif lst[mid] > target:
            high = mid - 1 # Imagine the list index and placing the highest side we end on one to the left of mid, this cuts the list in half

        # Check if mid is target
        elif lst[mid] == target:
            print("  [Binary] Found target in " + str(iteration) + " iteration(s)")
            return mid
    # We have searched entire logical half of list and have not found the target in mid
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
    large_lst = list(range(1, 1_000_001))

    print("Large dataset (1-1,000,000): [1, 2, 3, 4, 5, ... 1,000,000]")
    print("\nSearching for 94 (exists):")
    print("-> Linear index:", linear_search(large_lst, 94))
    print("-> Binary index:", binary_search(large_lst, 94))
    print("\nSearching for 1,000,001 (missing):")
    print("-> Linear index:", linear_search(large_lst, 1000001))
    print("-> Binary index:", binary_search(large_lst, 1000001))

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


    print("\n=== REAL WORLD SCENARIO - GAME HIGH SCORES ===")
    # Leaderboard is SORTED lowest to highest, so we can use binary search
    leaderboard = [1200, 2500, 3100, 4800, 5600, 7200, 8450, 9900]
    print("Leaderboard : ", leaderboard)

    # Check two scores: one that exists and one that doesnt
    scores_to_check = [8450, 5000]

    for score in scores_to_check:
        print("\nLooking up score " + str(score) + ":")
        index = binary_search(leaderboard, score)

        if index != -1:
            # The highest score is at the END of the list,
            # so rank is counted from the END: rank #1 is last item in list
            rank = len(leaderboard) - index
            print("-> Score " + str(score) + " is on the leaderboard at rank # " +str(rank))
        else:
            print("-> Score " + str(score) + " is not on the leaderboard")

    # Match history is in order games were PLAYED and is not sorted alphabetically
    # Binary search will not work here, we will use linear
    match_history = ["Brandon", "Ola", "Colton", "Mark"]
    print("\nToday's match history (order played):", match_history)

    for player in["Colton", "Leon"]:
        print("\n Did " + player + " play today?")
        index = linear_search(match_history, player)

        if index != -1:
            print("-> Yes, " + player + " played in game #" + str(index + 1))
        else:
            print("-> No, " + player + " did not play today")

if __name__ == "__main__":
    main()