# Split the binary string into substrings with equal number of 0s and 1s

# Given a binary string str of length N, the task is to find the maximum count of consecutive substrings 
# str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. 
# If it is not possible to split str satisfying the conditions then print -1.

# Example: 

# Input: str = "0100110101" 
# Output: 4 
# The required substrings are "01", "0011", "01" and "01".

# Input: str = "0111100010" 
# Output: 3 

# Input: str = "0000000000" 
# Output: -1

class Solution:
    def split_binary(self, s:str):

        count0 = 0
        count1 = 0
        count = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == '0':
                count0 += 1
            else:
                count1 +=1
            
            if count0 == count1:
                count += 1
        
        if count0 != count1:
            return -1
        
        return count



if __name__ == "__main__":
    s = Solution()
    print(f"Result1: {s.split_binary("0100110101")}")
    print(f"Result2: {s.split_binary("0111100010")}")
    print(f"Result3: {s.split_binary("0000000000")}")