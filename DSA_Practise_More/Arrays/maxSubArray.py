# You are given an integer array arr[]. You need to find the maximum sum of a subarray 
# (containing at least one element) in the array arr[].

# Note : A subarray is a continuous part of an array.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# -104 ≤ arr[i] ≤ 104


# ✅ Kadane’s Algorithm (Explanation)

# Idea:
# We traverse the array and keep track of:

# the current subarray sum (current_sum)

# the maximum subarray sum found so far (max_sum)

# At each step:

# Add the current element to current_sum.

# If current_sum becomes smaller than the current element, start a new subarray from the current element.

# Update max_sum whenever current_sum exceeds it.

class ArrayCal:
    def maxSubArray(self, arr, n):
        if not( 1 <= n <= 10**5):
            raise ValueError("\n Array size is out of constraint range. \n")
        
        if not any((-10**4 <= arr[x] <= 10**5) for x in range(n)):
            raise ValueError("\n Array element is out of constrain range. \n")
        
        max_subArray = arr[0]
        curr_subArray = arr[0]

        for i in range(1,n):
            # If the sum becomes negative, reset it to current element
            curr_subArray = max(arr[i], curr_subArray + arr[i])

            # Update global maximum
            max_subArray = max(max_subArray, curr_subArray)

        return max_subArray


if __name__ == '__main__':
    arr = [5, 4, 1, 7, 8]
    n = len(arr)

    arrObj = ArrayCal()
    res = arrObj.maxSubArray(arr,n) 
    print("result",res)