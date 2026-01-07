# Median of an Array
# Difficulty: Basic
# Given an array arr[] of integers, calculate the median.

# Examples:

# Input: arr[] = [90, 100, 78, 89, 67] --> [67,78,89,,90,100]
# Output: 89
# Explanation: After sorting the array middle element is the median 

# Input: arr[] = [56, 67, 30, 79]
# Output: 61.5
# Explanation: In case of even number of elements, average of two middle elements is the median. 

# Input: arr[] = [1, 2]
# Output: 1.5
# Explanation: The average of both elements will result in 1.5.

# Constraints:
    # 1 <= arr.size() <= 105
    # 1 <= arr[i] <= 105

# Expected Complexities
    # Time Complexity: O(n log n)
    # Auxiliary Space: O(1)

def median_array(arr):
    n = len(arr)
    arr.sort()

    if n % 2 == 0:
        y = (n//2)
        avg = (arr[y-1] + arr[y]) / 2
        return avg
    else:

        x = ((n+1)//2) - 1
        return arr[x]

if __name__ == "__main__":
    arr1 = [90, 100, 78, 89, 67]
    arr2 = [56, 67, 30, 79]
    arr3 = [1, 2]

    print(f"the result of array1: {median_array(arr1)}")
    print(f"the result of array2: {median_array(arr2)}")
    print(f"the result of array3: {median_array(arr3)}")