
# Given a matrix of ‘O’ and ‘X’ if surrounded by 'X'

# Given a matrix grid[ ][ ] where each cell contains either 'O' or 'X'. We have to replace all the ‘O’s with ‘X’s 
# if they are surrounded by ‘X’s on all sides. An 'O' is considered surrounded if it cannot reach the boundary of 
# the matrix by moving up, down, left, or right through adjacent 'O' cells.

# Examples: 

# Input: grid[][] =  [
#           ['X', 'O', 'X', 'X', 'X', 'X'], 
#           ['X', 'O', 'X', 'X', 'O', 'X'],
#           ['X', 'X', 'X', 'O', 'O', 'X'],
#           ['O', 'X', 'X', 'X', 'X', 'X'],
#           ['X', 'X', 'X', 'O', 'X', 'O'],
#           ['O', 'O', 'X', 'O', 'O', 'O']]

# Output:  
# [
#   ['X', 'O', 'X', 'X', 'X', 'X'],
#   ['X', 'O', 'X', 'X', 'X', 'X'],
#   ['X', 'X', 'X', 'X', 'X', 'X'],
#   ['O', 'X', 'X', 'X', 'X', 'X'],
#   ['X', 'X', 'X', 'O', 'X', 'O'],
#   ['O', 'O', 'X', 'O', 'O', 'O']
# ]

# Explanation: The 'O's at positions (1,4), (2,3), and (2,4) are completely surrounded by 'X' on all sides, so 
# they are replaced with 'X'. All other 'O's remain unchanged because they are connected to the boundary ‘O’s,


# Input: grid[][] =  [
# ['X', 'X', 'X', 'X']
# ['X', 'O', 'X', 'X']
# ['X', 'O', 'O', 'X']
# ['X', 'O', 'X', 'X']
# ['X', 'X', 'O', 'O']
#]

# Output:  [['X', 'X', 'X', 'X']
#                   ['X', 'X', 'X', 'X']
#                   ['X', 'X', 'X', 'X']
#                   ['X', 'X', 'X', 'X']
#                   ['X', 'X', 'O', 'O']]              

# Explanation: The 'O's at positions (1,1), (2,1), (2,2), (3,1) is fully surrounded by 'X' and is converted 
# to 'X'; the 'O's at (4,2) and (4,3) remain because they touch the matrix boundary.   

from typing import List
class solution:
    def fillUtils(self, Grid, x, y, prevV, newV):

        n, m = len(Grid), len(Grid[0])

        if x < 0 or x >= n or y < 0 or y >= m:
            return
        
        if Grid[x][y] != prevV:
            return 

        Grid[x][y] = newV

        self.fillUtils(Grid, x+1, y, prevV, newV)
        self.fillUtils(Grid, x-1, y, prevV, newV)
        self.fillUtils(Grid, x, y+1, prevV, newV)
        self.fillUtils(Grid, x, y-1, prevV, newV)


    def flood_fill(self, Grid:List[List[str]]):
        n, m = len(Grid), len(Grid[0])

        # fill all the O with -
        for i in range(n):
            for j in range(m):
                if Grid[i][j] == "O":
                    Grid[i][j] = "-"
            
        # fill col edge back to O
        for i in range(n):
            for j in range(m):
                if Grid[i][0] == "-":
                    self.fillUtils(Grid, i, 0,"-", "O" )
                if Grid[i][m-1] == "-":
                    self.fillUtils(Grid, i, m-1, "-", "O")
                    
        # fill rows edge back to O
        for i in range(n):
            for j in range(m):
                if Grid[0][j] == "-":
                    self.fillUtils(Grid, 0, j, "-", "O")
                if Grid[n-1][j] == "-":
                    self.fillUtils(Grid, n-1, j, "-", "O")
                    

        # at last replace remaining  - with X
        for i in range(n):
            for j in range(m):
                if Grid[i][j] == "-":
                    Grid[i][j] = 'X'
        
        return Grid





if __name__ == "__main__":
    grid1 =  [
        ['X', 'O', 'X', 'X', 'X', 'X'], 
        ['X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O']
    ]

    grid2 =  [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O']
    ]

    s1 = solution()
    res1 = s1.flood_fill(grid1)
    res2 = s1.flood_fill(grid2)
    
    for x in res1:
        print(''.join(x))

    for x in res2:
        print(''.join(x))
