# Three way partitioning
# Difficulty: Easy

# Given an array and a range a, b. The task is to partition the array around 
# the range such that the array is divided into three parts.

# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.

# The individual elements of three sets can appear in any order. You are required to return the modified array.

# Note: The generated output is true if you modify the given array successfully. Otherwise false.

# Geeky Challenge: Solve this problem in O(n) time complexity.

# Examples:

# Input: arr[] = [1, 2, 3, 3, 4], a = 1, b = 2
# Output: true
# Explanation: One possible arrangement is: {1, 2, 3, 3, 4}. If you return a valid arrangement, output will be true.

# Input: arr[] = [1, 4, 3, 6, 2, 1], a = 1, b = 3
# Output: true
# Explanation: One possible arrangement is: {1, 3, 2, 1, 4, 6}. If you return a valid arrangement, output will be true.

# Constraints:
#     1 <= arr.size()<= 106
#     1 <= array[i], a, b <= 109


def threeWayPartition(arr, a, b):
    # We use three pointers: low, mid, high
    # low  -> boundary for elements < a
    # mid  -> current element being processed
    # high -> boundary for elements > b

    low = 0
    mid = 0
    high = len(arr) - 1

    # Example for understanding:
    # arr = [1, 4, 3, 6, 2, 1], a = 1, b = 3
    # We will show iterations in comments below.

    while mid <= high:

        # CASE 1: Current element < a → swap with low region
        if arr[mid] < a:
            # Example iteration:
            # If arr[mid] = 1 (<1)? no. Later arr[mid]=2 (<1)? no.
            # But initially arr[mid]=1 (first element), equals a, so not in this case.
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        # CASE 2: Current element is between [a, b] → keep it in middle region
        elif a <= arr[mid] <= b:
            # Example: arr[mid] = 1, 3, 2 all fall in this range
            # So simply move ahead
            mid += 1

        # CASE 3: Current element > b → swap with high region
        else:
            # Example: arr[mid] = 4, 6 (both >3)
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # mid is NOT incremented here because swapped item must be checked

    return True



if __name__ == '__main__':
    print(threeWayPartition([1, 2, 3, 3, 4],1,2))
    print(threeWayPartition([1, 4, 3, 6, 2, 1],1,3))