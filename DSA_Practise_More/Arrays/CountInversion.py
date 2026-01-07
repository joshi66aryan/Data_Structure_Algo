# Given an array of integers arr[]. You have to find the Inversion Count of the array. 
# Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

# Examples:

# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

# Input: arr[] = [2, 3, 4, 5, 6]
# Output: 0
# Explanation: As the sequence is already sorted so there is no inversion count.

# Input: arr[] = [10, 10, 10]
# Output: 0
# Explanation: As all the elements of array are same, so there is no inversion count.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 104

def merge(arr, temp, left, mid, right):
    """
    Merge two sorted halves and count inversions during the process.
    An inversion occurs when we pick an element from right half before left half.
    """
    i = left          # Pointer for left subarray
    j = mid + 1       # Pointer for right subarray
    k = left          # Pointer for temp array
    inv_count = 0     # Count of inversions in this merge step

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            # No inversion, take from left
            temp[k] = arr[i]
            i += 1
        else:
            # Inversion! arr[i] > arr[j], and since left half is sorted,
            # all elements from i to mid are greater than arr[j]
            temp[k] = arr[j]
            inv_count += (mid - i + 1)   # Key: Count all remaining in left
            j += 1
        k += 1

    # Copy remaining elements from left half (if any)
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    # Copy remaining elements from right half (if any)
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    # Copy merged result back to original array
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return inv_count


def mergeSort(arr, temp, left, right):
    """
    Recursively divide array and merge while counting inversions
    """
    inv_count = 0
    if left < right:  # Base case: only when subarray has 2+ elements
        mid = (left + right) // 2

        # Count inversions in left half
        inv_count += mergeSort(arr, temp, left, mid)
        
        # Count inversions in right half
        inv_count += mergeSort(arr, temp, mid + 1, right)
        
        # Count split inversions (across both halves)
        inv_count += merge(arr, temp, left, mid, right)

    return inv_count


def countInversions(arr):
    """
    Main function to count total inversions in the array
    Time Complexity : O(n log n)  -> Same as merge sort
    Space Complexity: O(n)        -> For temporary array during merge
    """
    n = len(arr)
    temp = [0] * n                    # Temporary array for merging
    return mergeSort(arr, temp, 0, n - 1)    


if __name__ == '__main__':
    arr = [2, 4, 1, 3, 5]
    ans = countInversions(arr)
    print("result", ans)



# Time Complexity: O(n log n)

# We divide the array into two halves → log n levels
# At each level, we do O(n) work in merge step
# Total = n × log n

# Space Complexity: O(n)

# We use a temporary array temp of size n
# Recursion depth is log n → O(log n) stack space
# Dominant space → O(n)