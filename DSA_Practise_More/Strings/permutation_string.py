# Permutations of a String
# Difficulty: Medium
# Given a string s, which may contain duplicate characters, your task is to generate and return an array 
# of all unique permutations of the string. You can return your answer in any order.

# Examples:

# Input: s = "ABC"
# Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
# Explanation: Given string ABC has 6 unique permutations.

# Input: s = "ABSG"
# Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
# Explanation: Given string ABSG has 24 unique permutations.

# Input: s = "AAA"
# Output: ["AAA"]
# Explanation: No other unique permutations can be formed as all the characters are same.

# Constraints:
# 1 <= s.size() <= 9
# s contains only Uppercase english alphabets


class Solution:
    def permutation_helper(self, index, s, ans):
        if len(s) == index:
            ans.append("".join(s))
            return

        # 'index' represents the specific slot we are trying to fill right now.
        # 'i' represents the choices available to fill that slot.
        for i in range(index, len(s)):
            
            # 1. THE CHOICE (SWAP)
            # At a deep level, we are swapping the character at 'index' with 
            # every character that comes after it (including itself).
            # This "locks" a character into the current position for this branch.
            s[index], s[i] = s[i], s[index]

            # 2. THE EXPLORATION (RECURSION)
            # We move to the next slot (index + 1). 
            # Because 's' is a list (passed by reference), all deeper calls 
            # will see the change we just made. We keep diving until index == len(s).
            self.permutation_helper(index + 1, s, ans)

            # 3. THE UNDO (BACKTRACK)
            # This is the "Deeper Level" magic. Since 's' is shared across all calls, 
            # if we don't swap back, the string stays messy for the next loop iteration.
            # We restore the original order so the NEXT 'i' starts from a clean slate.
            s[index], s[i] = s[i], s[index]


    def permutation_string(self, s):
        if not s: 
            return None
        
        ans = []
        self.permutation_helper(0,list(s), ans)

        ans.sort()
        return ans
    
# What's happening in Memory (The "Why")
# When you run this for "ABC", think of it as a Decision Tree. Each level of the tree corresponds to the index value.

# Level 0 (index=0): The loop asks, "Who should be in the 1st position?"

# It tries swapping A into the 1st spot. (Then it calls the next level).

# Then it swaps B into the 1st spot. (Then it calls the next level).

# Then it swaps C into the 1st spot. (Then it calls the next level).

# Level 1 (index=1): The loop asks, "Now that the 1st spot is taken, who should be in the 2nd position?"

# It picks from the remaining characters.

# The Stack: Each time self.permutation_helper is called, a new "Frame" is pushed onto the Call Stack. 
# Python remembers exactly where it was in the for i in range... loop for every single level.

# Why the second swap s[index], s[i] = s[i], s[index] is critical:
# If you are at index=0 and you swap A with B to explore all permutations starting with "B" 
# (like "BAC" and "BCA"), you must swap them back to "ABC" before the loop moves to i=2. 
# If you don't, when you try to swap the first and third characters, you'd be swapping 
# from a mangled string instead of the original one.

if __name__ == "__main__":
    s = Solution()
    x = input("Enter the string")
    res = s.permutation_string(x)
    for item in res:
        print(item, end = " ")