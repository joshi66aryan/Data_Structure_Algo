# Next Permutation
# Difficulty: Medium
# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers 
# into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest
# possible order (i.e., sorted in ascending order). 

# Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear 
# order.

# Examples:

# Input: arr[] = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]
# Explanation: The next permutation of the given array is [2, 4, 5, 0, 1, 7].

# Input: arr[] = [3, 2, 1]
# Output: [1, 2, 3]
# Explanation: As arr[] is the last permutation, the next permutation is the lowest one.

# Input: arr[] = [3, 4, 2, 5, 1]
# Output: [3, 4, 5, 1, 2]
# Explanation: The next permutation of the given array is [3, 4, 5, 1, 2].

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105


class Solutions:
    def next_permutation(self,arr):
        n = len(arr)
        pivot = -1

        # find the pivot
        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        
        # if pivot is not there, reverse the whole array
        if pivot == -1:
            arr.reverse()
            return
        
        # find the element from the right that is greater than the pivot.
        for i in range(n-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # sort the right side
        left,right = pivot+1, n-1 
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s1 = Solutions()
    s2 = Solutions()
    s3 = Solutions()
    x,y,z = [2, 4, 1, 7, 5, 0], [3, 2, 1], [3, 4, 2, 5, 1]
    s1.next_permutation(x)
    s2.next_permutation(y)
    s3.next_permutation(z)
    print("".join(map(str,x)))
    print("".join(map(str,y)))
    print("".join(map(str,z)))