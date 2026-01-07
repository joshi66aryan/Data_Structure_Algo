# Max rectangle

# Difficulty: HardAccuracy

# You are given a 2D binary matrix mat[ ][ ], where each cell contains either 0 or 1. 
# Your task is to find the maximum area of a rectangle that can be formed using only 
# 1's within the matrix.

# Examples:

# Input: mat[][] = [[0, 1, 1, 0],
#                 [1, 1, 1, 1],
#                 [1, 1, 1, 1],
#                 [1, 1, 0, 0]]
# Output: 8
# Explanation: The largest rectangle with only 1’s is from (1, 0) to (2, 3) which is
# [1, 1, 1, 1]
# [1, 1, 1, 1]
# and area is 4 * 2 = 8.


# Input: mat[][] = [[0, 1, 1],
#                 [1, 1, 1],
#                 [0, 1, 1]]
# Output: 6
# Explanation: The largest rectangle with only 1’s is from (0, 1) to (2, 2) which is
# [1, 1]
# [1, 1]
# [1, 1]
# and area is 2 * 3 = 6.


# Constraints:
# 1 ≤ mat.size(), mat[0].size() ≤1000
# 0 ≤ mat[][] ≤1

# Expected Complexities
# Time Complexity: O(n * m)
# Auxiliary Space: O(m)

def maxArea(mat):
    # Get the number of rows (n) and columns (m) in the matrix
    n, m = len(mat), len(mat[0])
    
    # Create a 2D list 'memo' to store, for each cell, 
    # how many consecutive 1's are there to the left (including itself)
    # Example: if row is [1,1,1], memo becomes [1,2,3]
    memo = [[0] * m for _ in range(n)]
    
    # This will store the largest rectangle area we find
    ans = 0
    
    # Loop through every row from top to bottom
    for i in range(n):
        # Loop through every column in the current row
        for j in range(m):
            # If this cell is 0, we skip it (can't be part of any rectangle)
            if mat[i][j] == 0:
                continue
            
            # Calculate how wide the streak of 1's is in this row ending at column j
            # If it's the first column (j==0), width is 1 if mat[i][j]==1
            # Otherwise, add 1 to the width from the left cell
            memo[i][j] = 1 if j == 0 else memo[i][j - 1] + 1
            
            # Current possible width at the bottom row (row i) for column j
            width = memo[i][j]
            
            # Now go upwards from current row i all the way to row 0
            # For each possible height, calculate the maximum rectangle ending at (i,j)
            for k in range(i, -1, -1):  # k goes from i up to 0 (upwards)
                # As we go up, the width can't be larger than what the upper row allows
                # So we take the minimum width seen so far in this column
                width = min(width, memo[k][j])
                
                # Height of current rectangle = number of rows from k to i
                height = i - k + 1
                
                # Area = width × height
                area = width * height
                
                # Update the maximum area found so far
                ans = max(ans, area)
    
    # Return the largest rectangle area of 1's found
    return ans

             

if __name__ == "__main__":
    mat1 =  [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 0, 0]]
    mat2 = [[0, 1, 1],[1, 1, 1],[0, 1, 1]]

    print("Output1:",maxArea(mat1))
    print("Output2:",maxArea(mat2))