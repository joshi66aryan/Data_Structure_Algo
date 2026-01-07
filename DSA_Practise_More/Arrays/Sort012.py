# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.
# Dutch National Flag

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.
# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# Constraints:
# 1 ≤ arr.size() ≤ 10^6
# 0 ≤ arr[i] ≤ 2


# <--------------------------------------------------------------------------------------------------------------------->
# My attempt:

# def Sort012(arr):
#     n = len(arr)                                        # O(1)
#     if n<1 or n>10^6:                                   # O(1)
#         raise ValueError("\n Index out of range \n")
    
#     for i in range(0,n):                                # O(n^2)
#         for j in range(i+1,n):                          # O(n)
#             if  arr[i] < 0 or arr[i] > 2:               # O(1)
#                 raise ValueError("\n Value of an array out of range 0 to 2 \n")
#             if arr[i] >  arr[j]:                        # O(1)
#                 arr[i], arr[j] = arr[j], arr[i]         # O(1)
#             j = j+1                                     # O(1)
#     return arr



# if __name__ == '__main__':
#     arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
#     result = Sort012(arr)
#     print("Answer:",result)


# <--------------------------------------------------------------------------------------------------------------------->

# chat gpt's attempt:

# We can maintain three regions:
    # low → boundary for 0s
    # mid → current element being examined
    # high → boundary for 2s

# We iterate once:
    # If arr[mid] == 0 → swap arr[low] and arr[mid]; increment both low and mid
    # If arr[mid] == 1 → just increment mid
    # If arr[mid] == 2 → swap arr[mid] and arr[high]; decrement high

# This way:
    # Left of low → all 0s
    # Between low and mid → all 1s
    # Right of high → all 2s

def Sort012(arr):
    low, mid, high = 0,0,len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: # arr[mid] == 2
            arr[mid],arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(Sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))




# <--------------------------------------------------------------------------------------------------------------------->


# | Metric                          | Your Code               | Dutch National Flag        |
# | ------------------------------- | ----------------------- | -------------------------- |
# | **Time Complexity**             | O(n²)                   | O(n)                       |
# | **Space Complexity**            | O(1)                    | O(1)                       |
# | **Speed on 1,000,000 elements** | ❌ Very slow (~10¹² ops) | ✅ Instant (~10⁶ ops)       |
# | **Best for**                    | Small arrays            | Large arrays               |
# | **Algorithmic Idea**            | Compare every pair      | Partition using 3 pointers |


# Takeaway:
    # Your code is correct functionally, but inefficient for large input sizes (n up to 10⁶).
    # The Dutch National Flag algorithm is optimized specifically for {0,1,2} arrays — giving O(n) one-pass performance with constant memory.