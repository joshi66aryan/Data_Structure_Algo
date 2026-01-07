# All combinations of size r from an array
# Last Updated : 20 May, 2025

# You are given an array arr[] consisting of n elements. Your task is to generate and 
# print all possible combinations of exactly r elements from this array.

# Note: A combination is a selection of items where the order does not matter. 
# Ensure that each unique group of r elements is printed only once, regardless of order.

# Example:

# Input: arr = [1, 2, 3, 4], r = 2
# Output: 1 2
#                1 3
#                1 4
#                2 3
#                2 4
#                3 4
# Explanation: We need to generate all possible combinations of size 2 from an array of size 4. 
# The total number of such combinations is given by the formula:

# 4C2 = 4! / [(4 - 2)! × 2!] = 6 combinations.

# Input: arr = [1, 2, 3, 4], r = 3
# Output: 1 2 3
#                1 2 4
#                1 3 4
#                2 3 4
# Explanation: We need to generate all possible combinations of size 3 from an array of size 4. The total number of such combinations is given by the formula:
# 4C3 = 4! / [(4 - 3)! × 3!] = 4 combinations.

def combinationUtil(arr, r, results, tempData, start, n):
    if len(tempData) == r:
        results.append(tempData.copy())
        return
    
    for i in range(start, n):
        if i > start and arr[i] == arr[i-1]:
            continue  # skip duplicates
        tempData.append(arr[i])
        # print("TempData:",tempData)
        # print("Results:",results)
        combinationUtil(arr, r, results, tempData, i + 1, n)
        tempData.pop()

def findCombination(arr, r):
    if r == 0:
        return [[]]
    sorted_arr = sorted(arr)  # avoid mutating original
    results = []
    combinationUtil(sorted_arr, r, results, [], 0, len(sorted_arr))
    return results

# Test
if __name__ == "__main__":
    res = findCombination([1, 1, 2, 3, 4], 2)
    # print("Res:",res)
    for comb in sorted(res):  # sorted for consistent display
        print(*comb)
