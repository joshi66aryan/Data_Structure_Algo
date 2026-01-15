# Minimum Swaps for Bracket Balancing
# Difficulty: Medium 

# You are given a string s of 2*n characters consisting of n ‘[‘ brackets and n ‘]’ brackets. 
# A string is considered balanced if it can be represented in the form a[b] where a and b are balanced strings. 
# We can make an unbalanced string balanced by swapping adjacent characters. Calculate the minimum number of 
# swaps necessary to make a string balanced.

# Note - Strings a and b can be empty.

# Examples :

# Input: s = "[]][]["
# Output: 2
# Explanation: First swap: Position 3 and 4 [][]][, Second swap: Position 5 and 6 [][][]
                                                                                          
# Input: s = "[][]"
# Output : 0 

# Explanation: String is already balanced.
# Input: s = "[[[][][]]]"
# Output: 0 

# Constraints:
# 1<= s.size() <=105

class Solution:
    def minimumNoOfSwaps(self,strings:str)->int:
        openCount = 0
        swaps = 0
        n = len(strings)
        i = 0
        while i < n:
            if strings[i] == '[':
                openCount += 1
            else:
                openCount -= 1
            
            if openCount < 0:
                swaps += abs(openCount)
                balance = 1
            i += 1 
        return swaps
            


if __name__ == "__main__":
    s = Solution()
    print(f"Result1:{s.minimumNoOfSwaps("[]][][")}")
    print(f"Result1:{s.minimumNoOfSwaps("[][]")}")
    print(f"Result1:{s.minimumNoOfSwaps("[[[][][]]]")}")