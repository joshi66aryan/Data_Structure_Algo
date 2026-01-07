# Number of Islands

# Given an n × m grid[][] consisting of 'L' (land) and 'W' (water), we need to count the total number of islands 
# present in the grid without modifying the original grid. An island is defined as a group of connected 'L' cells 
# that are adjacent horizontally, vertically, or diagonally, and surrounded by water or the boundary of the grid.

# Examples:

# Input: grid[][] = [['L', 'L', 'W', 'W', 'W'],
#                             ['W', 'L', 'W', 'W', 'L'],
#                            ['L', 'W', 'W', 'L', 'L'],
#                           ['W', 'W', 'W', 'W', 'W'],
#                          ['L', 'W', 'L', 'L', 'W']]
# Output: 4
# Explanation: The image below shows all the 4 islands.


# Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'],
#                             ['W', 'W', 'L', 'L', 'W', 'L', 'W']]                         
# Output: 2
# Explanation: The image below shows all the 2 islands in the graph
# http://geeksforgeeks.org/dsa/find-the-number-of-islands-using-dfs/


from typing import List
class solution:
    def isSafe(self, grid, r, c, visited):
        n = len(grid)        # number of rows
        m = len(grid[0])     # number of columns
        
        # Is it okay to step on this cell?
        return (0 <= r < n and 0 <= c < m          # inside the grid?
                and grid[r][c] == 'L'              # is it land?
                and not visited[r][c])             # haven't visited it yet?


    def dfs(self, grid, r, c, visited):
        visited[r][c] = True    # "I was here!" (mark as visited)
    
        # These are all 8 possible directions you can move:
        # ↑ ↖ ← ↙ ↓ ↘ → ↗
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1,  0,  1,-1, 1,-1, 0, 1]

        for k in range(8):
            nr = r + dr[k]    # new row
            nc = c + dc[k]    # new column
            
            # If the neighbor is safe (land + not visited) → explore it too!
            if self.isSafe(grid, nr, nc, visited):
                self.dfs(grid, nr, nc, visited)   # recursive call = magic!
        

    def find_no_of_island(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
                return 0
                
        n = len(grid)
        m = len(grid[0])
        
        # Create a "visited" map, initially all False
        visited = [[False] * m for _ in range(n)]
        
        islands = 0
        
        # Look at EVERY cell in the grid
        for i in range(n):
            for j in range(m):
                # Found new land that nobody visited yet?
                if grid[i][j] == 'L' and not visited[i][j]:
                    # Start exploring (painting) the whole island
                    self.dfs(grid, i, j, visited)
                    # We finished one complete island
                    islands += 1
                
        return islands
            
    

if __name__ == "__main__":
    grid1 = [
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
    ]
    
    grid2 = [
        ['W', 'L', 'L', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'W', 'L', 'W']
    ]   

    s1 = solution()
    print(s1.find_no_of_island(grid1))
    print(s1.find_no_of_island(grid2))