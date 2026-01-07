# Given an array arr[] denoting heights of n towers and a positive integer k.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by k
# Decrease the height of the tower by k
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.

# Examples :

# Input: k = 2, arr[] = [1, 5, 8, 10]
# Output: 5
# Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference between the largest and the smallest is 8-3 = 5.

# Input: k = 3, arr[] = [3, 9, 12, 16, 20]
# Output: 11
# Explanation: The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17-6 = 11. 

# Constraints
# 1 ≤ k ≤ 107
# 1 ≤ n ≤ 105
# 1 ≤ arr[i] ≤ 107

def minimize_height(arr, k, n):

    if not(1 <= k <= 10**7):
        raise ValueError("K out of range.\n")
    
    if not(1 <= n <= 10**5):
        raise ValueError("n out of range.\n")
    
    if not any((1 <= arr[i] <= 10**7) for i in range(n)):
        raise ValueError("Element out of range.\n")
    

    if n <= 1:
        return 0
    
    arr.sort()  # Step 1: Sort the array → [1,5,8,10]
    # Time: O(n log n)

    # Initial worst-case difference (if we do nothing smart)
    result = arr[-1] - arr[0]  # e.g., 10 - 1 = 9

    # Try every possible "split point" i
    # Meaning: We increase all towers BEFORE i, and decrease all towers FROM i onwards

    for i in range(n):

        # We can only decrease arr[i] if arr[i] - k >= 0
        
        if arr[i] < k:
            continue  # cannot decrease this tower → skip this split

        # Now imagine:
        # → Towers 0 to i-1: we ADD k  → become arr[0]+k, arr[1]+k, ..., arr[i-1]+k
        # → Towers i to n-1: we SUBTRACT k → become arr[i]-k, arr[i+1]-k, ..., arr[n-1]-k

        # So the new heights will be:
        #   [arr[0]+k, arr[1]+k, ..., arr[i-1]+k, arr[i]-k, ..., arr[n-1]-k]

        # Now find the maximum and minimum in this new modified array

        # MAX height in modified array will be the larger of:
        #   - the largest decreased tower: arr[n-1] - k
        #   - the largest increased tower: arr[i-1] + k

        high = max(arr[n-1] - k, arr[i-1] + k)

        # Why? Because all towers >= i are decreased → max is arr[n-1]-k
        #       all towers < i are increased → max is arr[i-1]+k

        # MIN height in modified array will be the smaller of:
        #   - the smallest increased tower: arr[0] + k
        #   - the smallest decreased tower: arr[i] - k

        low = min(arr[0] + k, arr[i] - k)

        # Why? Smallest increased is arr[0]+k
        #       Smallest decreased is arr[i]-k (since array is sorted)

        # Now the difference for this split is high - low
        # We want the minimum possible difference

        result = min(result, high - low)

    return result

    # Time Complexity : O(n log n)  → due to sorting
    # Space Complexity : O(1)       → only using a few variables
    

        


if __name__ == '__main__':
    arr = [3, 9, 12, 16, 20]
    n = len(arr) 
    k = 3

    x = minimize_height(arr, k, n)
    print("result = ", x)