# Convert a sentence into its equivalent mobile numeric keypad sequence

# Given a sentence in the form of a string, convert it into its equivalent mobile numeric keypad sequence. 
# Mobile-keypad

# Examples : 

# Input: GEEKSFORGEEKS
# Output: 4333355777733366677743333557777
# Explanation: For obtaining a number, we need to press a number corresponding to that character for a 
# number of times equal to the position of the character. For example, for character E, press number 3 two times
#  and accordingly.



# Input : HELLO WORLD
# Output : 4433555555666096667775553


class Solution:
    def printSequence(self,s,str):
        ans = ""
        s = s.lower()
        for i in s:
            if i == " ":
                ans += '0'
            else:
                temp = ord(i) - ord('a')
                ans += str[temp]
        return ans
if __name__ == "__main__":
    x = input("Enter text")
    s = Solution()
    str  = [
        "2","22","222",
        "3","33","333",
        "4","44","444",
        "5","55","555",
        "6","66","666",
        "7", "77", "777", "7777",
        "8", "88", "888",
        "9", "99", "999", "9999"
    ]
    print(f"Equivalent numeric keypad of the entered text: {s.printSequence(x,str)}")