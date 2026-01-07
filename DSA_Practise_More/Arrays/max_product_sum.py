# Maximum Product Subarray
# Difficulty: Medium

# Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
# Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the answer fits in a 32-bit integer.

# Examples

# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

# Input: arr[] = [2, 3, 4] 
# Output: 24 
# Explanation: For an array with all positive elements, the result is product of all elements. 

# Constraints:
# 1 ≤ arr.size() ≤ 106
# -10  ≤  arr[i]  ≤  10

# Expected Complexities
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)



def maxProductSubarray(arr):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # We perform a single pass maintaining only constant variables.

    # Initialize max product, min product, and global answer
    maxProd = minProd = ans = arr[0]

    # -------------------------------------------------------------
    # Example walkthrough is shown inline for arr = [-2, 6, -3, -10, 0, 2]
    # -------------------------------------------------------------
    # Start:
    # maxProd = minProd = ans = -2
    # -------------------------------------------------------------

    for i in range(1, len(arr)):
        num = arr[i]

        # If current number is negative, we swap maxProd and minProd.
        # Why? Because multiplying by negative flips signs.
        #
        # Example steps:
        # i=1 → num=6 (positive, no swap)
        # i=2 → num=-3 (negative → swap max/min)
        # i=3 → num=-10 (negative → swap again)
        # i=4 → num=0 (reset behavior)
        # i=5 → num=2
        if num < 0:
            maxProd, minProd = minProd, maxProd

        # Update max product ending at current index
        # Either:
        # 1. take num alone
        # 2. extend previous maxProd * num
        #
        # Update min product similarly (needed because of negatives)
        prevMax, prevMin = maxProd, minProd  # just for commenting clarity

        maxProd = max(num, prevMax * num)
        minProd = min(num, prevMin * num)

        # ------------------------------
        # EXAMPLE ITERATION BREAKDOWN:
        # ------------------------------
        # For arr = [-2, 6, -3, -10, 0, 2]:
        #
        # i=1 → num=6
        #   maxProd = max(6, -2*6) = 6
        #   minProd = min(6, -2*6) = -12
        #   ans = 6
        #
        # i=2 → num=-3 (negative → swap first)
        #   swapped → maxProd=-12, minProd=6
        #   maxProd = max(-3, -12 * -3) = 36
        #   minProd = min(-3, 6 * -3)   = -18
        #   ans = 36
        #
        # i=3 → num=-10 (negative → swap)
        #   swapped → maxProd=-18, minProd=36
        #   maxProd = max(-10, -18 * -10) = 180
        #   minProd = min(-10, 36 * -10)  = -360
        #   ans = 180  <-- max product subarray found here
        #
        # i=4 → num=0
        #   maxProd = max(0, 180*0) = 0
        #   minProd = min(0, -360*0) = 0
        #   ans = 180
        #
        # i=5 → num=2
        #   maxProd = max(2, 0*2) = 2
        #   minProd = min(2, 0*2) = 2
        #   ans = 180 (unchanged)
        # ------------------------------

        # Update the global answer
        ans = max(ans, maxProd)

    return ans



if __name__ == '__main__':
    arr = [-2, 6, -3, -10, 0, 2]
    ans = maxProductSubarray(arr)
    print("The result:",ans)