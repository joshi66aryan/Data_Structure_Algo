# 38. Count and Say
# Medium
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive 
# identical characters (repeated 2 or more times) with the concatenation of the character and 
# the number marking the count of the characters (length of the run). For example, to compress 
# the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" 
# and replace "1" with "11". Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

 

# Example 1:

# Input: n = 4

# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:

# Input: n = 1

# Output: "1"

# Explanation:

# This is the base case.

 

# Constraints:

# 1 <= n <= 30


class Solution:
    def count_And_Say(self, n: int) -> str:
        # Base case:
        # The first term of the count-and-say sequence is always "1"
        result = "1"
        # Example: n = 4
        # Initially: result = "1"
        
        # We already have the 1st term,
        # so we generate the next (n - 1) terms
        for _ in range(n - 1):
            # This list will build the next term
            # Using list for efficiency (string concat is slow)
            next_str = []
            
            # Count of current repeating character
            count = 1
            
            # Traverse the current result string
            # Start from index 1 to compare with previous character
            for i in range(1, len(result)):
                
                # If current character is same as previous
                if result[i] == result[i - 1]:
                    # Increase count of repeated characters
                    count += 1
                else:
                    # Characters changed → write the previous group
                    
                    # Append count of previous character
                    next_str.append(str(count))
                    
                    # Append the previous character itself
                    next_str.append(result[i - 1])
                    
                    # Reset count for new character
                    count = 1
            
            # After loop ends, the LAST group is not yet added
            # So we append it manually
            
            # Append count of last repeated character
            next_str.append(str(count))
            
            # Append the last character
            next_str.append(result[-1])
            
            # Join list to form the new result string
            result = "".join(next_str)
            
            # ---------------- ITERATION EXAMPLE ----------------
            # Suppose n = 4
            #
            # Initial (before loop):
            #   result = "1"            → countAndSay(1)
            #
            # Loop iteration 1:
            #   result = "1"
            #   Read as: one '1'
            #   next_str = ["1", "1"]
            #   result becomes "11"     → countAndSay(2)
            #
            # Loop iteration 2:
            #   result = "11"
            #   Read as: two '1's
            #   next_str = ["2", "1"]
            #   result becomes "21"     → countAndSay(3)
            #
            # Loop iteration 3:
            #   result = "21"
            #   Read as: one '2', one '1'
            #   next_str = ["1", "2", "1", "1"]
            #   result becomes "1211"   → countAndSay(4)
            # ---------------------------------------------------

        
        # After completing all iterations, return final result
        return result



if __name__ == "__main__":
    s = Solution()
    x = int(input("Enter number you want to test."))
    print("Result1:",s.count_And_Say(x))
