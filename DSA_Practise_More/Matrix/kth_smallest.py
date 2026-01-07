
# Kth smallest element in a Matrix

# Difficulty: Medium

# Given a matrix mat[][] of size n*n, where each row and column is sorted in non-decreasing order. 
# Find the kth smallest element in the matrix.


# Examples:
# Input: mat[][] = [[16, 28, 60, 64], k = 3
#                 [22, 41, 63, 91],
#                 [27, 50, 87, 93],
#                 [36, 78, 87, 94]]
# Output: 27


# Explanation: 27 is the 3rd smallest element.
# Input: mat[][] = [[10, 20, 30, 40], k = 7
#                 [15, 25, 35, 45],
#                 [24, 29, 37, 48],
#                 [32, 33, 39, 50]] 
# Output: 30
# Explanation: 30 is the 7th smallest element.


# Constraints:
# 1 ≤ n ≤ 500
# 1 ≤ mat[i][j] ≤ 104
# 1 ≤ k ≤ n*n

# Expected Complexities
# Time Complexity: O(n × log(max(mat) - min(mat)))
# Auxiliary Space: O(1)

# Function to count how many elements in the sorted 2D matrix are <= x
# The matrix is row-wise and column-wise sorted (young tableau property)
def countSmallestEqual(mat, x):
    n = len(mat)                    # Size of the square matrix (n x n)
    count = 0                       # Total count of elements <= x
    row = 0                         # Start from the top row
    col = n - 1                     # Start from the rightmost column (top-right corner)
    
    # Traverse the matrix starting from top-right corner
    # This direction allows us to efficiently eliminate rows or columns
    while row < n and col >= 0:
        if mat[row][col] <= x:
            # Current element is <= x
            # Since each row is sorted ascending left-to-right,
            # ALL elements from column 0 to col in the current row are <= mat[row][col]
            # Hence, they are all <= x
            count += (col + 1)      # Add (col + 1) elements from this row
            row += 1                # Move down to the next row (check if more rows qualify)
        else:
            # Current element > x
            # Since the column is sorted ascending top-to-bottom,
            # all elements below in this column are even larger
            # So we can safely ignore this entire column for value x
            col -= 1                # Move left to previous column
    
    return count                    # Return total count of elements <= x


# Function to find the kth smallest element in a row-wise and column-wise sorted matrix
def kth_smallest_in_mat(mat, k ):
    n = len(mat)
    low = mat[0][0]                 # Smallest possible value in matrix
    high = mat[n - 1][n - 1]        # Largest possible value in matrix
    ans = 0                         # Will store the kth smallest element
    
    # Binary search on the possible value range [low, high]
    while low <= high:
        mid = low + (high - low) // 2   # Candidate value for kth smallest
        
        # Count how many elements are <= mid
        count = countSmallestEqual(mat, mid)
        
        if count < k:
            # Fewer than k elements are <= mid
            # Means the kth smallest must be strictly larger than mid
            low = mid + 1
        else:
            # At least k elements are <= mid
            # So mid is a possible candidate for kth smallest
            # There might be a smaller value that also has >= k elements <= it
            ans = mid               # Update answer to mid
            high = mid - 1          # Search in left half for smaller possible value
    
    return ans                      # ans holds the smallest value with at least k elements <= it

if __name__ == "__main__":
    mat1 = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
    mat2 = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]] 
    print("Results:",kth_smallest_in_mat(mat1,3))
    print("Results:",kth_smallest_in_mat(mat2,7))