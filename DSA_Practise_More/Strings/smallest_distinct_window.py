# Smallest distinct window
# Difficulty: Medium 

# Given a string str, your task is to find the length of the smallest window that contains
# all the characters of the given string at least once.

# Example:

# Input: str = "aabcbcdbca"
# Output: 4
# Explanation: Sub-String "dbca" has the smallest length that contains all the characters of str.

# Input: str = "aaab"
# Output: 2
# Explanation: Sub-String "ab" has the smallest length that contains all the characters of str.

# Input: str = "geeksforgeeks"
# Output: 7
# Explanation: There are multiple substring with smallest length that contains all characters of str, "eksforg" and "ksforge".

# Constraints:
# 1 ≤ str.size() ≤ 105

# str contains only lower-case english alphabets.

class Solution:
    def findSubString(self,strs:str):
        n = len(strs)
        visited = [False]*26
        distinct = 0

        for i in range(n):
            if visited[ord(strs[i]) - ord('a')] == False:
                visited[ord(strs[i]) - ord('a')] = True
                distinct += 1

        freq = [0]*26  # Frequency of characters in the current window
        disCountInWindow = 0
        windowLength = n
        leftPointer = 0

        for i in range(n):
            # Include current character in the window
            freq[ord(strs[i]) - ord('a')] += 1

              # If this character appears first time in current window, increment count
            if freq[ord(strs[i]) - ord('a')] == 1:
                disCountInWindow += 1

            # If current window contains all distinct characters
            while disCountInWindow == distinct:
                   # Update minimum window size
                windowLength = min(windowLength,i-leftPointer+1)
            
                freq[ord(strs[leftPointer]) - ord('a')] -= 1

                # If removing this character makes its count zero,
                # it is no longer in the window, so decrement distinct count
                if freq[ord(strs[leftPointer]) - ord('a')] == 0:
                    disCountInWindow -= 1 # Key step: keeps 'cnt' accurate for current window
                
                # Move window start to the right to shrink window
                leftPointer += 1
        return windowLength  # Return length of smallest substring containing all distinct characters




if __name__ == "__main__":
    s = Solution()
    print(f"Result1:{s.findSubString("aabcbcdbca")}")
    print(f"Result2:{s.findSubString("aaab")}")
    print(f"Result3:{s.findSubString("geeksforgeeks")}")
    