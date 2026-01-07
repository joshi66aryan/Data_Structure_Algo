
# Chocolate Distribution Problem

# Difficulty: Easy
# Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. 
# Each packet can have a variable number of chocolates. There are m students, the task is to distribute 
# chocolate packets among m students such that -

#       i. Each student gets exactly one packet.
#      ii. The difference between maximum number of chocolates given to a student 
#         and minimum number of chocolates given to a student is minimum and return 
#         that minimum possible difference.

# Examples:

# Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
# Output: 6
# Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 
#             by choosing following m packets :[3, 4, 9, 7, 9].


# Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3
# Output: 2
# Explanation: The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 
#             by choosing following m packets :[3, 2, 4].

# Input: arr = [3, 4, 1, 9, 56], m = 5
# Output: 55
# Explanation: With 5 packets for 5 students, each student will receive one packet, so the difference is 56 - 1 = 55.
        
# Constraints:
#     1 ≤ m <= arr.size ≤ 105
#     1 ≤ arr[i] ≤ 109

# Expected Complexities
#     Time Complexity: O(n log n)
#     Auxiliary Space: O(1)

def min_difference(arr,m):
    n = len(arr)
    if m > n:
        return -1
    if m == 0 or m == 1:
        return 0
    
    arr.sort()
    min_diff = arr[m-1] - arr[0]

    for x in range(1, n + 1 - m):

        curr_diff = arr[x+m-1] - arr[x]
        if curr_diff < min_diff:
            min_diff = curr_diff
    return min_diff 



if __name__ == '__main__':
    print(min_difference([3, 4, 1, 9, 56, 7, 9, 12], 5))
    print(min_difference([7, 3, 2, 4, 9, 12, 56], 3))
    print(min_difference([3, 4, 1, 9, 56], 5))