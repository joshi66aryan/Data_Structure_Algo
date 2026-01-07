# Parenthesis Checker
# Difficulty: Easy

# Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. 
# Determine whether the Expression is balanced or not.
# An expression is balanced if:

# Each opening bracket has a corresponding closing bracket of the same type.
# Opening brackets must be closed in the correct order.
# Examples :

# Input: s = "[{()}]"
# Output: true
# Explanation: All the brackets are well-formed.

# Input: s = "[()()]{}"
# Output: true
# Explanation: All the brackets are well-formed.

# Input: s = "([]"
# Output: false
# Explanation: The expression is not balanced as there is a missing ')' at the end.

# Input: s = "([{]})"
# Output: false
# Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.

# Constraints:
# 1 ≤ s.size() ≤ 106
# s[i] ∈ {'{', '}', '(', ')', '[', ']'}

class Solution:
    def check_parenthesis(self,arr):
        stack = []

        for bracket in arr:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)

            elif bracket == ')' or bracket == '}' or bracket == ']':
                if not stack:
                    return False
                top = stack[-1]
                if (
                    (bracket == ')' and top != '(')or
                    (bracket == '}' and top != '{') or
                    (bracket == ']' and top != '[')
                ): return False

                stack.pop()
        return not stack
                

if __name__ == "__main__":
    s = Solution()
    print(f"Result1:{s.check_parenthesis( '[{()}]'   )}")
    print(f"Result1:{s.check_parenthesis( '[()()]{}' )}")
    print(f"Result1:{s.check_parenthesis( '([]'      )}")
    print(f"Result1:{s.check_parenthesis( '([{]})'   )}")