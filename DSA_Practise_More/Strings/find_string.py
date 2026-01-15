# Find the string in grid
# Difficulty: Medium
# Given a 2D grid of n*m of characters and a word, find all occurrences of given word in grid. 
# A word can be matched in all 8 directions at any point. Word is said to be found in a direction 
# if all characters match in this direction (not in zig-zag form). The 8 directions are, horizontally 
# left, horizontally right, vertically up, vertically down, and 4 diagonal directions.

# Note: The returning list should be lexicographically smallest. If the word can be found in multiple
# directions starting from the same coordinates, the list should contain the coordinates only once. 

# Example 1:

# Input: 
# grid = {{a,b,c},{d,r,f},{g,h,i}},
# word = "abc"
# Output: 
# {{0,0}}

# Explanation: 
# From (0,0) we can find "abc" in horizontally right direction.

# Example 2:

# Input: 
# grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
# word = "abe"
# Output: 
# {{0,0},{0,2},{1,0}}

# Explanation: 
# From (0,0) we can find "abe" in right-down diagonal. 
# From (0,2) we can find "abe" in left-down diagonal. 
# From (1,0) we can find "abe" in horizontally right direction.

# Your Task:
# You don't need to read or print anything, Your task is to complete the function searchWord() 
# which takes grid and word as input parameters and returns a list containing the positions 
# from where the word originates in any direction. If there is no such position then returns 
# an empty list.

# Expected Time Complexity: O(n*m*k) where k is constant
# Expected Space Complexity: O(1)

# Constraints:
# 1 <= n <= m <= 50
# 1 <= |word| <= 15

from typing import List
class Solution:
    def search2D(self, grid, row, col, word):
        n, m  = len(grid), len(grid[0])

        if grid[row][col] != word[0]:
            return False
        
        lenWord = len(word)

        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        y = [-1, 0, 1, -1, 1, -1, 0, 1]

        for dir in range(8):
            currX, currY = row+x[dir], col+y[dir]
            k = 1

            while k < lenWord:
                # boundry check
                if currX >= n or currX < 0 or currY >= m or currY<0:
                    break
                
                if grid[currX][currY] != word[k]:
                    break

                currX += x[dir]
                currY += y[dir] 
                k+=1

            if  k == lenWord:
                return True
        
        return False




        
    def searchWord(self, word:str, grid: List[List[str]]):
        n, m = len(grid),len(grid[0])
        ans = []

        for i in range(n):
            for j in range(m):
                if self.search2D(grid, i, j, word):
                    ans.append((i,j))
        return ans

if __name__ == "__main__":
    s = Solution()
    print(f"Result1:{s.searchWord("abc",[['a','b','c'],['d','r','f'],['g','h','i']] )}")
    print(f"Result2:{s.searchWord("abe",[['a','b','a', 'b'],['a','b','e', 'b'],['e','b','e', 'b']] )}")
