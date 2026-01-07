# Sorted matrix
# Given an NxN matrix Mat. Sort all elements of the matrix.

# Example 1:

# Input:
# N=4
# Mat=[[10,20,30,40],
# [15,25,35,45] 
# [27,29,37,48] 
# [32,33,39,50]]

# Output:
# 10 15 20 25 
# 27 29 30 32
# 33 35 37 39
# 40 45 48 50

# Explanation:
# Sorting the matrix gives this result.


# Example 2:

# Input:
# N=3
# Mat=[[1,5,3],[2,8,7],[4,6,9]]
# Output:
# 1 2 3 
# 4 5 6
# 7 8 9
# Explanation:
# Sorting the matrix gives this result.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the 
# function sortedMatrix() which takes the integer N and the matrix Mat as input 
# parameters and returns the sorted matrix.


# Expected Time Complexity: O(N^2LogN)
# Expected Auxillary Space: O(N^2)


# Constraints:
# 1 <= N <= 1000
# 1 <= Mat[i][j] <= 10^5




# Python3 implementation to sort a given matrix in strict increasing order
# (i.e., all elements sorted row-wise from left to right, top to bottom)

# Function to sort the matrix in-place using Bubble Sort
def sortMat(data, row, col):
    """
    Sorts a 2D matrix in ascending order by treating it as a 1D array.
    
    Args:
        data: 2D list (matrix) to be sorted
        row:  Number of rows in the matrix
        col:  Number of columns in the matrix
    """
   
    # Calculate total number of elements in the matrix
    size = row * col  # e.g., 3x3 matrix has 9 elements
   
    # Perform Bubble Sort on the flattened view of the matrix
    # Outer loop: repeat the process 'size' times (worst-case passes needed)
    for i in range(0, size):
        # Inner loop: compare adjacent elements in the flattened sequence
        # We go up to size-1 because we compare j with j+1
        for j in range(0, size - 1):
           
            # Convert 1D index 'j' to 2D coordinates (row, col)
            # Current element position:
            curr_row = j // col      # Integer division gives row index
            curr_col = j % col       # Modulo gives column index within row
            
            # Next adjacent element position (in row-major order):
            next_row = (j + 1) // col
            next_col = (j + 1) % col
           
            # Compare current element with next element
            if (data[curr_row][curr_col] > data[next_row][next_col]):
               
                # Swap the two elements if they are out of order
                temp = data[curr_row][curr_col]
                data[curr_row][curr_col] = data[next_row][next_col]
                data[next_row][next_col] = temp

# Function to print the matrix in a clean format
def printMat(mat, row, col):
    """
    Prints the 2D matrix row by row.
    
    Args:
        mat: 2D list (matrix) to print
        row: Number of rows
        col: Number of columns
    """
   
    # Loop through each row
    for i in range(row):
        # Loop through each column in the current row
        for j in range(col):
            print(mat[i][j], end=" ")  # Print element followed by space
        print()  # Move to next line after finishing a row

# Driver Code (Main execution block)
if __name__ == "__main__":
    # Sample 3x3 matrix (unsorted)
    mat = [ [5, 4, 7],
            [1, 3, 8],
            [2, 9, 6] ]
    
    # Get dimensions of the matrix
    row = len(mat)         # Number of rows = 3
    col = len(mat[0])      # Number of columns = 3 (assuming rectangular)
   
    # Call function to sort the matrix in ascending order
    sortMat(mat, row, col)
   
    # Print the sorted matrix
    print("Sorted Matrix:")
    printMat(mat, row, col)
    

