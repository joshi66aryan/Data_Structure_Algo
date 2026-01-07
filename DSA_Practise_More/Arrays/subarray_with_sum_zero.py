# Subarray with 0 sum

# Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. 
# Return true/false depending upon whether there is a subarray present with 0-sum or not. 

# Examples:

# Input: arr[] = [4, 2, -3, 1, 6]
# Output: true
# Explanation: 2, -3, 1 is the subarray with a sum of 0.

# Input: arr = [4, 2, 0, 1, 6]
# Output: true
# Explanation: 0 is one of the element in the array so there exist a subarray with sum 0.
    
# Input: arr = [1, 2, -1]
# Output: false

# Constraints:
# 1 <= arr.size <= 104
# -105 <= arr[i] <= 105

# Expected Complexities

# Time Complexity: O(n)
# Auxiliary Space: O(n)

def sub_array_sum_zero(arr):
    """
    Returns True if arr contains a (contiguous) subarray with sum 0,
    otherwise False.
    """
    if not arr:
        return False

    seen = set()          # stores prefix sums encountered so far
    cur_sum = 0
    seen.add(0)           # empty prefix has sum 0

    for num in arr:
        cur_sum += num

        if cur_sum in seen:      # repeated prefix → zero-sum subarray
            return True

        seen.add(cur_sum)

    return False
        

if __name__ == '__main__':
    arr = [3, -3]
    ans = sub_array_sum_zero(arr)
    print("The result:",ans)
    print(sub_array_sum_zero([4, 2, 0, 1, 6]))    # True
    print(sub_array_sum_zero([1, 2, -1]))