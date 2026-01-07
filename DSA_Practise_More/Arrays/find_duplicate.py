
# Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.


# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

def find_duplicate(arr,n):
    if not(1 <= n <= 10**5):
        raise ValueError("\n Array size out of range. \n")
    
    if not any((1 <= x <= n) for x in arr):
        raise ValueError("\n Array element out of range. \n")
    
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    slow = arr[0]
    while slow!= fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow






if __name__ == '__main__':
    arr = [3,1,3,4,2]
    n = len(arr)
    ans = find_duplicate(arr,n)
    print('result',ans)



# Find the Duplicate Number
# Floyd’s Tortoise and Hare (SUPER EASY!)

# Example: nums = [1, 3, 4, 2, 2]
#          index   0  1  2  3  4
#                  ↓  ↓  ↓  ↓  ↓
#                → 1 → 3 → 4 → 2 → 2 ←
#                            ↑     ↑
#                            ├─────┘
#                         Two arrows point here
#                              DUPLICATE = 2

# Think of it like a chain:
# 0 points to 1 → 1 points to 3 → 3 points to 2 → 2 points to 4 → 4 points to 2
# So: 0 → 1 → 3 → 2 → 4 → 2 → 4 → 2 → 4 → 2 → ...
#                       ↑_____________↑
#                            LOOP!

# Because of the duplicate (2 appears twice), there is a loop.

# STEP 1: Find anyone inside the loop
# Use two pointers:
# - Tortoise = moves 1 step
# - Hare     = moves 2 steps

# Start:
# Tortoise at 0 → 1
# Hare     at 0 → 1 → 3

# Next:
# Tortoise → 3
# Hare     → 2 → 4

# Next:
# Tortoise → 2
# Hare     → 2 → 2

# MEET! Both at 2

# Tortoise and Hare meet at value 2

# STEP 2: Find the START of the loop (the duplicate!)

# Now:
# - Put one pointer back to start (index 0)
# - Keep the other at meeting point (2)
# - Move BOTH one step at a time

# Start:
# Pointer A → 0 → 1
# Pointer B → 2

# Next:
# A → 3
# B → 4

# Next:
# A → 2
# B → 2

# MEET AGAIN at 2 → This is the duplicate!

# Final Answer = 2

# BEAUTIFUL VISUAL SUMMARY

#     0 → 1 → 3 → 2 → 4 → 2 → 4 → 2 → 4 → 2 ...
#               ↑               ↑
#               └───────────────┘
#                     LOOP

#     Tortoise and Hare meet here
#                 ↓
#             [inside loop]

#     Reset one pointer → move together
#                 ↓
#         They meet again here → DUPLICATE!


