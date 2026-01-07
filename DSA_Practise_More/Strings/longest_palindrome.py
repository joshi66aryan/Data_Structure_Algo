# Longest Palindrome in a String
# Difficulty: Medium
# Given a string s, your task is to find the longest palindromic substring within s.

# A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).

# A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if reverse(s) == s.

# Note: If there are multiple palindromic substrings with the same length, return the first occurrence of the 
# longest palindromic substring from left to right.

# Examples :

# Input: s = “forgeeksskeegfor” 
# Output: “geeksskeeg”
# Explanation: There are several possible palindromic substrings like “kssk”, “ss”, “eeksskee” etc. But the 
# substring “geeksskeeg” is the longest among all.

# Input: s = “Geeks” 
# Output: “ee”
# Explanation: "ee" is the longest palindromic substring of "Geeks". 

# Input: s = “abc” 
# Output: “a”
# Explanation: "a", "b" and "c" are longest palindromic substrings of same length. So, the first occurrence is returned.

# Constraints:
# 1 ≤ s.size() ≤ 103
# s consist of only lowercase English letters.


class Solution:
    def expand_around_center(self, s, left, right):
        # Continue expanding as long as indices are valid 
        # and characters at left/right match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1     # Move left pointer outwards
            right += 1    # Move right pointer outwards
        
        # Returns the valid boundaries. 
        # Since the loop breaks when s[left] != s[right], 
        # we return left+1 and right-1 to get the correct palindrome range.
        return left + 1, right - 1

    def longest_palindrome(self, s):
        # Handle empty string case
        if not s:
            return None
        
        start = 0       # Stores the starting index of the longest palindrome
        max_length = 1  # Stores the length of the longest palindrome found

        for i in range(len(s)):  
            # --- Odd Length Check ---
            # Center is a single character (e.g., 'aba', center is 'b')
            l1, r1 = self.expand_around_center(s, i, i)
            if (r1 - l1 + 1) > max_length:
                max_length = r1 - l1 + 1
                start = l1

            # --- Even Length Check ---
            # Center is between two characters (e.g., 'abba', center is between 'b' and 'b')
            l2, r2 = self.expand_around_center(s, i, i + 1)
            if (r2 - l2 + 1) > max_length:
                max_length = r2 - l2 + 1
                start = l2

        # Return the slice using the stored start and length
        return s[start:start + max_length]

if __name__ == "__main__":
    s = Solution()
    print("Result1",s.longest_palindrome("forgeeksskeegfor"))
    print("Result2",s.longest_palindrome("Geeks"))
    print("Result3",s.longest_palindrome("abc"))