# Create Largest Concatenated Number

# Given an array of non-negative integers arr[], arrange them such that their 
# concatenation forms the largest possible number. Return the result as a string, 
# since it may be too large for standard integer types.

# Examples:

# Input: arr[] =  [3, 30, 34, 5, 9]
# Output: 9534330
# Explanation: The arrangement [9, 5, 34, 3, 30], gives the largest value 9534330.

# Input: arr[] =  [54, 546, 548, 60]
# Output: 6054854654
# Explanation: The arrangement [60, 548, 546, 54], gives the largest value 6054854654.

from functools import cmp_to_key

def customCompare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1  # places s1 before s2
    else:
        return 1    # places s2 before s1

def findLargestConcat(arr):
    numbers = [str(x) for x in arr]
    numbers.sort(key = cmp_to_key(customCompare))

    if numbers[0] == '0':
        return '0'
    
    res = "".join(numbers)

    return res

if __name__ == "__main__":
    print(findLargestConcat([3, 30, 34, 5, 9]))
    print(findLargestConcat([54, 546, 548, 60]))
