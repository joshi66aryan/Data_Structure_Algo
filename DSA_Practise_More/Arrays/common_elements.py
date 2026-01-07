# Given three sorted arrays in non-decreasing order, print all common elements 
# in non-decreasing order across these arrays. If there are no such elements 
# return an empty array. In this case, the output will be -1.

# Note: can you handle the duplicates without using any additional Data Structure?

# Examples :
# Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output: [20, 80]
# Explanation: 20 and 80 are the only common elements in arr1, arr2 and arr3.

# Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
# Output: [-1]
# Explanation: There are no common elements in arr1, arr2 and arr3.

# Input: arr1 = [1, 1, 1, 2, 2, 2], arr2 = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
# Output: [1, 2]
# Explanation: We do not need to consider duplicates

# Constraints:
# 1 <= arr1.size(), arr2.size(), arr3.size() <= 105
# -105 <= arr1i , arr2i , 1arr3i <= 105

def common_element(arrA, arrB, arrC):
    n1,n2,n3 = len(arrA), len(arrB), len(arrC)
    i,j,k = 0,0,0
    results = []

    while i < n1 and j < n2 and k < n3:
        if arrA[i] == arrB[j] == arrC[k]:
            results.append(arrA[i])

            val = arrA[i]
            while  i < n1 and arrA[i] == val:
                i+=1
            while j < n2 and arrB[j] == val:
                j+=1
            while k < n3 and arrC[k] == val:
                k+=1
        elif arrA[i] < arrB[j] or arrA[i] < arrC[k]:
            i+=1
        elif arrB[j] < arrA[i] or arrB[j] < arrC[k]:
            j+=1
        else:
            k+=1
    return results if results else [-1] 

if __name__ == '__main__':
    arrA, arrB, arrC = [1, 5, 10, 20, 40, 80] ,  [6, 7, 20, 80, 100] ,  [3, 4, 15, 20, 30, 70, 80, 120]
    ans =  common_element(arrA, arrB, arrC)
    print("Result:",ans)
    