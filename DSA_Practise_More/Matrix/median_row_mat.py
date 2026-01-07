# Median in a row-wise sorted Matrix

# Given a row-wise sorted matrix mat[][] of size n*m, where the number 
# of rows and columns is always odd. Return the median of the matrix.

# Examples:

# Input: mat[][] = [[1, 3, 5], 
#                 [2, 6, 9], 
#                 [3, 6, 9]]
# Output: 5
# Explanation: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.

# Input: mat[][] = [[2, 4, 9],
#                 [3, 6, 7],
#                 [4, 7, 10]]
# Output: 6
# Explanation: Sorting matrix elements gives us [2, 3, 4, 4, 6, 7, 7, 9, 10]. Hence, 6 is median.

# Input: mat = [[3], [4], [8]]
# Output: 4
# Explanation: Sorting matrix elements gives us [3, 4, 8]. Hence, 4 is median.

# it can be done in naive approach, but it can also be done using priority queue.

import heapq

def median(mat):
    rows = len(mat)
    columns = len(mat[0])

    minHeap = []
    medianIndex = (rows * columns) // 2
    results = -1
    count = 0

    for i in range(rows):
        heapq.heappush(minHeap, [mat[i][0], i, 0])

    while count <= medianIndex:
        val, row, col = heapq.heappop(minHeap)
        results = val
        count += 1

        if col + 1 < columns:
            heapq.heappush(minHeap, [mat[row][col+1],row, col+1])

    return results

if __name__ == "__main__":
    mat1 = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    mat2 = [[2, 4, 9], [3,6,7], [4,7,10]]
    mat3 = [[3], [4], [10]]

    print("Mat1:",median(mat1))
    print("Mat2:", median(mat2))
    print("Mat3:", median(mat3))