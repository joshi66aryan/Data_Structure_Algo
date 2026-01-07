# Smallest subarray with sum greater than x
# Difficulty: Easy

# Given a number x and an array of integers arr, find the smallest subarray with sum greater 
# than the given value. If such a subarray do not exist return 0 in that case.

# Examples:

# Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
# Output: 3
# Explanation: Minimum length subarray is [4, 45, 6]

# Input: x = 100, arr[] = [1, 10, 5, 2, 7]
# Output: 0
# Explanation: No subarray exist

# Constraints:
# 1 ≤ arr.size, x ≤ 105
# 0 ≤ arr[] ≤ 104

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

def smallestSubWithSum(arr,x):
    n = len(arr)

    min_len = float('inf')      # stores smallest window length found
    curr_sum = 0                # current window sum
    left = 0                    # left pointer of window

    # -----------------------------------------------------------
    # We expand the window using the right pointer (i)
    # -----------------------------------------------------------
    for right in range(n):
        curr_sum += arr[right]

        # -------------------------------------------------------
        # EXAMPLE WALK-THROUGH for: x = 51, arr = [1,4,45,6,0,19]
        #
        # right = 0 → curr_sum = 1
        #    sum <= 51 → continue expanding
        #
        # right = 1 → curr_sum = 1 + 4 = 5
        #    still <= 51
        #
        # right = 2 → curr_sum = 5 + 45 = 50
        #    still <= 51
        #
        # right = 3 → curr_sum = 50 + 6 = 56  → NOW > 51
        #    start shrinking window
        # -------------------------------------------------------

        # -------------------------------------------------------
        # Now shrink from the LEFT as long as sum > x
        # -------------------------------------------------------
        while curr_sum > x:
            # Update minimum size
            window_len = right - left + 1
            min_len = min(min_len, window_len)

            # ---------------------------------------------------
            # Example shrinking for arr = [1,4,45,6,0,19]
            #
            # curr_sum = 56 > 51 → window = [1,4,45,6]
            # window_len = 4 → min_len = 4
            #
            # Shrink:
            #    curr_sum -= arr[left]  → 56 - 1 = 55
            #    left = 1
            #
            # Still 55 > 51 → window = [4,45,6]
            # window_len = 3 → min_len = 3  (new minimum)
            #
            # Shrink:
            #    curr_sum -= arr[left] → 55 - 4 = 51
            #    left = 2
            #
            # STOP because curr_sum = 51 is NOT > x
            # ---------------------------------------------------

            curr_sum -= arr[left]
            left += 1

    # If no valid subarray found
    return min_len if min_len != float('inf') else 0

    


if __name__ == '__main__':
    print(smallestSubWithSum([1, 4, 45, 6, 0, 19], 51))
    print(smallestSubWithSum([1, 10, 5, 2, 7], 100))
