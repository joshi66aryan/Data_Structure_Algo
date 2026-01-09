"""
KMP (Knuth-Morris-Pratt) Algorithm for 2D Grid String Search

PROBLEM OVERVIEW:
-----------------
Given a 2D character grid and a target string, find how many times the string
appears in the grid. The string can appear in 4 directions:
1. Horizontally left-to-right
2. Horizontally right-to-left
3. Vertically top-to-bottom
4. Vertically bottom-to-top

WHY KMP ALGORITHM?
------------------
Naive approach: O(n*m) per search where n=text length, m=pattern length
KMP approach: O(n+m) per search - much faster!

KMP avoids re-checking characters we've already matched by using the LPS array
to "remember" which parts of the pattern can be reused after a mismatch.
"""

def computeLPSArray(pat, M, lps):
    """
    Computes the Longest Proper Prefix which is also Suffix (LPS) array.
    
    WHAT IS LPS?
    ------------
    For each position i in the pattern, lps[i] stores the length of the longest
    proper prefix of pat[0...i] that is also a suffix of pat[0...i].
    
    "Proper" means: prefix/suffix cannot be the entire substring itself.
    
    EXAMPLE 1: Pattern "AABAAC"
    Position:  0  1  2  3  4  5
    Pattern:   A  A  B  A  A  C
    LPS:       0  1  0  1  2  0
    
    Explanation:
    - lps[0] = 0: Single char has no proper prefix/suffix
    - lps[1] = 1: "AA" → prefix "A" = suffix "A" (length 1)
    - lps[2] = 0: "AAB" → no matching prefix/suffix
    - lps[3] = 1: "AABA" → prefix "A" = suffix "A" (length 1)
    - lps[4] = 2: "AABAA" → prefix "AA" = suffix "AA" (length 2)
    - lps[5] = 0: "AABAAC" → no matching prefix/suffix
    
    EXAMPLE 2: Pattern "ABABC"
    Position:  0  1  2  3  4
    Pattern:   A  B  A  B  C
    LPS:       0  0  1  2  0
    
    Explanation:
    - lps[2] = 1: "ABA" → prefix "A" = suffix "A"
    - lps[3] = 2: "ABAB" → prefix "AB" = suffix "AB"
    
    WHY IS THIS USEFUL?
    -------------------
    When we have a mismatch after matching j characters, instead of starting
    over from the beginning, we can skip ahead to position lps[j-1] because
    we know those characters already match!
    
    Parameters:
    -----------
    pat: The pattern string
    M: Length of pattern
    lps: Array to store LPS values (passed by reference, modified in place)
    """
    
    # len = length of the longest prefix-suffix we've found so far
    # It represents how many characters from the start of the pattern
    # match the characters just before the current position
    len_prefix = 0
    
    # Base case: First character has no proper prefix or suffix
    # A single character cannot have a "proper" prefix/suffix
    lps[0] = 0
    
    # Start from second character and build LPS array iteratively
    i = 1
    
    while i < M:
        # CASE 1: Characters match - extend the current prefix-suffix
        if pat[i] == pat[len_prefix]:
            # We found a longer matching prefix-suffix!
            # Example: Pattern "ABAB", at i=3
            # pat[3]='B' matches pat[1]='B' (len_prefix was 1)
            # So now we have prefix "AB" = suffix "AB" (length 2)
            len_prefix += 1
            lps[i] = len_prefix
            i += 1
        
        # CASE 2: Mismatch - we need to handle this carefully
        else:
            if len_prefix != 0:
                # CRITICAL REASONING: Why lps[len_prefix - 1]?
                # -----------------------------------------------
                # We had a match of length 'len_prefix', but now mismatched.
                # The question is: is there a SHORTER prefix-suffix we can use?
                #
                # The insight: If pat[0...len_prefix-1] has a prefix-suffix of
                # length k (stored in lps[len_prefix-1]), then we can try
                # matching from position k instead!
                #
                # Example: Pattern "AABAAC", at i=5, len_prefix=2
                # We've matched "AA" but pat[5]='C' doesn't match pat[2]='B'
                # lps[1] = 1 tells us there's a shorter overlap of length 1
                # So we try matching 'C' with pat[1] instead
                #
                # IMPORTANT: We do NOT increment i here!
                # We want to retry matching pat[i] with pat[len_prefix]
                len_prefix = lps[len_prefix - 1]
            else:
                # No prefix-suffix match possible at this position
                # len_prefix is already 0, can't fall back further
                lps[i] = 0
                i += 1
    
    # Example walkthrough for "ABABC":
    # i=0: lps[0]=0 (by definition)
    # i=1: A≠B, len=0 → lps[1]=0, i=2
    # i=2: A==A, len=1 → lps[2]=1, i=3
    # i=3: B==B, len=2 → lps[3]=2, i=4
    # i=4: C≠A, len=lps[1]=0, then C≠A, len=0 → lps[4]=0, i=5
    # Result: lps = [0, 0, 1, 2, 0]


def KMPSearch(pat, txt):
    """
    Searches for all occurrences of pattern 'pat' in text 'txt' using KMP.
    Counts overlapping matches.
    
    ALGORITHM OVERVIEW:
    -------------------
    Maintain two pointers:
    - i: current position in text (where we're reading)
    - j: current position in pattern (how much we've matched so far)
    
    THREE MAIN SCENARIOS:
    1. Match: Both pointers advance
    2. Full pattern matched: Count it, use LPS to find next potential match
    3. Mismatch: Use LPS to avoid re-checking already matched characters
    
    TIME COMPLEXITY: O(N + M)
    - Computing LPS: O(M)
    - Searching: O(N) - each character of text examined at most twice
    
    SPACE COMPLEXITY: O(M) for LPS array
    
    Parameters:
    -----------
    pat: Pattern string to search for
    txt: Text string to search in
    
    Returns:
    --------
    Count of pattern occurrences (including overlapping matches)
    """
    M = len(pat)  # Pattern length
    N = len(txt)  # Text length
    
    # Build LPS array for the pattern
    lps = [0] * M
    computeLPSArray(pat, M, lps)
    
    i = 0      # Index in text
    j = 0      # Index in pattern (also represents how many chars matched)
    cnt = 0    # Count of matches found
    
    # CRITICAL CONDITION: Why (N - i) >= (M - j)?
    # --------------------------------------------
    # (N - i) = number of characters remaining in text (including position i)
    # (M - j) = number of characters still needed to complete the pattern
    #
    # If remaining text < remaining pattern, it's impossible to find a match.
    # This optimization prevents unnecessary iterations at the end.
    #
    # Example: Text="HELLO"(N=5), Pattern="WORLD"(M=5)
    # At i=2: (5-2)=3 chars left, but need (5-0)=5 chars → Can continue? 3>=5? NO!
    # At i=1: (5-1)=4 chars left, need 5 chars → 4>=5? NO!
    # 
    # Example: Text="HELLO"(N=5), Pattern="LLO"(M=3)
    # At i=2: (5-2)=3 chars left, need (3-0)=3 chars → 3>=3? YES! Continue.
    # At i=3: (5-3)=2 chars left, need 3 chars → 2>=3? NO! Stop.
    
    while (N - i) >= (M - j):
        
        # SCENARIO 1: Characters match
        if pat[j] == txt[i]:
            # Move both pointers forward
            # We've successfully matched one more character
            j += 1
            i += 1
        
        # SCENARIO 2: Full pattern matched (j reached end of pattern)
        if j == M:
            # Found a complete match!
            cnt += 1
            
            # CRITICAL REASONING: Why j = lps[j-1] instead of j = 0?
            # -------------------------------------------------------
            # We want to find OVERLAPPING matches!
            # 
            # Example: Text="AAAA", Pattern="AAA"
            # After finding first match at position 0:
            #   Text:    A A A A
            #   Pattern: A A A
            #            0 1 2
            # 
            # If we reset j=0, we'd move pattern completely and miss overlaps.
            # But lps[2]=2 tells us the last 2 chars "AA" of our match
            # are the same as the first 2 chars "AA" of the pattern!
            # 
            # So we can slide the pattern by only 1 position:
            #   Text:    A A A A
            #   Pattern:   A A A  ← Start checking from j=2
            #              0 1 2
            # 
            # This way we find the overlapping match at position 1!
            #
            # IMPORTANT: j-1 because j currently equals M (one past last index)
            # The last actual character matched was at index j-1
            j = lps[j - 1]
        
        # SCENARIO 3: Mismatch after some matches (or at start)
        elif i < N and pat[j] != txt[i]:
            # Additional check (i < N) prevents accessing txt beyond bounds
            
            if j != 0:
                # CRITICAL REASONING: Why j = lps[j-1]?
                # --------------------------------------
                # We've matched j characters (positions 0 to j-1 of pattern)
                # But pat[j] doesn't match txt[i]
                #
                # The key insight: The text segment txt[i-j...i-1] matches
                # pattern segment pat[0...j-1]
                #
                # lps[j-1] tells us: within pat[0...j-1], there's a prefix
                # of length lps[j-1] that equals a suffix of length lps[j-1]
                #
                # This means: txt[i-lps[j-1]...i-1] matches pat[0...lps[j-1]-1]
                # So we can skip ahead and retry from position lps[j-1]!
                #
                # Example: Text="ABABCABABD", Pattern="ABABC"
                #          LPS=[0,0,1,2,0]
                # 
                # After matching "ABAB" (j=4), we mismatch at 'C' vs 'D'
                # lps[3] = 2 means first 2 chars "AB" = last 2 chars "AB"
                # So the last "AB" we matched in text can serve as the
                # first "AB" of a new pattern match attempt!
                #
                # Text:    A B A B C A B A B D
                # Pattern: A B A B C
                #                A B A B C  ← Continue from j=2
                #
                # IMPORTANT: We do NOT increment i!
                # We want to retry matching txt[i] against pat[lps[j-1]]
                j = lps[j - 1]
            else:
                # j=0 means we haven't matched anything yet
                # First character itself doesn't match
                # Move to next character in text and try again
                i += 1
    
    return cnt
    
    # Example walkthrough: Search "ABA" in "ABABABA"
    # Pattern: A B A (M=3), LPS: [0, 0, 1]
    # Text:    A B A B A B A (N=7)
    #
    # i=0,j=0: 7-0>=3-0 (7≥3✓), A==A, i=1,j=1
    # i=1,j=1: 7-1>=3-1 (6≥2✓), B==B, i=2,j=2
    # i=2,j=2: 7-2>=3-2 (5≥1✓), A==A, i=3,j=3
    # j==3: Match found! cnt=1, j=lps[2]=1
    # i=3,j=1: 7-3>=3-1 (4≥2✓), B==B, i=4,j=2
    # i=4,j=2: 7-4>=3-2 (3≥1✓), A==A, i=5,j=3
    # j==3: Match found! cnt=2, j=lps[2]=1
    # i=5,j=1: 7-5>=3-1 (2≥2✓), B==B, i=6,j=2
    # i=6,j=2: 7-6>=3-2 (1≥1✓), A==A, i=7,j=3
    # j==3: Match found! cnt=3, j=lps[2]=1
    # i=7,j=1: 7-7>=3-1 (0≥2✗) STOP
    # Result: 3 overlapping matches found!


def main():
    """
    Main function to search for a target string in a 2D grid.
    
    APPROACH:
    ---------
    1. Convert each row to a string, search left→right and right→left
    2. Convert each column to a string, search top→bottom and bottom→top
    3. Use KMP for efficient string matching in each direction
    
    WHY SEARCH IN ALL 4 DIRECTIONS?
    --------------------------------
    The target string can be spelled forwards or backwards in the grid.
    - Horizontal forward: Normal left-to-right reading
    - Horizontal backward: Right-to-left (reverse the row string)
    - Vertical forward: Top-to-bottom (build column string)
    - Vertical backward: Bottom-to-top (reverse the column string)
    """
    
    # Target string we're searching for
    str = "MAGIC"
    
    # 2D grid represented as list of strings
    # Each string is a row of the grid
    input = [
        "BBABBM",  # Row 0: No "MAGIC"
        "CBMBBA",  # Row 1: No "MAGIC"
        "IBABBG",  # Row 2: No "MAGIC"
        "GOZBBI",  # Row 3: No "MAGIC"
        "ABBBBC",  # Row 4: No "MAGIC"
        "MCIGAM"   # Row 5: Contains "MAGIC" backwards! (M-A-G-I-C reading right-to-left)
    ]
    
    # Grid visualization with indices:
    #       Col: 0 1 2 3 4 5
    # Row 0:     B B A B B M
    # Row 1:     C B M B B A
    # Row 2:     I B A B B G
    # Row 3:     G O Z B B I
    # Row 4:     A B B B B C
    # Row 5:     M C I G A M
    #
    # Column 5 (reading top to bottom): M-A-G-I-C-M (contains "MAGIC"!)
    # Row 5 (reading right to left): M-A-G-I-C-M (contains "MAGIC"!)
    
    n = len(input)      # Number of rows = 6
    m = len(input[0])   # Number of columns = 6 (assuming all rows same length)
    ans = 0             # Total count accumulator
    
    # ============================================
    # PHASE 1: HORIZONTAL SEARCH (Row-wise)
    # ============================================
    # For each row, we treat it as a 1D string and search in both directions
    
    for i in range(n):  # i goes from 0 to 5
        text = input[i]  # Get the entire row as a string
        
        # Search LEFT → RIGHT
        # Normal reading direction
        # Example: Row 5 = "MCIGAM"
        # Searching for "MAGIC" in "MCIGAM" → No match (0 occurrences)
        ans += KMPSearch(str, text)
        
        # Search RIGHT → LEFT
        # Reverse the row and search for the original pattern
        # Why this works: If "MAGIC" is spelled backwards in the row,
        # it becomes forwards in the reversed row!
        # 
        # Example: Row 5 = "MCIGAM"
        # Reversed: "MAGICM"
        # Searching for "MAGIC" in "MAGICM" → Found! (1 occurrence)
        text_reversed = text[::-1]  # Python slice notation to reverse string
        ans += KMPSearch(str, text_reversed)
    
    # After horizontal search:
    # Found 1 occurrence in Row 5 (reading right-to-left)
    # ans = 1
    
    # ============================================
    # PHASE 2: VERTICAL SEARCH (Column-wise)
    # ============================================
    # For each column, we build a string by concatenating characters
    # from top to bottom, then search in both directions
    
    for i in range(m):  # i goes from 0 to 5 (each column index)
        # Build the column string
        text = ""
        for j in range(n):  # j goes from 0 to 5 (each row)
            # Take the i-th character from the j-th row
            text += input[j][i]
        
        # Example: Building column 5 (i=5)
        # j=0: text += input[0][5] = "M"
        # j=1: text += input[1][5] = "MA"
        # j=2: text += input[2][5] = "MAG"
        # j=3: text += input[3][5] = "MAGI"
        # j=4: text += input[4][5] = "MAGIC"
        # j=5: text += input[5][5] = "MAGICM"
        # Final: text = "MAGICM"
        
        # Search TOP → BOTTOM
        # Normal vertical reading direction
        # Example: Column 5 = "MAGICM"
        # Searching for "MAGIC" in "MAGICM" → Found! (1 occurrence)
        ans += KMPSearch(str, text)
        
        # Search BOTTOM → TOP
        # Reverse the column string and search
        # Example: Column 5 = "MAGICM"
        # Reversed: "MCIGAM"
        # Searching for "MAGIC" in "MCIGAM" → No match (0 occurrences)
        text_reversed = text[::-1]
        ans += KMPSearch(str, text_reversed)
    
    # After vertical search:
    # Found 1 occurrence in Column 5 (reading top-to-bottom)
    # ans = 1 + 1 = 2
    
    # ============================================
    # FINAL RESULT
    # ============================================
    print("Count :", ans)  # Output: Count : 2
    
    # Summary of where "MAGIC" was found:
    # 1. Row 5, reading right-to-left: M←C←I←G←A←M
    # 2. Column 5, reading top-to-bottom: M↓A↓G↓I↓C↓M

if __name__ == "__main__":
    main()


"""
COMPLETE ALGORITHM SUMMARY:
===========================

1. LPS ARRAY COMPUTATION: O(M) where M = pattern length
   - Builds a lookup table to enable efficient pattern sliding
   - Stores longest matching prefix-suffix for each position
   - Key insight: Reuse previous match information to avoid redundant comparisons

2. KMP SEARCH: O(N) where N = text length
   - Each text character examined at most twice
   - Uses LPS array to skip already-matched characters
   - Finds all overlapping occurrences

3. GRID SEARCH: O(rows × cols)
   - Process each row: 2 searches × O(cols)
   - Process each column: 2 searches × O(rows)
   - Total searches: 4 × max(rows, cols)

TOTAL TIME COMPLEXITY: O(rows × cols) + O(pattern_length × searches)
In practice, very efficient for grid-based string searching!

KEY ADVANTAGES OF KMP:
----------------------
1. No backtracking in the text (i never decreases)
2. Linear time complexity guaranteed
3. Handles overlapping matches correctly
4. Works well with repeated patterns (e.g., "AAAA")
"""