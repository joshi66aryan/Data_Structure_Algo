#  Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of 
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next 
# lexicographically greater permutation of its integer. More formally, 
# if all the permutations of the array are sorted in one container according 
# to their lexicographical order, then the next permutation of that array is 
# the permutation that follows it in the sorted container. If such arrangement 
# is not possible, the array must be rearranged as the lowest possible order (
# i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] 
# does not have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100



def nextPermutation(nums):
    """
    Rearranges numbers into the next lexicographically greater permutation.
    If not possible (array is in descending order), rearranges into ascending order.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    n = len(nums)  # total elements in nums

    # STEP 1️⃣: Find the first decreasing element from the right
    # ----------------------------------------------------------
    # Start from second-last index and move left.
    # The goal: find 'i' where nums[i] < nums[i + 1].
    # This means nums[i] is the "pivot" that can be increased.
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1  # keep moving left while the sequence is non-increasing

    # STEP 2️⃣: If such a pivot is found, find the element just larger than nums[i]
    # ---------------------------------------------------------------------------
    # We now look from the end to find 'j' where nums[j] > nums[i].
    # That will be the next greater element to swap with pivot.
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1  # move left until we find element greater than nums[i]
        # Swap the two elements
        nums[i], nums[j] = nums[j], nums[i]

    # STEP 3️⃣: Reverse the elements after the pivot index (i + 1 to end)
    # -------------------------------------------------------------------
    # The suffix after position i was originally in descending order.
    # Reversing it will make it ascending — the smallest possible order.
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # At this point, nums has been rearranged in-place to the next permutation.




if __name__ == '__main__':
    nums = [1, 2, 3,6,5,4]    
    print(nextPermutation(nums)) 

