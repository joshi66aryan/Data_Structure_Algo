NO_OF_CHARS = 256 # We assume ASCII extended character set (0-255)

class Solution:

    def badCharHeuristic(self,string, size):
        '''
        Preprocessing function for Boyer Moore's Bad Character Heuristic
        Creates a table telling us the LAST position of each character in pattern
        '''
        # Initialize array with -1 → means character doesn't appear in pattern
        badChar = [-1] * NO_OF_CHARS
        
        # Fill the actual last occurrence position of each character
        for i in range(size):
            # ord() → converts character to its ASCII/Unicode integer value
            # We store the rightmost (last) position of each character
            badChar[ord(string[i])] = i
        
        return badChar


    def search(self,txt, pat):
        '''
        Main Boyer-Moore search function using only Bad Character Heuristic
        (Note: Real-world Boyer-Moore usually combines Bad Character + Good Suffix)
        '''
        m = len(pat)           # length of pattern
        n = len(txt)           # length of text
        
        # Preprocess pattern → create bad character table
        badChar = self.badCharHeuristic(pat, m)
        
        s = 0                  # s = current shift/alignment position of pattern
        
        # While we still have enough characters left to compare
        while s <= n - m:
            j = m - 1          # Start comparing from the END of the pattern
            
            # Compare pattern and text from right to left
            while j >= 0 and pat[j] == txt[s + j]:
                j -= 1
            
            # After inner loop:
            # j == -1  → we found complete match!
            # j >= 0   → mismatch occurred at position j in pattern
            
            if j < 0:
                # Pattern found!
                print("Pattern occur at shift = {}".format(s))
                
                # After match: decide how much to skip forward
                
                # If there are still characters after current match
                if s + m < n:
                    # Skip to align next text character with
                    # last occurrence of that character in pattern
                    # (or skip whole pattern length if character not found)
                    s += (m - badChar[ord(txt[s + m])])
                else:
                    # Pattern occurred at the very end → just move 1 step
                    s += 1
                    
            else:
                # Mismatch occurred!
                # badChar[ord(txt[s+j])] → last position of bad character in pattern
                # j - badChar[...] → how much we can safely skip
                
                # We take max(1, ...) because we must advance at least by 1
                # (to avoid infinite loop when badChar gives negative value)
                s += max(1, j - badChar[ord(txt[s + j])])


if __name__ == "__main__":
    s = Solution()
    s.search("ABAAABCD", "ABC")
             

