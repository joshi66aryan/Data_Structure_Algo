# Merge Two Sorted Arrays Without Extra Space
# Given two sorted arrays a[] and b[] of size n and m respectively, 
# merge both the arrays and rearrange the elements such that the smallest 
# n elements are in a[] and the remaining m elements are in b[]. 
# All elements in a[] and b[] should be in sorted order.

# Examples: 

# Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
# Output: a[] = [2, 2, 3, 4], b[] = [7, 10] 
# Explanation: Combined sorted array = [2, 2, 3, 4, 7, 10], 
# array a[] contains smallest 4 elements: 2, 2, 3 and 4, 
# and array b[] contains remaining 2 elements: 7, 10.

# Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
# Output: a[] = [1, 2, 3, 5, 8, 9], b[] = [10, 13, 15, 20]
# Explanation: Combined sorted array = [1, 2, 3, 5, 8, 9, 10, 13, 15, 20],
#  array a[] contains smallest 6 elements: 1, 2, 3, 5, 8 and 9, and array b[] 
# contains remaining 4 elements: 10, 13, 15, 20.

# Input: a[] = [0, 1], b[] = [2, 3]
# Output: a[] = [0, 1], b[] = [2, 3] 
# Explanation: Combined sorted array = [0, 1, 2, 3], array a[] contains smallest 2 
# elements: 0 and 1, and array b[] contains remaining 2 elements: 2 and 3.

def merge_without_extra_pace(a,b,n,m):

    i = n-1
    j= 0 

    while i >= 0 and j < m:
        if a[i] > b[j]:
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1
        else:
            break
    
    a.sort()
    b.sort()
    return a,b
        


if __name__ == '__main__':
    a = [1, 5, 9, 10, 15, 20]
    b = [2, 3, 8, 13]
    n = len(a)
    m = len(b)

    a_final, b_final = merge_without_extra_pace(a,b,n,m)
    print('a = ',a_final, 'b_final',b_final)



# Idea (Two-pointer + swap + sort only the changed parts)

# Start with two pointers:
# i at the end of a (n-1)
# j at the beginning of b (0)

# While i >= 0 and j < m:
# If a[i] > b[j] → swap them and move both pointers.
# Else → we are done with a, break.

# After the loop, a may have some large elements at the end and b may have some small elements at the beginning.
# Sort the whole a (now contains the smallest n elements, possibly unsorted).
# Sort the whole b (contains the largest m elements).


# That’s it! No extra array needed.

# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1) extra space