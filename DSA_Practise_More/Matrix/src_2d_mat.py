# Search element in a sorted matrix

# Given a sorted matrix mat[][] of size n × m and an integer x, determine whether x is present in the matrix.
# The matrix is sorted in the following way:

# Each row is sorted in increasing order.
# The first element of each row is greater than or equal to the last element of the previous row
# (i.e., mat[i][0] ≥ mat[i−1][m−1] for all 1 ≤ i < n).
# Examples:

# Input: x = 14, mat[][] = [[ 1,  5,  9],
#                                         [14, 20, 21],
#                                         [30, 34, 43]]
# Output: true
# Explanation: The value 14 is present in the second row, first column of the matrix.

# Input: x = 42, mat[][] = [[ 1,  5,  9,  11],
#                                          [14, 20, 21, 26],
#                                         [30, 34, 43, 50]]
# Output: false
# Explanation: The value 42 does not appear in the matrix. 


## This can be done in naive way by linear search in 2d. --> O(mn) time complexity, O(1) space complexity.

## another way is binary search, other  ---> O(log m + log n) time complexity, O(1) space complexity.


def binarySearch(arr, x):
    low = 0 
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2

        if x == arr[mid]:
            return True
        elif x < mid:
            high = mid - 1
        else:
            low = mid + 1

    return False

def searchMatrix(mat, x):
    m,n = len(mat), len(mat[0])
    low = 0 
    high = m-1
    row = -1

    while low <= high:

        mid  = (low + high) // 2

        if x == mat[mid][0]:
            return True
        elif x > mat[mid][0]:
            row = mid
            low = mid + 1
        else:
            high = mid - 1
    
    if row == -1:
        return False
    
    return binarySearch(mat[row], x)





if __name__ == "__main__":
    mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    print(searchMatrix(mat, 14))
    print(searchMatrix(mat, 144))
    print(searchMatrix(mat, 12))
