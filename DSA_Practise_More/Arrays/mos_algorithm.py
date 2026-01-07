# MO's Algorithm (Query Square Root Decomposition) | Set 1 (Introduction)

# Let us consider the following problem to understand MO's Algorithm.
# We are given an array and a set of query ranges, we are required to find the sum of every query range.

# Example: 

# Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
#         query[] = [0, 4], [1, 3] [2, 4]
# Output: Sum of arr[] elements in range [0, 4] is 8
#         Sum of arr[] elements in range [1, 3] is 4  
#         Sum of arr[] elements in range [2, 4] is 6

import math

def mos_algorithm(arr, query):
    if not (arr and query):
        return False
    
    N = len(arr)
    M = len(query)

    # Note: This simple sort (by R only) does not guarantee the optimal MO's complexity,
    # but it works for demonstrating the sliding window logic.
    query.sort(key = lambda x:x[1]) # Sort by R

    # Initialize current L (inclusive), current R (exclusive), and current sum
    currL, currR, currSum = 0, 0, 0

    for i in range(len(query)):
        L, R = query[i] # Target range is [L, R] (inclusive)

        # 1. Adjust Left Boundary (currL)

        # Move currL to the right (Shrink window from left)
        # We need to subtract elements arr[currL] until currL reaches L.
        while currL < L:
            currSum -= arr[currL] # Subtract arr[currL] before moving it past L
            currL += 1
            
        # Move currL to the left (Expand window to left)
        # We need to add elements arr[L-1] down to arr[currL].
        while currL > L:
            currL -= 1           # Move currL to L first (e.g., from 1 to 0)
            currSum += arr[currL] # Add the newly included element arr[currL]

        # 2. Adjust Right Boundary (currR)

        # Move currR to the right (Expand window to right)
        # We need to add elements arr[currR] up to arr[R].
        # The loop condition currR <= R is correct.
        while currR <= R:
            currSum += arr[currR] # Add the element arr[currR]
            currR += 1           # Move currR (exclusive) to the right

        # Move currR to the left (Shrink window from right)
        # We need to subtract elements arr[currR - 1] until currR reaches R + 1.
        while currR > R + 1:
            currR -= 1           # Move currR to the left (e.g., from 5 to 4)
            currSum -= arr[currR] # Subtract the element arr[currR] that just left the window

        # Print the sum of the current range [L, R]
        print("Sum of", query[i], "is", currSum)
    

if __name__ == "__main__":
    arr1 = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    query = [[0, 4], [1, 3], [2, 4]]

    # Expected Output:
    # Sum of [1, 3] is 4
    # Sum of [0, 4] is 8
    # Sum of [2, 4] is 6
    mos_algorithm(arr1, query)

