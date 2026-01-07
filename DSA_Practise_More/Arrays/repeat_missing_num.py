# Repeat and Missing Number Array

# medium

# There are certain problems which are asked in the interview to also check how you 
# take care of overflows in your problem.

# This is one of those problems.

# Please take extra care to make sure that you are type-casting your ints to long 
# properly and at all places. Try to verify if your solution works if number of 
# elements is as large as 105

# Food for thought :

# Even though it might not be required in this problem, in some cases, you might
# be required to order the operations cleverly so that the numbers do not overflow.
# For example, if you need to calculate n! / k! where n! is factorial(n), one approach 
# is to calculate factorial(n), factorial(k) and then divide them.
# Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
# Obviously approach 1 is more susceptible to overflows.
# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4

def tell_missing_num(arr):
    """
    Repeat and Missing Number Problem
    --------------------------------
    Given an array of size n containing numbers 1..n:
      - One number A appears twice (repeated)
      - One number B is missing
    We return [A, B] in that order.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # ===================================================================
    # INTUITION (The "Kid Roll-Call" Story – Why This Works!)
    # ===================================================================
    # Imagine kids with roll numbers 1 to n are supposed to line up.
    # Perfect day:
    #   Sum of roll numbers        = 1 + 2 + ... + n
    #   Sum of (roll numbers)²     = 1² + 2² + ... + n²
    #
    # But today:
    #   - One kid A sneaked in TWICE  → we added +A extra
    #   - One kid B is hiding         → we never added B
    #
    # So compared to perfect sums:
    #   Actual sum          = Perfect sum - B + A   →  difference = B - A
    #   Actual sum of squares = Perfect sq sum - B² + A² → difference = B² - A²
    #
    # And we know from school: B² - A² = (B - A)(B + A)
    #
    # So we get two beautiful clues:
    #   Clue 1 → (B - A)           from normal sum difference
    #   Clue 2 → (B - A) * (B + A) from sum-of-squares difference
    #
    # Divide Clue 2 by Clue 1 → we instantly get (B + A)!
    # Then it's just 7th-grade algebra:
    #       B + A = ?
    #       B - A = ?
    #     → Add them → 2B, Subtract → 2A
    #
    # That's the whole magic — no extra space needed!
    # ===================================================================

    # ---------------------------------------------------------------
    # STEP 1: Compute the expected sums for the perfect sequence 1..n
    # ---------------------------------------------------------------
    n = len(arr)
    # Example: n = 5 for arr = [3,1,2,5,3]
    # Sum of 1..n → n(n+1)/2
    expected_sum = n * (n + 1) // 2
    # Example: 5*6//2 = 15
    # Sum of squares 1² + 2² + ... + n² → n(n+1)(2n+1)/6
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
    # Example: 5*6*11//6 = 55

    # ---------------------------------------------------------------
    # STEP 2: Compute actual sums from the array
    # ---------------------------------------------------------------
    actual_sum = 0      # will become 3+1+2+5+3 = 14
    actual_sq_sum = 0   # will become 9+1+4+25+9 = 48
    for num in arr:
        actual_sum += num
        actual_sq_sum += num * num
        # Example iterations:
        # num=3: sum=3, sq=9
        # num=1: sum=4, sq=10
        # num=2: sum=6, sq=14
        # num=5: sum=11, sq=39
        # num=3: sum=14, sq=48

    # ---------------------------------------------------------------
    # STEP 3: Compute differences
    # ---------------------------------------------------------------
    # expected_sum - actual_sum = (1+2+3+4+5) - (sum of array)
    # = B - A
    S_diff = expected_sum - actual_sum
    # Example: 15 - 14 = 1 = B - A

    # expected_sq_sum - actual_sq_sum = (1²+2²+...) - (sum of array squares)
    # = B² - A² = (B - A)(B + A)
    SQ_diff = expected_sq_sum - actual_sq_sum
    # Example: 55 - 48 = 7 = (B - A)(B + A)

    # ---------------------------------------------------------------
    # STEP 4: Solve for B + A
    #
    # SQ_diff = (B-A)(B+A)
    # B + A = SQ_diff / (B-A)
    #
    # So:
    # B_plus_A = SQ_diff / S_diff
    # ---------------------------------------------------------------
    B_plus_A = SQ_diff // S_diff
    # Example: 7 // 1 = 7 → B + A = 7

    # ---------------------------------------------------------------
    # STEP 5: Solve for B (the missing number)
    #
    # We now have:
    # B - A = S_diff
    # B + A = B_plus_A
    #
    # Add them:
    # (B - A) + (B + A) = S_diff + B_plus_A
    # 2B = S_diff + B_plus_A
    #
    # B = (S_diff + B_plus_A) / 2
    # ---------------------------------------------------------------
    B = (S_diff + B_plus_A) // 2
    # Example: B = (1 + 7) // 2 = 4

    # ---------------------------------------------------------------
    # STEP 6: Solve for A (the repeated number)
    #
    # From B - A = S_diff:
    # A = B - S_diff
    # ---------------------------------------------------------------
    A = B - S_diff
    # Example: A = 4 - 1 = 3
    # A = repeated number
    # B = missing number

    return [A, B]


if __name__ == "__main__":

    print(f"Result1:{tell_missing_num([3, 1, 2, 5, 3])}")
    print(f"Result1:{tell_missing_num([4, 3, 6, 2, 1, 1])}")