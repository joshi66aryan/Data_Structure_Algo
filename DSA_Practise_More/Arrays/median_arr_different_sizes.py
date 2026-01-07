# Median of two Sorted Arrays of Different Sizes

# Given two sorted arrays, a[] and b[], find the median of these sorted arrays. 
# Assume that the two sorted arrays are merged and then median is selected from 
# the combined array.

# This is an extension of Median of two sorted arrays of equal size problem. 
# Here we handle arrays of unequal size also.

# Examples: 

# Input: a[] = [-5, 3, 6, 12, 15], b[] = [-12, -10, -6, -3, 4, 10]
# Output: 3

# Explanation: 
# The merged array is [-12, -10, -6, -5 , -3, 3, 4, 6, 10, 12, 15]. 
# So the median of the merged array is 3.

# Input: a[] = [1], b[] = [2, 4, 5, 6, 7]
# Output: 4.5
# Explanation: 
# The merged array is [1, 2, 4, 5, 6, 7]. The total number of elements are even, 
# so there are two middle elements. Take the average between the two: (4 + 5) / 2 = 4.5

def median_diff_sizes(a, b):
    if not (a and b):
        return 0
    
    c = a + b
    c.sort()

    n = len(c)

    if n % 2 == 0: 
        x =  n // 2
        return (c[x-1] + c[x]) / 2
    else:
        x = (n+1)//2
        return c[x-1]
    

    


if __name__ == "__main__":
    a1, b1  = [-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]
    a2, b2 = [1], [2, 4, 5, 6, 7]

    print(f"The result1: {median_diff_sizes(a1,b1)}")
    print(f"The result1: {median_diff_sizes(a2,b2)}")