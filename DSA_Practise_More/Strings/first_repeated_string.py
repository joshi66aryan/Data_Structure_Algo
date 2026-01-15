# Second most repeated string in a sequence
# Difficulty: Easy

# Given a sequence of strings, the task is to find out the second most repeated (or frequent) 
# string in the given sequence.

# Note: No two strings are the second most repeated, there will be always a single string.

# Example 1:

# Input:
# N = 6
# arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
# Output: bbb
# Explanation: "bbb" is the second most 
# occurring string with frequency 2.

# Example 2:

# Input: 
# N = 6
# arr[] = {geek, for, geek, for, geek, aaa}
# Output: for
# Explanation: "for" is the second most
# occurring string with frequency 2.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function secFrequent() 
# which takes the string array arr[] and its size N as inputs and returns the second most frequent string 
# in the array. If no such string exists, then return an empty string.


# Expected Time Complexity: O(N*max(|Si|).
# Expected Auxiliary Space: O(N*max(|Si|).


# Constraints:
# 1<=N<=103

 


class Solution:
    # My  solution:

    # def find_repeated_string(self,arr:list, n:int)->str:
    #     i = 0
    #     freq = dict()
    #     while i < n:
    #         freq[arr[i]] = freq.get(arr[i],0) + 1
    #         i+= 1
        
    #     firstMaxKey,  secondMaxKey  = ""
    #     firstMaxValue, secondMaxValue = 0
    #     for key, value in freq.items():
    #         if value > firstMaxValue:
    #             firstMaxKey, firstMaxValue = key, value
    #         elif value < firstMaxValue and value > secondMaxValue:
    #             secondMaxKey, secondMaxValue = key, value
        
    #     return (secondMaxKey, secondMaxValue)
    
    # optimized version:
    def secFrequent(self, arr, n):
        freq = {}

        # Count frequencies
        for word in arr:
            freq[word] = freq.get(word, 0) + 1

        firstMax = secondMax = 0
        firstKey = secondKey = ""

        for key, value in freq.items():
            if value > firstMax:
                secondMax, secondKey = firstMax, firstKey
                firstMax, firstKey = value, key
            elif firstMax > value > secondMax:
                secondMax, secondKey = value, key

        return secondKey
            




if __name__ == "__main__":
    s = Solution()
    s1 = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
    s2 = ['geek', 'for', 'geek', 'for', 'geek', 'aaa']
    print(s.secFrequent(s1,len(s1)))
    print(s.secFrequent(s2,len(s2)))