# Find Minimum in Rotated Sorted Array
# Medium

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, 
# the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

def findMin(nums):
    """
    Finds the minimum element in a rotated sorted array using Binary Search in O(log n) time.
    The minimum element is the pivot point where the sorting order breaks.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    --- Example Trace: nums = [4, 5, 6, 7, 0, 1, 2] ---
    """
    
    low, high = 0, len(nums) - 1
    # Initial State: low = 0, high = 6
    # nums: [4, 5, 6, 7, 0, 1, 2]
    
    # If the array is fully sorted (not rotated, or rotated n times), return the first element.
    if nums[low] <= nums[high]:
        return nums[low]
        # Trace: nums[0] (4) <= nums[6] (2) is False. Continue to loop.
        
    # Search for the rotation point
    while low < high:
        
        # --- Iteration Log ---
        # 1. low=0, high=6. mid=3. nums[mid]=7. nums[high]=2.
        # 2. low=4, high=6. mid=5. nums[mid]=1. nums[high]=2.
        # 3. low=4, high=5. mid=4. nums[mid]=0. nums[high]=1.
        mid = (low + high) // 2
        
        # --- The Key Decision ---
        
        # Case 1: nums[mid] is greater than nums[high]. (We are in the larger segment of the array)
        # This means the pivot (minimum) MUST be in the right half (mid + 1 to high).
        if nums[mid] > nums[high]:
            # Trace 1: 7 > 2 is True. The minimum is in [0, 1, 2].
            # Discard mid and the left segment, search the right side.
            low = mid + 1 # Trace 1: low becomes 4
            
        # Case 2: nums[mid] is less than nums[high]. (We are in the sorted segment containing the minimum)
        # The minimum is either nums[mid] OR somewhere in the left half.
        else:
            # Trace 2: 1 > 2 is False. The minimum is in [0] or to its left.
            # Trace 3: 0 > 1 is False. The minimum is 0 or to its left.
            # We keep mid as a possible minimum but discard the right segment.
            high = mid # Trace 2: high becomes 5. Trace 3: high becomes 4
            
    # When low == high, we have converged on the minimum element.
    # Trace: low = 4, high = 4.
    return nums[low] # Returns nums[4] which is 0.



    


if __name__ == "__main__":
    print(f"Result1:{findMin([3,4,5,1,2])}")
    print(f"Result1:{findMin([4,5,6,7,0,1,2])}")
    print(f"Result1:{findMin([11,13,15,17])}")