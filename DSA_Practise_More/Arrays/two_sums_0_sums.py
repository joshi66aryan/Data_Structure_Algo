# Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

# Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

# Examples:

# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]

# Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
# arr[2] + arr[4] = 1 + (-1) = 0.
# The distinct pair are [-1,1].


# Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# Output: [[-6, 6],[-1, 1]]

# Explanation: The distinct pairs are [-1, 1] and [-6, 6].
# Expected Time Complexity: O(n log n)
# Expected Auxiliary Space: O(n).

# Constraints:
# 3 <= arr.size <= 105
# -105 <= arr[i] <= 105

def getPairs(arr,n):
    arr.sort()
    results = []
    i,j = 0, n-1

    while i<j:
        sumA  = arr[i]+arr[j]

        if sumA == 0:
            results.append([arr[i],arr[j]])
            i += 1
            j -= 1

            # remove duplicate
            while i<j and arr[i] == arr[i-1]:
                i+=1
            while i<j and arr[j] == arr[j+1]:
                j-=1


        elif sumA < 0:
            i+=1
        else:
            j-=1
    return results




if __name__ == '__main__':
    arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
    n = len(arr)
    ans = getPairs(arr,n)
    print("Result:",ans)