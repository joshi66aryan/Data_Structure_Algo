# Check if Strings Are Rotations of Each Other

# Given two strings s1 and s2 of equal length, determine whether s2 is a rotation of s1.
# A string is said to be a rotation of another if it can be obtained by shifting some leading 
# characters of the original string to its end without changing the order of characters.

# Examples: 

# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: After 2 right rotations, s1 will become equal to s2.

# Input: s1 = "aab", s2 = "aba"
# Output: true
# Explanation: After 1 left rotation, s1 will become equal to s2.

# Input: s1 = "abcd", s2 = "acbd"
# Output: false
# Explanation: Strings are not rotations of each other.


class Solution:
    def check_rotation(self, s1:str, s2:str) -> bool:
        n, m = len(s1), len(s2)
        if s1 == s2:
            return False
        
        if len(s1) == 0:
            return False
        
        if len(s1) != len(s2):
            return False
        
        combined = s1+s1
        
        return self.kmp_search(combined, s2)
    
    def kmp_search(self, text:str, pattern:str) -> bool:
        lps = self.build_lps(pattern)
        i, j = 0, 0

        while i < len(text):
            if text[i] == pattern[j]:
                i+=1
                j+=1

            if j == len(pattern):
                return True
            
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                     i += 1
        return False


    def build_lps(self,pattern:str):
        n = len(pattern)
        i = 1
        length = 0 
        lps = [0]*n

        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    

if __name__ == "__main__":
    s = Solution()
    print("Result1",s.check_rotation("abcd", "cdab"))
    print("Result2",s.check_rotation("aab", "aba"))
    print("Result3",s.check_rotation("abcd", "acbd"))