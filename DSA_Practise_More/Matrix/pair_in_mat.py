# Find a specific pair in Matrix

# Given an n x n matrix mat[n][n] of integers, find the maximum value of 
# mat(c, d) - mat(a, b) over all choices of indexes such that both c > a and d > b.

# Example: 

# Input:
# mat[N][N] = {{ 1, 2, -1, -4, -20 },
#              { -8, -3, 4, 2, 1 }, 
#              { 3, 8, 6, 1, 3 },
#              { -4, -1, 1, 7, -6 },
#              { 0, -4, 10, -5, 1 }};
# Output: 18

# The maximum value is 18 as mat[4][2] 
# - mat[1][0] = 18 has maximum difference. 

# The program should do only ONE traversal of the matrix. i.e. expected time complexity is O(n2)
# A simple solution would be to apply Brute-Force. For all values mat(a, b) in the matrix, we find 
# mat(c, d) that has maximum value such that c > a and d > b and keeps on updating maximum value 
# found so far. We finally return the maximum value.

def find_max_value(mat):
    N = len(mat)

    # temp1[j] = biggest value available
    # in rows BELOW current row, starting from column j
    temp1 = [0] * N

    # temp2[j] = same idea, but for CURRENT row
    temp2 = [0] * N

    # Start from bottom-right corner
    temp1[N - 1] = mat[N - 1][N - 1]

    # =================================================
    # STEP 1: Process LAST ROW
    # Example last row:
    # [ 0  -4  10  -5  1 ]
    #
    # Build max-from-right:
    # temp1 becomes:
    # [10, 10, 10, 1, 1]
    # =================================================
    for j in range(N - 2, -1, -1):
        temp1[j] = max(temp1[j + 1], mat[N - 1][j])

    # This stores final answer
    max_value = float("-inf")

    # =================================================
    # STEP 2: MAIN LOGIC (bottom → top, right → left)
    #
    # Idea:
    # At each cell (i, j):
    #   1) Look at biggest number strictly bottom-right
    #   2) Subtract current value
    #   3) Update answer
    # =================================================
    for i in range(N - 2, -1, -1):

        # ---------------------------------------------
        # Handle LAST COLUMN first
        #
        # Example (row 3):
        # mat[3][4] = -6
        # temp1[4]  = 1
        # temp2[4]  = max(1, -6) = 1
        # ---------------------------------------------
        temp2[N - 1] = max(temp1[N - 1], mat[i][N - 1])

        # ---------------------------------------------
        # Move RIGHT → LEFT
        # ---------------------------------------------
        for j in range(N - 2, -1, -1):

            # -----------------------------------------
            # CORE CHECK (with example)
            #
            # Example when i=3, j=0:
            # current cell = mat[3][0] = -4
            # best future  = temp1[1] = 10
            #
            # candidate = 10 - (-4) = 14
            #
            # Later when i=1, j=0:
            # current cell = -8
            # best future  = 10
            #
            # candidate = 10 - (-8) = 18  <-- FINAL ANSWER
            # -----------------------------------------
            max_value = max(max_value, temp1[j + 1] - mat[i][j])

            # -----------------------------------------
            # Update temp2[j]
            #
            # Meaning:
            # "What is the biggest number I can see
            #  from here or ahead?"
            #
            # Compare:
            # - current cell
            # - below (temp1[j])
            # - right (temp2[j+1])
            #
            # Example row 3 result:
            # temp2 becomes:
            # [10, 10, 10, 7, 1]
            # -----------------------------------------
            temp2[j] = max(
                mat[i][j],     # current cell
                temp1[j],      # below
                temp2[j + 1]   # right
            )

        # ---------------------------------------------
        # Row finished
        #
        # temp1 now represents:
        # "biggest values available BELOW next row"
        # ---------------------------------------------
        temp1 = temp2[:]

    return max_value


if __name__ == "__main__":
    mat1 = [
            [ 1, 2, -1, -4, -20],
            [-8, -3, 4, 2, 1],
            [ 3, 8, 6, 1, 3],
            [-4, -1, 1, 7, -6],
            [0, -4, 10, -5, 1]
        ]
    print(find_max_value(mat1))