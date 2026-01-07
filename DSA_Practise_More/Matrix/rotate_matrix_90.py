# Rotate an Image 90 Degree Clockwise

# Given a square matrix mat[][], turn it by 90 degrees in an clockwise 
# direction without using any extra space

# Examples: 

# Input: mat[][] = {{1, 2, 3},
#                              {4, 5, 6},
#                              {7, 8, 9}}
# Output: {{7, 4, 1}, 
#                 {8, 5, 2}, 
#                 {9, 6, 3}} 

# Input: mat[][] = {{1, 2, 3, 4},
#                              {5, 6, 7, 8}, 
#                              {9, 10, 11,12}
#                              {13, 14, 15, 16}} 
# Output: {{13, 9, 5, 1}, 
#                 {14, 10, 6, 2},
#                 {15, 11, 7, 3},
#                 {16, 12, 8, 4}


def Rotate_Matrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    
    for row in mat:
        row.reverse()
    
    return mat

if __name__ == "__main__":
    mat1 = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11,12], [13, 14, 15, 16]]
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Result1:",Rotate_Matrix(mat1))
    print("Result2:",Rotate_Matrix(mat2))