# Given an array arr[] of size n, the task is to rearrange 
# it in alternate positive and negative manner without changing 
# the relative order of positive and negative numbers. 
# In case of extra positive/negative numbers, 
# they appear at the end of the array.

# Note: The rearranged array should start with a positive number 
# and 0 (zero) should be considered as a positive number.

# Examples: 

# Input:  arr[] = [1, 2, 3, -4, -1, 4]
# Output: arr[] = [1, -4, 2, -1, 3, 4]

# Input:  arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# Output: arr[] = [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]

# Python3 program to rearrange array
# in alternating positive & negative
# items with O(1) extra space

# Function to rearrange positive and
# negative integers in alternate fashion.
# The below solution does not maintain
# original order of elements




def rearrange_alternate_stable(arr):
    # Separate positive (including 0) and negative elements
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    
    # Now merge them alternately starting with positive
    i = j = k = 0
    n_pos, n_neg = len(pos), len(neg)
    
    # Alternate placement
    while i < n_pos and j < n_neg:
        arr[k] = pos[i]
        k += 1
        i += 1
        arr[k] = neg[j]
        k += 1
        j += 1

    # If extra positives remain, place them at the end
    while i < n_pos:
        arr[k] = pos[i]
        i += 1
        k += 1

    # If extra negatives remain, place them at the end
    while j < n_neg:
        arr[k] = neg[j]
        j += 1
        k += 1

    return arr


# ---------- Example ----------
arr1 = [1, 2, 3, -4, -1, 4]
print(rearrange_alternate_stable(arr1))  # [1, -4, 2, -1, 3, 4]

arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(rearrange_alternate_stable(arr2))  # [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
