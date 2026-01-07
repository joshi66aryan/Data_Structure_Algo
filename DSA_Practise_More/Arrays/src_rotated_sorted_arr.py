# Medium

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown 
# index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
# nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 
# 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of 
# target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

def src_rotated_arr(nums, target):
    """
    Find target in a rotated sorted array (all numbers are unique)
    
    Example: nums = [4,5,6,7,0,1,2], target = 0 → returns 4
                nums = [4,5,6,7,0,1,2], target = 3 → returns -1
    """
    left = 0                  # Start of search range
    right = len(nums) - 1     # End of search range
    
    while left <= right:      # Keep searching as long as range is valid
        mid = (left + right) // 2    # Find middle index
        
        # Example: nums = [4,5,6,7,0,1,2], first mid = 3 → nums[3] = 7
        if nums[mid] == target:
            return mid        # Found it! Return the index immediately
        
        # Step 1: Check which half is properly sorted
        
        if nums[left] <= nums[mid]:
            # Left half is sorted (from left → mid)
            # Example: [4,5,6,7] is sorted (4 ≤ 5 ≤ 6 ≤ 7)
            
            # Now check: is target in this sorted left part?
            if nums[left] <= target < nums[mid]:
                # Yes! Target is between nums[left] and nums[mid]
                # Example: target=5 → 4 ≤ 5 < 7 → Yes → search only left side
                right = mid - 1
            else:
                # No → target must be in the right half
                # Example: target=1 → 4 ≤ 1 < 7? No → go right
                left = mid + 1
        else:
            # Right half is sorted (from mid → right)
            # Example: when mid=3 (7), right half is [0,1,2] → not sorted yet
            # But when mid=5 (nums[5]=1), right half [1,2] is sorted
            
            # Check: is target in the sorted right part?
            if nums[mid] < target <= nums[right]:
                # Yes! Target is between nums[mid] and nums[right]
                # Example: target=2, mid=5 (1), right=6 (2) → 1 < 2 ≤ 2 → Yes
                left = mid + 1
            else:
                # No → target must be in left half
                right = mid - 1
    
    # If we exit the loop → target not found
    return -1


if __name__ == "__main__":
    print(f"Result1: {src_rotated_arr([4,5,6,7,0,1,2], 0)}")
    print(f"Result1: {src_rotated_arr( [4,5,6,7,0,1,2], 3)}")
    print(f"Result1: {src_rotated_arr([1], 0)}")
