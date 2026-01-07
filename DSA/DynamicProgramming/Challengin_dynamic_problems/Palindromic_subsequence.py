
# ### Code with More Detailed Comments

# # This function is named 'lps', short for Longest Palindromic Subsequence.
# # Its job is to find the length of the longest possible palindrome you can make 
# # by deleting zero or more characters from the input string.
# def lps(str): 
#     # First, we get the total number of characters in the string.
#     # We store it in a variable 'n' so we can use it easily later.
#     n = len(str) 
  
#     # This is the most important part: we create our "cheat sheet".
#     # It's a 2D grid (like a spreadsheet or a chessboard) named 'L'.
#     # L[i][j] will store the answer for the chunk of the string that starts at index 'i' and ends at index 'j'.
#     # We initialize it with all zeros.
#     L = [[0 for x in range(n)] for x in range(n)] 
  
#     # --- STEP 1: Handle the smallest possible chunks (single letters) ---
#     # A single letter is always a palindrome of length 1 (e.g., "G" is a palindrome).
#     # This loop goes through each character of the string.
#     for i in range(n): 
#         # It fills the diagonal of our grid (L[0][0], L[1][1], etc.) with the number 1.
#         # This means "The longest palindrome in the chunk from index i to i is 1".
#         L[i][i] = 1
  
#     # --- STEP 2: Build up solutions for bigger and bigger chunks ---
#     # 'cl' stands for "chunk length". We start with chunks of length 2, then 3, all the way up to 'n'.
#     for cl in range(2, n + 1): 
        
#         # 'i' is the starting index of our chunk. This loop slides our "window" of size 'cl' across the string.
#         for i in range(n - cl + 1): 
#             # 'j' is the ending index. This formula calculates where a chunk of length 'cl' ends if it starts at 'i'.
#             j = i + cl - 1
            
#             # Now, for the chunk of the string from 'i' to 'j', we have three possibilities:

#             # POSSIBILITY A: The chunk has length 2 and its characters are the same (e.g., "EE").
#             if str[i] == str[j] and cl == 2: 
#                 # This is a palindrome of length 2. We record '2' in our cheat sheet.
#                 L[i][j] = 2
                
#             # POSSIBILITY B: The ends match, and the chunk is longer than 2 (e.g., "BEEB").
#             elif str[i] == str[j]: 
#                 # The total length will be 2 (for the matching ends) PLUS the length of the
#                 # palindrome for the middle part (the "EE" in "BEEB").
#                 # We've ALREADY solved the middle part! The answer is in our cheat sheet at L[i+1][j-1].
#                 # So we just look it up and add 2.
#                 L[i][j] = L[i+1][j-1] + 2
                
#             # POSSIBILITY C: The ends DO NOT match (e.g., "GEK").
#             else: 
#                 # Since the ends don't match, we can't use both of them. We have to discard one.
#                 # We find the longest palindrome by either:
#                 #   1. Ignoring the last character (look at "GE"). The answer is already in L[i][j-1].
#                 #   2. Ignoring the first character (look at "EK"). The answer is already in L[i+1][j].
#                 # We take the bigger of those two options.
#                 L[i][j] = max(L[i][j-1], L[i+1][j]); 
  
#     # --- STEP 3: Return the final answer ---
#     # After all the loops, our cheat sheet is completely filled.
#     # The answer for the ENTIRE string (from index 0 to n-1) is in the top-right corner.
#     return L[0][n-1] 

# """

# ### A Step-by-Step Example: The String `"BEEB"`

# Let's trace how the table `L` gets filled for `str = "BEEB"` (`n=4`).

# #### **Initial Table**

# The code creates a 4x4 grid filled with zeros.

# | | 0 (B) | 1 (E) | 2 (E) | 3 (B) |
# | :-- | :-- | :-- | :-- | :-- |
# | **0 (B)** | 0 | 0 | 0 | 0 |
# | **1 (E)** | | 0 | 0 | 0 |
# | **2 (E)** | | | 0 | 0 |
# | **3 (B)** | | | | 0 |

# #### **Step 1: Fill Diagonals (Chunks of length 1)**

# Every character is a palindrome of length 1.
# `L[0][0]=1`, `L[1][1]=1`, `L[2][2]=1`, `L[3][3]=1`.

# | | 0 (B) | 1 (E) | 2 (E) | 3 (B) |
# | :-- | :-- | :-- | :-- | :-- |
# | **0 (B)** | **1** | 0 | 0 | 0 |
# | **1 (E)** | | **1** | 0 | 0 |
# | **2 (E)** | | | **1** | 0 |
# | **3 (B)** | | | | **1** |

# #### **Step 2.1: `cl = 2` (Chunks of length 2)**

#   * `i=0, j=1` ("BE"): `B != E`. `L[0][1] = max(L[0][0], L[1][1]) = max(1,1) = 1`.
#   * `i=1, j=2` ("EE"): `E == E`. It's length 2, so `L[1][2] = 2`.
#   * `i=2, j=3` ("EB"): `E != B`. `L[2][3] = max(L[2][2], L[3][3]) = max(1,1) = 1`.

# | | 0 (B) | 1 (E) | 2 (E) | 3 (B) |
# | :-- | :-- | :-- | :-- | :-- |
# | **0 (B)** | 1 | **1** | 0 | 0 |
# | **1 (E)** | | 1 | **2** | 0 |
# | **2 (E)** | | | 1 | **1** |
# | **3 (B)** | | | | 1 |

# #### **Step 2.2: `cl = 3` (Chunks of length 3)**

#   * `i=0, j=2` ("BEE"): `B != E`. `L[0][2] = max(L[0][1], L[1][2]) = max(1,2) = 2`.
#   * `i=1, j=3` ("EEB"): `E != B`. `L[1][3] = max(L[1][2], L[2][3]) = max(2,1) = 2`.

# | | 0 (B) | 1 (E) | 2 (E) | 3 (B) |
# | :-- | :-- | :-- | :-- | :-- |
# | **0 (B)** | 1 | 1 | **2** | 0 |
# | **1 (E)** | | 1 | 2 | **2** |
# | **2 (E)** | | | 1 | 1 |
# | **3 (B)** | | | | 1 |

# #### **Step 2.3: `cl = 4` (The whole string)**

#   * `i=0, j=3` ("BEEB"): `B == B`. So, `L[0][3] = 2 + L[1][2]`. We look up `L[1][2]` in our table, which is `2`.
#   * `L[0][3] = 2 + 2 = 4`.

# | | 0 (B) | 1 (E) | 2 (E) | 3 (B) |
# | :-- | :-- | :-- | :-- | :-- |
# | **0 (B)** | 1 | 1 | 2 | **4** |
# | **1 (E)** | | 1 | 2 | 2 |
# | **2 (E)** | | | 1 | 1 |
# | **3 (B)** | | | | 1 |

# The final answer is in the top-right corner: **4**.

# """

def LPS(string):
    n = len(string)
    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            # three possibilities.
            if string[i] == string[j] and cl == 2:
                L[i][j] = 2
            elif string[i] == string[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])
    return L[0][n-1]
print(LPS("BEEB"))

