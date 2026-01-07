# Create a matrix with alternating rectangles of O and X

# Write a code which inputs two numbers m and n and creates a matrix of size m x n (m rows and n columns) 
# in which every elements is either X or 0. The Xs and 0s must be filled alternatively, the matrix should 
# have outermost rectangle of Xs, then a rectangle of 0s, then a rectangle of Xs, and so on.

# Examples:  

# Input: m = 3, n = 3
# Output: Following matrix 
# X X X
# X 0 X
# X X X

# Input: m = 4, n = 5
# Output: Following matrix
# X X X X X
# X 0 0 0 X
# X 0 0 0 X
# X X X X X

# Input:  m = 5, n = 5
# Output: Following matrix
# X X X X X
# X 0 0 0 X
# X 0 X 0 X
# X 0 0 0 X
# X X X X X

# Input:  m = 6, n = 7
# Output: Following matrix
# X X X X X X X
# X 0 0 0 0 0 X
# X 0 X X X 0 X
# X 0 X X X 0 X
# X 0 0 0 0 0 X
# X X X X X X X 

class solution:
    def print_alternate_x_O_spiral(self,last_row,last_col):
        start_row, start_col, i = 0, 0, 0
        r = last_row
        c = last_col

        last_row = last_row-1
        last_col = last_col-1

        mat = [[None for _ in range(c)] for _ in range(r)]

        X = "X"

        while start_row <= last_row and start_col <= last_col:

            for i in range(start_col, last_col+1):
                mat[start_row][i] = X
            start_row +=1

            for i in range(start_row, last_row+1):
                mat[i][last_col] = X
            last_col -=1

            if start_row <= last_row:
                for i in range(last_col,start_col-1, -1):
                    mat[last_row][i] = X
                last_row -=1

            if start_col <= last_col:
                for i in range(last_row, start_row-1, -1):
                    mat[i][start_col] = X
                start_col +=1

            X = "0" if X == 'X' else "X"
        
        for i in range(r):
            for j in range(c):
                print(mat[i][j], end =" ")
            print()


if __name__ == "__main__":

    s1 = solution()
    print("Output X and O for m = 3 and n = 3")
    s1.print_alternate_x_O_spiral(3,3)

    print("Output X and O for m = 4 and n = 5")
    s1.print_alternate_x_O_spiral(4,5)

    print("Output X and O for m = 5 and n = 5 ")
    s1.print_alternate_x_O_spiral(5,5)

    print("Output X and O for m = 6 and n = 7")
    s1.print_alternate_x_O_spiral(6,7)

