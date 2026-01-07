# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number 
# of steps you can jump forward from that position.

# For example:

# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# If arr[i] = 0, you cannot jump forward from that position.
# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

# Note:  Return -1 if you can't reach the end of the array.

# Examples : 

# Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Index:          0  1  2  3  4  5  6  7 8  9  10
# Output: 3 
# Explanation: First jump from 1st element to 2nd element with value 3. 
# From here we jump to 5th element with value 9, and from here we will jump to the last. 

# Input: arr = [1, 4, 3, 2, 6, 7]
# Output: 2 
# Explanation: First we jump from the 1st to 2nd element and then jump to the last element.

# Input: arr = [0, 10, 20]
# Output: -1
# Explanation: We cannot go anywhere from the 1st element.

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

def cal_jump(arr,n):

    if not(2 <= n <= 10**5):
        raise ValueError("\n Array size out of range. \n")
    
    if not any((0 <= x <= 10**5) for x in arr):
        raise ValueError("\n Array element is out of range. \n")
    
    if n == 0 or arr[0] == 0:
        return -1
    
    if n == 1:
        return 0
    
    maxReach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1,n):
      # if i reach the last index return jump
      if i == n-1:
          return jump
      
      # take the max reach 
      maxReach = max(maxReach, i+arr[i])

      # reduce the step just used
      step -= 1

      # if step is o make jump 
      if step == 0:
          jump += 1

          # if current index is beyond the max reachable index
          if i >= maxReach:
              return -1
          
          # reinitialize the step for the new jump
          step = maxReach - i

    return -1



if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    n = len(arr)
    ans = cal_jump(arr,n)
    print("result",ans)



# Let’s take your example:
# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# 
# 
# ┌────────────────────────────────────────────┐
# │ Start: i = 0, arr[0] = 1                  │
# │ Initialize:                                │
# │   maxReach = 1                            │
# │   step = 1                                │
# │   jump = 1                                │
# └────────────────────────────────────────────┘
#                 │
#                 ▼
#         ┌───────────────────────────┐
#         │ i = 1                     │
#         │ arr[1] = 3                │
#         │ maxReach = max(1, 1+3)=4  │
#         │ step -= 1 → step = 0      │
#         │ step == 0 → jump++ → 2    │
#         │ new step = maxReach - i   │
#         │ step = 4 - 1 = 3          │
#         └───────────────────────────┘
#                 │
#                 ▼
#         ┌───────────────────────────┐
#         │ i = 2                     │
#         │ arr[2] = 5                │
#         │ maxReach = max(4, 2+5)=7  │
#         │ step -= 1 → step = 2      │
#         └───────────────────────────┘
#                 │
#                 ▼
#         ┌───────────────────────────┐
#         │ i = 3                     │
#         │ arr[3] = 8                │
#         │ maxReach = max(7, 3+8)=11 │
#         │ step -= 1 → step = 1      │
#         └───────────────────────────┘
#                 │
#                 ▼
#         ┌───────────────────────────┐
#         │ i = 4                     │
#         │ arr[4] = 9                │
#         │ maxReach = max(11, 4+9)=13│
#         │ step -= 1 → step = 0      │
#         │ step == 0 → jump++ → 3    │
#         │ new step = maxReach - i   │
#         │ step = 13 - 4 = 9         │
#         └───────────────────────────┘
#                 │
#                 ▼
#         ┌───────────────────────────┐
#         │ i = 5 → last index = 10   │
#         │ Since maxReach (13) > 10  │
#         │ ✅ Reached end with jump=3│
#         └───────────────────────────┘



