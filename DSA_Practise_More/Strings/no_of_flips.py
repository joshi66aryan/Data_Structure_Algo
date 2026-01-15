# Min Number of Flips
# Difficulty: Easy 
# Given a binary string s of length n. We need to make this string a sequence of alternate characters by 
# flipping some of the bits, our goal is to minimize the number of bits to be flipped.

# Examples:

# Input: s = "001"
# Output: 1
# Explanation: We can flip the 0th bit to 1 to have "101".

# Input: s = "0001010111" 
# Output: 2
# Explanation: We can flip the 1st and 8th bit. After this we have "0101010101"

# Constraints:
# 1 ≤ |s| ≤ 105


class Solutions:
    def no_of_flips(self, s:str)->int:
        length = len(s)
        ans = 0
        # We count how many changes needed to make pattern: 010101...
        for i in range(length): 

            # For even positions (0,2,4,...) we want '0'
            # If we find '1' instead → we need to change it
            if i % 2 == 0 and s[i] == '1': 
                ans += 1

            # For odd positions (1,3,5,...) we want '1'
            # If we find '0' instead → we need to change it
            if i % 2 == 1 and s[i] == '0': 
                ans += 1
        
        # ans = changes needed to make 010101... pattern
        
        # The changes needed for the other pattern 101010... 
        # is exactly: total length - ans
        # Because every position you didn't change for one pattern,
        # you would need to change for the other
        
        return min(ans, length - ans) 
        # We take the minimum between the two possible target patterns
        



if __name__ == "__main__":
    s = Solutions()
    print(f"Number of flips required for 001: {s.no_of_flips("001")}")
    print(f"Number of flips required for 0001010111: {s.no_of_flips("0001010111")}")
