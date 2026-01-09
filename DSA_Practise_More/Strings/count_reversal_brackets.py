# Count the Reversals
# Difficulty: Medium 
# Given a string s consisting of only opening and closing curly brackets '{' and '}', find out the minimum number of 
# reversals required to convert the string into a balanced expression. A reversal means changing '{' to '}' or vice-versa.

# Examples:

# Input: s = "}{{}}{{{"
# Output: 3
# Explanation: One way to balance is:
# "{{{}}{}}". There is no balanced sequence
# that can be formed in lesser reversals.

# Input: s = "{{}{{{}{{}}{{"
# Output: -1
# Explanation: There's no way we can balance
# this sequence of braces.

# Constraints:
# 1 ≤ |s| ≤ 105



class Solutions:
    def countReversal(self, s:str)->int:
        # bottom of stack should be. { and top of the stack should be closed. otherwise it required reversal.

        n = len(s)
        if n % 2 != 0:
            return -1
        
        countLeft = 0
        countRight = 0

        for i in range(n):
            if s[i] == '{':
                countLeft += 1
            else:
                if countLeft == 0:
                    countRight +=1
                else:
                    countLeft -= 1
        ans = (countLeft + 1) // 2 + (countRight + 1) // 2
        return ans 

# Simple explanation:
# (x + 1) // 2 = ceiling of x divided by 2
# It means: "how many flips do I need for x unbalanced braces?"
# Why?

# Every 2 unbalanced braces can be fixed with 1 flip.
# Example: {{ → flip one to } → becomes {} (1 flip fixes 2).
# If there's 1 left over (odd number), you need 1 more flip.

# Examples:

# x = 0 → (0+1)//2 = 0 → 0 flips
# x = 1 → (1+1)//2 = 1 → 1 flip
# x = 2 → (2+1)//2 = 1 → 1 flip (pair them)
# x = 3 → (3+1)//2 = 2 → 2 flips (fix 2 together, 1 alone)
# x = 4 → (4+1)//2 = 2 → 2 flips

# In the code:

# One side has left_brace excess {
# Other side has right_brace excess/early }

# We calculate flips needed for each side separately using (x + 1)//2, then add them.
# That sum = minimum total flips to make the whole string balanced.


if __name__ == "__main__":
    s = Solutions()
    print(f"the minimum number of reversals required to convert the string into a balanced expression1:{s.countReversal( "}{{}}{{{"  )}")
    print(f"the minimum number of reversals required to convert the string into a balanced expression2:{s.countReversal( "{{}{{{}{{}}{{"  )}")