# Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

# Examples:

# Input: arr[] = [111, 222, 333, 444, 555]
# Output: true

# Explanation:
    # arr[0] = 111, which is a palindrome number.
    # arr[1] = 222, which is a palindrome number.
    # arr[2] = 333, which is a palindrome number.
    # arr[3] = 444, which is a palindrome number.
    # arr[4] = 555, which is a palindrome number.
    # As all numbers are palindrome so This will return true.

# Input: arr[] = [121, 131, 20]
# Output: false

# Explanation: 20 is not a palindrome hence the output is false.
    # Expected Time Complexity: O(nlogn)
    # Expected Space Complexity: O(1)

# Constraints:
    # 1 <=arr.size<= 20
    # 1 <=arr[i]<= 105


def check_palindrome(num):
    if num < 0:
        return False
    
    original = num
    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    return reversed_num == original 
    

def all_palindrome(arr):
    """
    Main function: Returns True if all elements in arr are palindromic numbers.
    
    Time Complexity: O(n × d) 
                     where n = len(arr), d = average number of digits in elements
                     Since max(arr[i]) <= 10^5 → d <= 6 → O(n × 6) = O(n)
                     But as per expected constraint: O(n log n) is acceptable.
                     (log n here refers to log10 of number value, not array size)
    
    Space Complexity: O(1) — only using a few variables
    """
    if not arr:
        return False
    
    for x in arr:
        if not check_palindrome(x):
            return False
    return True



if __name__ == "__main__":
    arr = [111, 222, 333, 444, 555]
    arr1 = [123, 234]

    print(f"The given array is palindrome:{all_palindrome(arr)}")
    print(f"The given array is palindrome:{all_palindrome(arr1)}")
