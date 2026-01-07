# Longest Common Subsequence (LCS) Algorithm
# A subsequence is a sequence that can be derived from another sequence 
# by deleting some or no elements without changing the order of remaining elements

# Function to find LCS of X[0..m-1] and Y[0..n-1] 
def LCS(X, Y, m, n, T): 
    """
    This function reconstructs the actual LCS string from the lookup table
    X, Y: input strings
    m, n: lengths of strings X and Y
    T: lookup table filled with LCS lengths
    """
    
    # Base case: if we have reached the end of either sequence 
    # return empty string since no more characters to compare
    if m == 0 or n == 0: 
        return str()  # Return empty string
  
    # If last characters of both strings match
    if X[m - 1] == Y[n - 1]: 
        # Since characters match, this character is part of LCS
        # Recursively find LCS of remaining parts and append current character
        # We move diagonally up-left in the table (reduce both m and n by 1)
        return LCS(X, Y, m - 1, n - 1, T) + X[m - 1] 
  
    # When last characters don't match, we need to decide which direction to go
    # We choose the direction that gave us the maximum LCS length
    
    # Check if moving up (excluding current char from X) gives better result
    # T[m-1][n] represents LCS length without current character of X
    if T[m - 1][n] > T[m][n - 1]: 
        # Move up: exclude current character of X, keep all of Y
        return LCS(X, Y, m - 1, n, T) 
    else: 
        # Move left: exclude current character of Y, keep all of X
        # T[m][n-1] represents LCS length without current character of Y
        return LCS(X, Y, m, n - 1, T) 
  
  
# Function to fill lookup table with LCS lengths
def LCSLength(X, Y, m, n, T): 
    """
    This function fills the lookup table T using dynamic programming
    T[i][j] will store length of LCS of X[0..i-1] and Y[0..j-1]
    """
    
    # Fill the lookup table in bottom-up manner (building solution from smaller subproblems)
    for i in range(1, m + 1):  # For each character in string X
        for j in range(1, n + 1):  # For each character in string Y
            
            # If current characters match (remember: i-1 and j-1 because table is 1-indexed)
            if X[i - 1] == Y[j - 1]: 
                # Add 1 to the LCS length of substrings without these characters
                # We add 1 because we found a matching character
                T[i][j] = T[i - 1][j - 1] + 1 
                
            # If current characters don't match
            else: 
                # Take the maximum of:
                # 1. LCS length excluding current character of X: T[i-1][j]
                # 2. LCS length excluding current character of Y: T[i][j-1]
                T[i][j] = max(T[i - 1][j], T[i][j - 1]) 
  
  
# Example execution
X = "ABCBDAB"  # First string
Y = "BDCABA"   # Second string
m = len(X)     # Length of first string = 7
n = len(Y)     # Length of second string = 6
  
# Create lookup table T with dimensions (m+1) x (n+1)
# Extra row and column for empty string cases (base cases)
# T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1] 
T = [[0 for x in range(n + 1)] for y in range(m + 1)] 

# WHY i-1 and j-1? INDEX OFFSET EXPLANATION:
# 
# String X = "ABCBDAB"  (indices: 0,1,2,3,4,5,6)
# String Y = "BDCABA"   (indices: 0,1,2,3,4,5)
#
# Table has extra row/column for empty string:
#
# Table indices:  i=0  i=1  i=2  i=3  i=4  i=5  i=6  i=7
#                 ""   A    B    C    B    D    A    B
#      j=0  ""    0    0    0    0    0    0    0    0
#      j=1  B     0    ?    ?    ?    ?    ?    ?    ?
#      j=2  D     0    ?    ?    ?    ?    ?    ?    ?
#      j=3  C     0    ?    ?    ?    ?    ?    ?    ?
#      j=4  A     0    ?    ?    ?    ?    ?    ?    ?
#      j=5  B     0    ?    ?    ?    ?    ?    ?    ?
#      j=6  A     0    ?    ?    ?    ?    ?    ?    ?
#
# When i=1, j=1: We're comparing X[0] with Y[0] → X[i-1] with Y[j-1]
# When i=2, j=3: We're comparing X[1] with Y[2] → X[i-1] with Y[j-1]
#
# The table is 1-indexed, but strings are 0-indexed!

# The table initially looks like:
#     ""  B  D  C  A  B  A
# ""   0  0  0  0  0  0  0
# A    0  
# B    0  
# C    0  
# B    0  
# D    0  
# A    0  
# B    0  

# Fill lookup table with LCS lengths
LCSLength(X, Y, m, n, T) 

# After filling, the table will look like:
#     ""  B  D  C  A  B  A
# ""   0  0  0  0  0  0  0
# A    0  0  0  0  1  1  1
# B    0  1  1  1  1  2  2
# C    0  1  1  2  2  2  2
# B    0  1  1  2  2  3  3
# D    0  1  2  2  2  3  3
# A    0  1  2  2  3  3  4
# B    0  1  2  2  3  4  4

# Find and print the actual longest common subsequence string
print("The Longest Common Subsequence is:", LCS(X, Y, m, n, T)) 

# The LCS of "ABCBDAB" and "BDCABA" is "BCAB"
# This means the characters B, C, A, B appear in the same order in both strings

"""
How the algorithm works:
1. Create a table to store LCS lengths for all subproblems
2. Fill the table using the recurrence relation:
   - If characters match: LCS[i][j] = LCS[i-1][j-1] + 1
   - If they don't match: LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
3. Use the filled table to reconstruct the actual LCS string

Time Complexity: O(m * n) for filling table + O(m + n) for reconstruction = O(m * n)
Space Complexity: O(m * n) for the lookup table
"""