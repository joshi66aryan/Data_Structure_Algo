# 79. Word Search -- Medium

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15

from typing import List

class solution:
    def exist(self, board:List[List[str]] , word:str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r,c,index):
            if index == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]):
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r+1,c,index+1) or
                dfs(r-1,c,index+1) or
                dfs(r,c+1,index+1) or
                dfs(r,c-1,index+1)
                )
            
            board[r][c] = temp
            return found


        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
        


if __name__ == "__main__":
    s1 = solution()
    print(s1.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "ABCCED"))
    print(s1.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "SEE"))
    print(s1.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "ABCB"))