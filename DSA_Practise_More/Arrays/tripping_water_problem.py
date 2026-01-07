
# Trapping Rain Water
# Difficulty: Hard

# Given an array arr[] with non-negative integers representing the height of blocks. 
# If the width of each block is 1, compute how much water can be trapped between the 
# blocks during the rainy season. 

# Examples:

# Input: arr[] = [3, 0, 1, 0, 4, 0 2]
# Output: 10
# Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

# Input: arr[] = [3, 0, 2, 0, 4]
# Output: 7
# Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

# Input: arr[] = [1, 2, 3, 4]
# Output: 0
# Explanation: We cannot trap water as there is no height bound on both sides.

# Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
# Output: 9
# Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.

# Constraints:
# 1 < arr.size() < 105
# 0 < arr[i] < 103

# Expected Complexities

#     Time Complexity: O(n)
#     Auxiliary Space: O(1)


# <------------------------------------------------------------------------------------------------------------------->

# ✅ **1. Problem Explanation**

# You are given an array `arr[]`, where each value represents the **height of a block**.

# When it rains, water gets trapped **between** the blocks if:

# * There is a **taller block on the left**
# * There is a **taller block on the right**

# At every index `i`, the amount of water stored is:

# ```
# water[i] = min(max_left, max_right) – height[i]
# ```

# (but only if this value is positive)

# You must compute **total water trapped**.

# ---

# 🌧 **Intuition with Visual Understanding**

# For each index, imagine:

# * Look left → find tallest block
# * Look right → find tallest block
# * Water can fill only up to the **shorter** of these two boundaries
# * Subtract current height to get water stored at that index

# ---

# 🚀 **Optimal O(n) Two Pointer Technique**

# We avoid computing left-max and right-max arrays (which needs O(n) space).
# Instead:

# * Maintain two pointers: `left`, `right`
# * Track:

#   * `left_max`
#   * `right_max`
# * Move the pointer which has the **smaller boundary**, because it limits the water level.

# <------------------------------------------------------------------------------------------------------------------->



def trapping_water(arr):
    # Two pointers to scan from both sides
    left = 0
    right = len(arr) - 1

    # Track the maximum boundaries seen so far
    left_max = 0
    right_max = 0

    total_water = 0

    # ---------------------------------------------------------------------
    # Example used for step-by-step explanation:
    # arr = [3, 0, 2, 0, 4]
    #
    # We'll show key iterations in comments.
    # ---------------------------------------------------------------------

    while left <= right:

        # Whichever side has the smaller boundary determines the trapped water
        if arr[left] <= arr[right]:

            # If current height is greater than or equal to left_max,
            # update boundary.
            if arr[left] >= left_max:
                # Example iteration step:
                # i=0 → arr[0]=3; left_max becomes 3
                left_max = arr[left]
            else:
                # Water = left_max - arr[left]
                # Example:
                # i=1 → left_max=3, arr[1]=0 → water=3
                total_water += left_max - arr[left]

            left += 1

        else:   # arr[right] < arr[left]

            if arr[right] >= right_max:
                # Update right boundary
                right_max = arr[right]
            else:
                # Water = right_max - arr[right]
                total_water += right_max - arr[right]

            right -= 1

    return total_water


# ---------------------------------------------------------------------
# Example Walkthrough for arr = [3, 0, 2, 0, 4]
#
# left_max = 0, right_max = 0
#
# Iteration steps:
# 1. left=0, right=4 → 3 <= 4 → update left_max=3
# 2. left=1 → 0 < 3 → trap = 3 - 0 = 3
# 3. left=2 → 2 < 3 → trap = 3 - 2 = 1
# 4. left=3 → 0 < 3 → trap = 3 - 0 = 3
# 5. left=4 → 4 >= left_max → update left_max=4
#
# Total water = 3 + 1 + 3 = 7
# ---------------------------------------------------------------------



# ⏱ **Time & Space Complexity**
### **Time Complexity → O(n)**
### **Space Complexity → O(1)**



    





if __name__ == '__main__':
    print(trapping_water([ 3, 0, 1, 0, 4, 0, 2]))
    print(trapping_water([3, 0, 2, 0, 4]))
    print(trapping_water([1, 2, 3, 4]))
    print(trapping_water([2, 1, 5, 3, 1, 0, 4]))