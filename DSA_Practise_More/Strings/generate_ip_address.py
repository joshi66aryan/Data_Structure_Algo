
# Generate Valid IP Addresses from String

# Given a String containing only digits, the task is to restore it by returning all possible valid IP address combinations.
# A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 
# prefixed unless they are 0.

# Examples:

# Input: "255678166"
# Output: [“25.56.78.166”, “255.6.78.166”, "255.67.8.166", "255.67.81.66"]
# Explanation: These are the only valid possible IP addresses.

# Input: "25505011535"
# Output: []
# Explanation: We cannot generate a valid IP address with this string.


class Solution:
    def isValid(self,s):
        n = len(s)
        if n == 1:
            return True

        val = int(s)
        if s[0] == '0'  or val > 255:
            return False

        return True
        
    def ipHelper(self,s:str, index, curr, cnt, res):
        temp = ""

        if index >=  len(s): 
            return 
        
        if cnt == 3:
            temp = s[index:]
            if len(temp) <= 3 and self.isValid(temp):
                res.append(curr+temp)
            return
        
        for i in range(index, min(index+3,len(s))):
            temp += s[i]
            if  self.isValid(temp):
                self.ipHelper(s, i+1, curr+temp+'.', cnt+1, res)
        
        


    def generateIPs(self, s:str):
        res = []
        self.ipHelper(s, 0, "", 0, res)
        return res



if __name__ == "__main__":
    s = Solution()
    print(f"Result1:{s.generateIPs("255678166")}")
    print(f"Result1:{s.generateIPs("25505011535")}")
