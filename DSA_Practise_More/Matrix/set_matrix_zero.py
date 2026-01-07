# Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:

# Input: 

# matrix = [
#     [1,1,1],
#     [1,0,1],
#     [1,1,1]
# ]

# Output: [
#     [1,0,1],
#     [0,0,0],
#     [1,0,1]
# ]

# Example 2:
# Input: 
# matrix = [
#     [0,1,2,0],
#     [3,4,5,2],
#     [1,3,1,5]
# ]
# Output: [
#     [0,0,0,0],
#     [0,4,5,0],
#     [0,3,1,0]
# ]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.

def row_col_zero(mat):
    n = len(mat)          # Number of rows
    m = len(mat[0])       # Number of columns
    c0 = 1                # Flag to track if the FIRST COLUMN should be set to zero
                          # We use a separate variable because mat[0][0] is shared
                          # between first row and first column marking
    
    # Step 1: Traverse the entire matrix to find all zeros
    # When we find a zero at mat[i][j], we mark:
    #   - The first cell of its row: mat[i][0] = 0  (indicates row i should be zeroed)
    #   - The first cell of its column: mat[0][j] = 0  (indicates column j should be zeroed)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                # Mark the row by setting first element of this row to 0
                mat[i][0] = 0
                
                # Mark the column
                if j == 0:
                    # If zero is in first column, we cannot use mat[0][0] reliably
                    # So we use separate flag 'c0'
                    c0 = 0
                else:
                    # For other columns, safely mark top cell
                    mat[0][j] = 0
    
    # Step 2: Now use the markings to set internal elements (from row 1, col 1) to zero
    # We start from (1,1) to avoid overwriting our markers prematurely
    for i in range(1, n):
        for j in range(1, m):
            # If either the row or column was marked (has a zero somewhere),
            # set this cell to zero
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    
    # Step 3: Handle the first row separately
    # If there was a zero anywhere in the first row, mat[0][0] would have been set to 0
    # So if mat[0][0] == 0 → entire first row should be zero
    if mat[0][0] == 0:
        for j in range(m):
            mat[0][j] = 0
    
    # Step 4: Handle the first column separately
    # We use the flag c0 (set to 0 if there was any zero in column 0)
    if c0 == 0:
        for i in range(n):
            mat[i][0] = 0

    return mat


if __name__ == "__main__":
    mat1 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]

    mat2 = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]

    res1 = row_col_zero(mat1)
    res2 = row_col_zero(mat2)

    print("Result1:", res1)
    print("Result2:", res2)
