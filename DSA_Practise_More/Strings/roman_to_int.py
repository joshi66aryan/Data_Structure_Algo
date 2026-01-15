# Roman Number to Integer
# Difficulty: Easy
# Given a string s in Roman number format, your task is to convert it to an integer. Various symbols and their 
# values are given below.

# Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

# Examples:

# Input: s = "IX"
# Output: 9
# Explanation: IX is a Roman symbol which represents 10 – 1 = 9.

# Input: s = "XL"
# Output: 40
# Explanation: XL is a Roman symbol which represents 50 – 10 = 40.

# Input: s = "MCMIV"
# Output: 1904
# Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.

# Constraints:
# 1 ≤ roman number ≤ 3999
# s[i] belongs to [I, V, X, L, C, D, M]


class Solution:
    def romanToDecimal(self, map:dict, romanWrd:str) -> int:
        
        lenWord = len(romanWrd)
        res = 0
        i = 0

        while i < lenWord:
            if i+1 < lenWord and map[romanWrd[i]] < map[romanWrd[i+1]]:
                res +=  map[romanWrd[i+1]] -  map[romanWrd[i]] 
                i += 1
            else:
                res += map[romanWrd[i]]
            i+=1
        return res



if __name__ == "__main__":
    s = Solution()
    map = { 'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000 }
    print(f"Result1:{s.romanToDecimal(map,"IX")}")
    print(f"Result2:{s.romanToDecimal(map, "XL")}")
    print(f"Result3:{s.romanToDecimal(map, "MCMIV")}")

