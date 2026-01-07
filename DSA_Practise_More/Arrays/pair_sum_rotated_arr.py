# Pair Sum in a Sorted and Rotated Array

# Given an array arr[] of size n, which is sorted and then rotated around an unknown pivot, the task 
# is to check whether there exists a pair of elements in the array whose sum is equal to a given target value.

# Examples : 

# Input: arr[] = [11, 15, 6, 8, 9, 10], target = 16
# Output: true
# Explanation: There is a pair (6, 10) with sum 16.

# Input: arr[] = [11, 11, 15, 26, 38, 9, 10], target = 35
# Output: true
# Explanation: There is a pair (26, 9) with sum 35.

# Input: arr[] = [9, 10, 10, 11, 15, 26, 38], target = 45
# Output: false
# Explanation: There is no pair with sum 45.

def pairSumRotatedArr(arr, target):
    """
    Checks if a pair with the given target sum exists in a sorted and rotated array.
    This solution uses an O(n) linear scan to find the pivot (breakpoint), 
    followed by an O(n) two-pointer search, resulting in an overall time complexity of O(n).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    --- Example Trace: arr = [11, 15, 6, 8, 9, 10], target = 16 (n=6) ---
    """
    n = len(arr)
    # Trace: n = 6

    # --- Step 1: Find the Index of the Largest Element (the breakpoint) ---
    # The largest element (arr[i]) is immediately followed by the smallest element (arr[i+1] % n).
    i = 0
    # Trace: i starts at 0
    for i in range(n - 1):
        # We are looking for the point where the ascending order breaks.
        # Trace: 
        # Iteration 1 (i=0): arr[0]=11, arr[1]=15. 11 > 15 is False. Continue.
        # Iteration 2 (i=1): arr[1]=15, arr[2]=6. 15 > 6 is True. Break loop.
        if arr[i] > arr[i + 1]:
            break
	
    # Trace: i is now 1 (index of 15, the largest element).
    # This final adjustment ensures 'i' points to the index of the largest element.
    # It handles cases where the array is fully sorted (no rotation break).
    if arr[i] <= arr[i + 1]:
        i += 1
        # Trace: arr[1] (15) <= arr[2] (6) is False. i remains 1.
        
    # --- Step 2: Initialize Two Pointers ---
    # The two-pointer search starts at the two elements adjacent to the rotation breakpoint.
    
    # l is now the index of the smallest element (at the pivot, just after the largest one).
    # Trace: l = (1 + 1) % 6 = 2. arr[l] = 6 (Smallest element)
    l = (i + 1) % n

    # r is now the index of the largest element.
    # Trace: r = 1. arr[r] = 15 (Largest element)
    r = i

    # --- Step 3: Two-Pointer Search (O(n)) ---
    # We move l (to increase sum) and r (to decrease sum) towards each other 
    # until they meet, checking all unique pairs.
    # 
    # Initial State: l=2 (value=6), r=1 (value=15)
    while l != r:

        # Case A: Pair Found
        # Trace Iteration 1: arr[l] + arr[r] = 6 + 15 = 21. 21 == 16? False. Proceed.
        # Trace Iteration 2: arr[l] + arr[r] = 6 + 11 = 17. 17 == 16? False. Proceed.
        # Trace Iteration 3: arr[l] + arr[r] = 6 + 10 = 16. 16 == 16? True. Return True.
        if arr[l] + arr[r] == target:
            return True

        # Case B: Sum is too low (Need a HIGHER sum)
        # Move the smaller pointer (l) forward to the next smallest element.
        if arr[l] + arr[r] < target:
            # The modulo operator (%) handles the wrap-around (e.g., moving from index 5 to 0).
            # Trace: This case not hit in example until possibly later, but for completeness:
            # If sum < target, l = (l + 1) % n
            l = (l + 1) % n

        # Case C: Sum is too high (Need a LOWER sum)
        # Move the larger pointer (r) backward to the next largest element.
        else:
            # Trace Iteration 1: 21 > 16, so move r backward.
            # r = (1 - 1 + 6) % 6 = 0. Now r=0 (value=11), l=2 (value=6)
            # Trace Iteration 2: 17 > 16, so move r backward.
            # r = (0 - 1 + 6) % 6 = 5. Now r=5 (value=10), l=2 (value=6)
            # Trace Iteration 3: 16 == 16, skipped to return.
            # The addition of 'n' handles negative results from (r - 1) when r=0, 
            # ensuring the modulo always results in a valid positive index for wrap-around.
            r = (r - 1 + n) % n
            
    # If the pointers meet and no pair was found, return False
    # Trace: In this example, pair found in iteration 3, so this line not reached.
    return False
    


if __name__ == "__main__":
    print(f"Result1:{pairSumRotatedArr([11, 15, 6, 8, 9, 10],16)}")
    print(f"Result1:{pairSumRotatedArr([11, 11, 15, 26, 38, 9, 10], 35)}")
    print(f"Result1:{pairSumRotatedArr([9, 10, 10, 11, 15, 26, 38], 45)}")