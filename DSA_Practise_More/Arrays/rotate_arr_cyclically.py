# Given an array arr, rotate the array by one position in clockwise direction.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

# Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
# Output: [3, 9, 8, 7, 6, 4, 2, 1]
# Explanation: After rotating clock-wise 3 comes in first position.


# Constraints:
# 1<=arr.size()<=10**5
# 0<=arr[i]<=10**5

def rotate_arr(arr,n):
    if not(1 <= n <=10**5):
        raise ValueError("\n Out of range constraint. \n")
    
    if not any((0 <= x <= 10**5 ) for x in arr):
        raise ValueError("\n Element exceed the constraint.\n") 
    
    last_element = arr[-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last_element 
    return arr
    


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = len(arr) 
    res = rotate_arr(arr, n)
    print("answer",res)

