# Row with max 1s:

# You are given a 2D binary array arr[][] consisting of only 1s and 0s. 
# Each row of the array is sorted in non-decreasing order. Your task is 
# to find and return the index of the first row that contains the maximum 
# number of 1s. If no such row exists, return -1.

# Note:

# The array follows 0-based indexing.
# The number of rows and columns in the array are denoted by n and m respectively.


# Examples:

# Input: arr[][] = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
# Output: 2
# Explanation: Row 2 contains the most number of 1s (4 1s). Hence, the output is 2.

# Input: arr[][] = [[0,0], [1,1]]
# Output: 1
# Explanation: Row 1 contains the most number of 1s (2 1s). Hence, the output is 1.

# Input: arr[][] = [[0,0], [0,0]]
# Output: -1
# Explanation: No row contains any 1s, so the output is -1.

# Constraints:
# 1 ≤ arr.size(), arr[i].size() ≤ 103
# 0 ≤ arr[i][j] ≤ 1 

# Expected Complexities
# Time Complexity: O(n + m)
# Auxiliary Space: O(1)

def first_one(arr, low, high):
    ind = -1
    while low <= high:

        mid = (low + high) // 2
        if arr[mid] == 1:
            ind = mid  
            high = mid - 1
        else:
            low = mid + 1
    return ind

def rowWithMaxOnes(mat):

    rows = len(mat)
    cols = len(mat[0])
    max_row_index = 0 
    max = -1

    for i in range(rows):
        index_of_first_one = first_one(mat[i], 0, cols-1 )
        if index_of_first_one != -1 and cols - index_of_first_one > max:
            max = cols - index_of_first_one 
            max_row_index = i
    return max_row_index

if __name__ == "__main__":
    print(rowWithMaxOnes([[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]))
    print(rowWithMaxOnes([[0,0], [1,1]]))
    print(rowWithMaxOnes([[0,0], [0,0]]))