# Common elements in all rows of a given matrix

# Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.

# Example: 

# Input:
# mat[4][5] = {{1, 2, 1, 4, 8},
#              {3, 7, 8, 5, 1},
#              {8, 7, 7, 3, 1},
#              {8, 1, 2, 7, 9},
#             };

# Output: 
# 1 8 or 8 1

# 8 and 1 are present in all rows.

# A simple solution is to consider every element and check if it is present in all rows. If present, then print it. 
# A better solution is to sort all rows in the matrix and use similar approach as discussed here. 
# Sorting will take O(mnlogn) time and finding common elements will take O(mn) time. So overall time 
# complexity of this solution is O(mnlogn)

# Can we do better than O(mnlogn)? 
# The idea is to use maps. We initially insert all elements of the first row in an map. For every 
# other element in remaining rows, we check if it is present in the map. If it is present in the 
# map and is not duplicated in current row, we increment count of the element in map by 1, else 
# we ignore the element. If the currently traversed row is the last row, we print the element if 
# it has appeared m-1 times before. 


# The time complexity of this solution is O(m * n) and we are doing only one traversal of the matrix.
# Auxiliary Space: O(N)


def common_element_in_row(mat):
    n = len(mat)
    m = len(mat[0])
    map = dict()

    for  j in range(m):
        map[mat[0][j]] = 1

    for i in range(1,n):
        for j in range(m):
            if (mat[i][j] in map.keys() and map[(mat[i][j])] == i):
                map[(mat[i][j])] = i + 1

                if i == n - 1:
                    print(mat[i][j], end = " ")  
                


if __name__ == "__main__":
    mat1 = [
        [1, 2, 1, 4, 8],
        [3, 7, 8, 5, 1],
        [8, 7, 7, 3, 1],
        [8, 1, 2, 7, 9]
        ]

    # mat2 = [
    #     [16, 28, 60, 64], 
    #     [22, 64, 63, 91], 
    #     [27, 50, 87, 93], 
    #     [36, 87, 87, 63]
    #     ]
    mat3 = [
       [1, 2, 1, 1, 8],
       [1, 7, 8, 5, 1],
       [8, 7, 1, 3, 1],
       [8, 1, 2, 7, 9]
       ]
    
    common_element_in_row(mat1)
    # common_element_in_row(mat2)
    common_element_in_row(mat3)