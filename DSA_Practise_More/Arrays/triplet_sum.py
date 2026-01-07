# Triplet Sum in Array
# Difficulty: Medium

# Given an array arr[] and an integer target, determine if there exists a triplet 
# in the array whose sum equals the given target.

# Return true if such a triplet exists, otherwise, return false.

# Examples: 

# Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
# Output: true 
# Explanation: The triplet {1, 4, 8} sums up to 13.

# Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
# Output: true 
# Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10. 

# Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
# Output: false 
# Explanation: No triplet in the array sums to 24.

# Constraints:

# 3 ≤ arr.size() ≤ 5*103
# 0 ≤ arr[i], target ≤ 105


def triplet_sum(arr, target):
    # Step 1: Sort the array to apply the two-pointer technique
    arr.sort()

    # Step 2: Fix one element and use two pointers for the remaining sum
    for i in range(len(arr) - 2):
        # Two pointers: one at i+1 and one at end
        left = i + 1
        right = len(arr) - 1

        # While left and right do not cross each other
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            # -------------------------
            # Example iteration comment:
            # If arr = [1,4,6,8,10,45] and target = 13
            # i=0 → arr[i]=1
            # left=1 → arr[left]=4
            # right=3 → arr[right]=8
            # current_sum = 1+4+8 = 13 → Found!
            # -------------------------

            if current_sum == target:
                return True       # Triplet found

            elif current_sum < target:
                left += 1         # Need a larger sum → move left forward
            
            else:
                right -= 1        # Need a smaller sum → move right backward

    return False  # No such triplet exists


    


if __name__ == '__main__':
    print(triplet_sum([1, 4, 45, 6, 10, 8], 13))
    print(triplet_sum([1, 2, 4, 3, 6, 7], 10))
    print(triplet_sum([40, 20, 10, 3, 6, 7], 24))