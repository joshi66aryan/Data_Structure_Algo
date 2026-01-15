# Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, listWords:list) -> str:
        length = len(listWords)
        listWords.sort()
        first, last = listWords[0], listWords[-1]
        minLen = min(len(first),len(last))
        
        i = 0
        while i < minLen and first[i] == last[i]:
            i+=1
        return first[:i]

if __name__ == "__main__":
    s = Solution()
    print(f"Result1: {s.longestCommonPrefix(["flower","flow","flight"])}")
    print(f"Result1: {s.longestCommonPrefix(["dog","racecar","car"])}")