# Minimum swaps and K together
# Difficulty: Medium

# Given an array arr and a number k. One can apply a swap operation on the array any 
# number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . 
# Find the minimum number of swaps required to bring all the numbers less than or equal 
# to k together, i.e. make them a contiguous subarray.

# Examples :

# Input: arr[] = [2, 1, 5, 6, 3], k = 3
# Output: 1
# Explanation: To bring elements 2, 1, 3 together, swap index 2 with 4 (0-based indexing),
#  i.e. element arr[2] = 5 with arr[4] = 3 such that final array will be- arr[] = [2, 1, 3, 6, 5]

# Input: arr[] = [2, 7, 9, 5, 8, 7, 4], k = 6 
# Output: 2 
# Explanation: To bring elements 2, 5, 4 together, swap index 0 with 2 (0-based indexing) and i
# index 4 with 6 (0-based indexing) such that final array will be- arr[] = [9, 7, 2, 5, 4, 7, 8]

# Input: arr[] = [2, 4, 5, 3, 6, 1, 8], k = 6 
# Output: 0

# Constraints:
    # 1 ≤ arr.size() ≤ 106
    # 1 ≤ arr[i] ≤ 106
    # 1 ≤ k ≤ 106



def min_swap_k(arr,k):
    # ----------------------------------------------------
    # STEP 1: Count how many elements are <= k ("good" elements)
    # Example: arr = [2,1,5,6,3], k=3
    # Good elements = 2, 1, 3  → count_good = 3
    # ----------------------------------------------------
    count_good = sum(1 for x in arr if x <= k)

    # If there are 0 or 1 good elements, they are already together → no swaps needed
    if count_good <= 1:
        return 0


    # ----------------------------------------------------
    # STEP 2: Count how many "bad" elements(>k) exist
    # IN THE FIRST WINDOW of size count_good
    #
    # Window size = count_good = 3
    # First window = arr[0:3] = [2, 1, 5]
    # Bad elements = 5 → bad = 1
    # ----------------------------------------------------
    bad = 0
    for i in range(count_good):
        if arr[i] > k:      # Check if element is bad
            bad += 1        # Example: arr[2] = 5, so bad = 1

    # Store minimum bad elements found so far
    min_bad = bad          # min_bad = 1 in example


    # ----------------------------------------------------
    # STEP 3: Slide window across the array from left to right
    # right pointer moves from index count_good → end
    #
    # SLIDE 1:
    #   old window: [2,1,5]
    #   new window: [1,5,6]
    #
    # SLIDE 2:
    #   old window: [1,5,6]
    #   new window: [5,6,3]
    # ----------------------------------------------------
    left = 0               # left pointer starts at 0

    for right in range(count_good, len(arr)):

        # ---------------------------
        # Remove outgoing element from window
        # SLIDE 1: outgoing = arr[0] = 2 (good) → no change
        # SLIDE 2: outgoing = arr[1] = 1 (good)
        # ---------------------------
        if arr[left] > k:
            bad -= 1       # decrease bad count if outgoing was bad

        # Move left pointer forward
        left += 1


        # ---------------------------
        # Add incoming element to window
        # SLIDE 1: incoming = arr[3] = 6 (bad) → bad becomes 2
        # SLIDE 2: incoming = arr[4] = 3 (good) → bad becomes 1
        # ---------------------------
        if arr[right] > k:
            bad += 1       # add to bad if incoming > k

        # Update min_bad with the smallest bad count found so far
        min_bad = min(min_bad, bad)
        # Example progression:
        # SLIDE 1: bad = 2 → min_bad stays 1
        # SLIDE 2: bad = 1 → min_bad = 1


    # --------------------------------------------------------
    # min_bad = minimum bad elements in any window
    # This equals minimum swaps required.
    #
    # Example final answer = 1
    # --------------------------------------------------------
    return min_bad



if __name__ == '__main__':
    print(min_swap_k([2, 1, 5, 6, 3],3))
    print(min_swap_k([2, 7, 9, 5, 8, 7, 4], 6))
    print(min_swap_k([2, 4, 5, 3, 6, 1, 8], 6))