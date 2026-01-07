# Given an array containing both positive and negative numbers in random order. 
# The task is to rearrange the array elements so that all negative numbers appear before all positive numbers.

# Note:
# Given array does not contain any zeroes.
# Order of resultant array does not matter.

# Example : 

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5




def move(arr,n):
    i = 0
    for j in range(n):
        if arr[j] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    return arr

if __name__ == '__main__':
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    n = len(arr)
    result = move(arr,n)
    print("answer",result) 