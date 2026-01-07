#  Reverse String - Easy
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


from typing import List

class solution:
    def reverse_string(self, arr: List[str]) -> None:
        n = len(arr)
        low, high = 0, n-1
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1





if __name__ == "__main__":
    s1 = solution()

    I1 = ["h","e","l","l","o"]
    s1.reverse_string(I1)

    I2 = ["H","a","n","n","a","h"]
    s1.reverse_string(I2)

    print("Result1:",I1)
    print("Result2:",I2)