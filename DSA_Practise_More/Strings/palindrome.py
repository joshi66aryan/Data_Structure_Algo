# 125. Valid Palindrome -- Easy
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
# characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class solution: 
    def check_palindrome(self, strings: str) -> bool:
        low, high = 0, len(strings) - 1

        while low < high:
            # Skip non-alphanumeric from left
            if not strings[low].isalnum():
                low += 1
                continue

            # Skip non-alphanumeric from right
            if not strings[high].isalnum():
                high -= 1
                continue

            # Compare lowercase characters
            if strings[low].lower() != strings[high].lower():
                return False

            low += 1
            high -= 1

        return True


if __name__ == "__main__":
    s = solution()
    print("Result1",s.check_palindrome("A man, a plan, a canal: Panama"))
    print("Result2",s.check_palindrome("race a car"))
    print("Result3:", s.check_palindrome(" "))
    
