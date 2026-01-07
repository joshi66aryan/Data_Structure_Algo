# Diagonal Traversal of a Matrix I

# Given a 2D matrix of size n*m, the tasks is to print all elements of the given matrix in diagonal order.

# Example:

# Input: mat[][] = 
# [
#   [1, 2, 3, 4 ],
#   [5, 6, 7, 8 ],
#   [9, 10, 11, 12],
#   [13, 14, 15, 16],
#   [17, 18, 19, 20]
# ]
# Output: 1 5 2 9 6 3 13 10 7 4 17 14 11 8 18 15 12 19 16 20 

# Diagonal-Traversal-of-a-Matrix-2
 
# Using Line by Line Diagonal Traversal - O(n*m) time and O(n*m) space
# The idea is to traverse the matrix diagonally from bottom-left to top-right, 
# one diagonal at a time. Since a matrix with R rows and C columns has exactly R+C-1 diagonals,
# we iterate through each diagonal line and identify the starting position, number of elements,
# and the indices of elements belonging to that diagonal, collecting them in sequence to produce 
# the desired diagonal ordering.

def diagonal_traversal(mat):
    n = len(mat)
    m = len(mat[0])
    res = []

    for row in range(n):
        i = row
        j = 0

        while i >= 0 and  j < m:
            res.append(mat[i][j])
            i-=1
            j+=1
    
    for col in range(1,m):
        i = n - 1
        j = col

        while i >= 0 and j < m: 
            res.append(mat[i][j])
            i-=1
            j+=1
            
    return res



if __name__ == "__main__":
    mat1 = [[ 1, 2, 3, 4 ], [5, 6, 7, 8 ], [9, 10, 11, 12], [13, 14, 15, 16],[17, 18, 19, 20]]
    result = diagonal_traversal(mat1)
    for n in result:
        print(n, end = " ")
    print()
    
