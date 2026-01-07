# Print all subsequences of a string

# Given a string, we have to find out all its subsequences of it. A String is said to be a 
# subsequence of another String, if it can be obtained by deleting 0 or more character 
# without changing its order.


# Examples: 

# Input : ab
# Output : "", "a", "b", "ab"

# Input : abc
# Output : "", "a", "b", "c", "ab", "ac", "bc", "abc"


class Solution:
    def find_all_subsequences(self, s):
        """
        Generate all subsequences of a string s using recursion.

        Deep explanation (memory & backtracking):
        - Strings in Python are immutable. Each time we do `current + s[index]`,
          Python creates a new string object in memory; the original `current` is unchanged.
        - Recursion uses the **call stack**. Each call gets its own local variables
          (index, current) stored in a **stack frame**.
        - Backtracking happens naturally: after one branch finishes, the previous 
          frame is restored with the original `current` value.
        - Heap memory stores the string objects created by `current + s[index]`.
        """
        
        result = []  # List to store all subsequences (references to string objects)

        def helper(index, current):
            """
            Recursive helper function.

            Parameters:
            - index: current position in string s
            - current: subsequence formed so far (new string objects created for each include)
            
            Memory-level explanation:
            1. Every recursive call creates a new **stack frame** for its local variables.
            2. `current + s[index]` creates a new string in **heap memory**, leaving previous 'current' intact.
            3. When recursion returns, stack frame is popped, restoring previous 'current' automatically (backtracking).
            """
            # BASE CASE: reached the end of the string
            if index == len(s):
                # Store the current subsequence in result
                result.append(current)  # Append a reference to the string object in heap
                return
            
            # RECURSIVE CASE 1: INCLUDE s[index] in the subsequence
            # - Creates a new string object: current + s[index]
            # - A new stack frame is created for this recursive call
            helper(index + 1, current + s[index])
            
            # RECURSIVE CASE 2: EXCLUDE s[index] from the subsequence
            # - Uses the current string as-is (no changes, backtracking restored automatically)
            helper(index + 1, current)

        # Start recursion with index 0 and empty subsequence
        helper(0, "")
        return result


if __name__ == "__main__":
    s = Solution()
    
    # EXAMPLE 1: "ab"
    # Stack + memory trace for helper(0, "")
    # helper(0, "")           # Start, current = ""
    # ├─ INCLUDE 'a' → helper(1, "a") 
    # │    ├─ INCLUDE 'b' → helper(2, "ab") → base case → append "ab"
    # │    └─ EXCLUDE 'b' → helper(2, "a")  → base case → append "a"
    # └─ EXCLUDE 'a' → helper(1, "")
    #      ├─ INCLUDE 'b' → helper(2, "b")  → base case → append "b"
    #      └─ EXCLUDE 'b' → helper(2, "")   → base case → append ""
    print(f"Result1: {s.find_all_subsequences('ab')}")  
    # Output: ['ab', 'a', 'b', '']

    # EXAMPLE 2: "abc"
    # Deep backtracking happens naturally:
    # Each recursive call gets a new stack frame, current string + new char is in heap,
    # and returning from recursion restores previous current string automatically.
    print(f"Result2: {s.find_all_subsequences('abc')}")
    # Output: ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']
