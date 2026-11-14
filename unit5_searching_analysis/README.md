# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Implementation Summary

I implemented linear search and binary search in Python and added an iteration counter to each one, so the program prints how many checks each search took. That turned the Big-O comparison into numbers I could see in the output instead of just theory.

### Linear Search: O(n)

`linear_search` loops through the list from the first index to the last and returns the index as soon as it finds the target. If it reaches the end without a match, it returns `-1`. In the worst case (the target is last or missing), it checks every item, so the work grows at the same rate as the list: O(n). It works on any list, sorted or not.

### Binary Search: O(log n)

`binary_search` only works on a **sorted** list. It keeps a search window between `low` and `high`:

1. Find the middle index: `mid = (low + high) // 2`.
2. If the middle value is the target, return `mid`.
3. If the middle value is **too small**, the target must be on the right, so `low` moves to `mid + 1` and the left half is thrown away.
4. If the middle value is **too big**, the target must be on the left, so `high` moves to `mid - 1` and the right half is thrown away.
5. The loop runs `while low <= high`. When `low` passes `high`, the window is empty and the function returns `-1`.
   Each pass cuts the remaining list in half, so the most checks it can ever need is ⌊log₂(n)⌋ + 1.

## Results

| Test | List size | Target | Linear iterations | Binary iterations |
| --- | --- | --- | --- | --- |
| Small, found | 10 | 7 | 7 | 4 |
| Small, missing | 10 | 54 | 10 | 4 |
| Large, found | 200 | 94 | 94 | 7 |
| Large, missing | 200 | 5000 | 200 | 8 |

**Performance analysis:** on the 10-item list the difference was small, but on the 200-item list linear search needed up to 200 checks while binary search never needed more than 8. That matches the formula: ⌊log₂(200)⌋ + 1 = 7 + 1 = 8. Doubling the list size doubles the work for linear search, but only adds about one more check for binary search, which is why binary search pulls further ahead as datasets grow.

## Edge Cases

- **Empty list `[]`:** both searches returned `-1` after 0 iterations. Linear search's loop never runs, and in binary search `high` starts at `-1`, so `low <= high` is false right away. Neither one crashes.
- **Single-element list `[42]`:** both found 42 at index 0 in 1 iteration. For binary search, `low` and `high` are both 0, and the `<=` in the loop condition is what lets that last remaining item still get checked.
## Real-World Scenario: Game Leaderboard

I modeled an arcade game that uses both searches for different jobs:

- **Leaderboard lookup (binary search):** the leaderboard is stored sorted from lowest to highest score, so binary search can find a score fast. Since the highest score is last, rank is counted from the end with `rank = len(leaderboard) - index`. Searching 8 scores, it found 8450 at **rank #2** in 3 iterations and confirmed 5000 was not on the board in 3 iterations.
- **Match history (linear search):** the list of players is in the order games were played, not sorted, so binary search would guess the wrong half. Linear search found Mia in game #4 after 4 checks and confirmed Zed didn't play after checking all 5 names.
  This showed the real tradeoff: binary search is faster, but only when the data is already sorted.

## Challenges

- **Keeping `low` and `high` straight.** I'm dyslexic, and I kept wanting to move `low` and `high` to the opposite sides. I got past it by writing the algorithm from memory several times until the pattern stuck. A code review also caught two comments where I had described the direction backwards, which I fixed.
- **The math notation.** Symbols like log₂(n), ⌊ ⌋, and T(n) were overwhelming at first. It clicked once I thought of log n as "how many times can I cut the list in half before I reach 1," and used a doubling test: if the list doubles, does the work stay the same, go up by one, double, or go up four times?
- **Remembering time complexities.** I worked on this with story-based practice questions instead of memorizing a chart.
## Discussion Reflection

I learned that binary search is incredibly efficient on sorted data, and the bigger the dataset, the bigger the advantage. On my 200-item list, binary search found 94 in 7 iterations while linear search took 94, and it confirmed a missing value after only 8 checks.

My biggest challenge was writing binary search correctly. I'm dyslexic, and I kept moving `low` and `high` to the opposite sides. Rewriting the algorithm from memory several times is what made it stick. The math notation also felt overwhelming until I started thinking of log n as "how many times can I cut the list in half."

I would use binary search on data that stays sorted and gets searched often, like a game leaderboard. I would use linear search on unsorted data, like a match history in the order games were played, or on small lists that only get searched once. In those cases, sorting first costs more work than just checking every item.

## How to Run

Right-click `unit5_discussion.py` in IntelliJ and select **Run**.