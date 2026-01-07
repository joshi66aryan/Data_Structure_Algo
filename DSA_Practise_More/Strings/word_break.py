# Word Break
# Difficulty: Medium
# You are given a string s and a list dictionary[] of words. Your task is to determine whether the string s 
# can be formed by concatenating one or more words from the dictionary[].

# Note: From dictionary[], any word can be taken any number of times and in any order.

# Examples :

# Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
# Output: true
# Explanation: s can be breakdown as "i like".

# Input: s = "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
# Output: true
# Explanation: s can be breakdown as "i like gfg".

# Input: s = "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
# Output: false
# Explanation: s cannot be formed using dictionary[] words.

# Constraints:
# 1 ≤ s.size() ≤ 3000
# 1 ≤ dictionary.size() ≤ 1000
# 1 ≤ dictionary[i].size() ≤ 100


class Solution:
    def wordBreak(self, s, dictionary):
        # Convert list to set for O(1) average lookup time
        word_set = set(dictionary)
        n = len(s)
        
        # dp[i] means s[0:i] can be segmented into words from the dictionary
        # Size is n + 1 to account for the empty string base case
        dp = [False] * (n + 1)
        
        # Base case: An empty string can always be "formed"
        dp[0] = True
        
        # Iterate through every possible end position of a substring
        for i in range(1, n + 1):
            # Check every possible split point before 'i'
            for j in range(i):
                # If s[0:j] is valid AND s[j:i] exists in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    # Optimization: No need to check other j's if we found one valid split
                    break
                    
        return dp[n]

# Example Execution Trace:
# s = "ilike", dictionary = ["i", "like"]
# i=1: j=0 -> s[0:1]="i" is in set, dp[0] is T -> dp[1]=T
# i=2: j=0 -> s[0:2]="il" (F), j=1 -> s[1:2]="l" (F) -> dp[2]=F
# i=3: j=0,1,2 -> No combinations work -> dp[3]=F
# i=4: j=0,1,2,3 -> No combinations work -> dp[4]=F
# i=5: j=1 -> dp[1] is T AND s[1:5]="like" is in set -> dp[5]=T
# Result: True


if __name__ == "__main__":
    s = Solution() 
    print(f"Result1: {s.wordBreak("ilike", ["i", "like", "gfg"])}")
    print(f"Result2: {s.wordBreak("ilikegfg", ["i", "like", "man", "india", "gfg"])}")
    print(f"Result3: {s.wordBreak("ilikemangoes", ["i", "like", "man", "india", "gfg"])}")