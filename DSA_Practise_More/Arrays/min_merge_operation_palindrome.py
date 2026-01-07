# Find minimum number of merge operations to make an array palindrome

# Given an array of positive integers. We need to make the given array a 'Palindrome'. 
# The only allowed operation is"merging" (of two adjacent elements). Merging two adjacent 
# elements means replacing them with their sum. The task is to find the minimum number of
#  merge operations required to make the given array a 'Palindrome'.

# To make any array a palindrome, we can simply apply merge operation n-1 times where 
# n is the size of the array (because a single-element array is always palindromic, 
# similar to single-character string). In that case, the size of array will be reduced 
# to 1. But in this problem, we are asked to do it in the minimum number of operations.

# Example : 

# Input : arr[] = {15, 4, 15}
# Output : 0
# Array is already a palindrome. So we
# do not need any merge operation.

# Input : arr[] = {1, 4, 5, 1}
# Output : 1
# We can make given array palindrome with
# minimum one merging (merging 4 and 5 to
# make 9)

# Input : arr[] = {11, 14, 15, 99}
# Output : 3
# We need to merge all elements to make
# a palindrome.
# The expected time complexity is O(n).

def min_merge_operation_palindrome(arr):
    """
    Function to find the minimum number of merge operations required
    to make the array a palindrome.

    We use a two-pointer approach:
        - If arr[i] == arr[j] → move inward
        - If arr[i] < arr[j]  → merge left side
        - If arr[i] > arr[j]  → merge right side

    Time Complexity:  O(n)
    Space Complexity: O(1)    (modifies array in-place)
    """

    i = 0
    j = len(arr) - 1
    merges = 0

    # --- Example: arr = [1, 4, 3, 2, 5] ---
    # Initial state: i=0, j=4, merges=0
    
    # Process until pointers meet
    while i < j:

        # Case 1: Values match → already palindromic at edges
        if arr[i] == arr[j]:
            i += 1
            j -= 1
            # Iteration 1 (Example): arr[0]=1, arr[4]=5. Not equal.
            # Iteration 2 (Example): arr[0]=5, arr[4]=5. Equal.
            #   i becomes 1, j becomes 3.
            # Iteration 3 (Example): arr[1]=4, arr[3]=4. Equal.
            #   i becomes 2, j becomes 2. Loop terminates (i < j is false).

        # Case 2: Left side smaller → merge arr[i] with arr[i+1]
        elif arr[i] < arr[j]:
            # Example Iteration 1: arr[0]=1, arr[4]=5. arr[0] < arr[4]. Case 2.
            #   Merge arr[0] (1) into arr[1] (4). arr[1] becomes 1 + 4 = 5.
            arr[i + 1] += arr[i]           # merge arr[i] into arr[i+1]
            i += 1                         # merged element now at i+1
            merges += 1
            # State after merge: arr = [1, 5, 3, 2, 5], i=1, j=4, merges=1.
            #   arr[i] (5) is now the merged element. The effective comparison is now between arr[i] and arr[j].
            
            # Example Iteration 2 (after the first merge): arr[1]=5, arr[4]=5. Case 1 is met.

        # Case 3: Right side smaller → merge arr[j] with arr[j-1]
        else:
            # Example Iteration X: Not triggered in this example (1 < 5).
            arr[j - 1] += arr[j]           # merge arr[j] into arr[j-1]
            j -= 1                         # merged element now at j-1
            merges += 1
            # Example Iteration X: Let's consider if arr = [5, 4, 3, 2, 1]
            #   arr[0]=5, arr[4]=1. Case 3. arr[3] (2) becomes 2 + 1 = 3.
            #   arr = [5, 4, 3, 3, 1], i=0, j=3, merges=1.

    # Final Example: The loop terminates when i=2, j=2.
    # The final number of merges is 2.
    return merges

    

if __name__ == "__main__":
    print(f"Result1:{min_merge_operation_palindrome([15, 4, 15])}")
    print(f"Result1:{min_merge_operation_palindrome([1, 4, 5, 1])}")
    print(f"Result1:{min_merge_operation_palindrome([11, 14, 15, 99])}")





# ### 🎯 **The Algorithm's Logic**

# The two-pointer algorithm correctly calculates the minimum number of merge operations needed to reach a 
# state where the array **can be made palindromic**.

# Let's re-examine the state at the end of the trace:

# * **Final Array State (After 2 Merges):** $\text{arr} = [1, 5, 5, 2, 5]$
# * **Final Pointers:** $i=2, j=2$
# * **Total Merges:** 2

# The algorithm terminates because the pointers meet ($i \not< j$). At this point, the 
# comparison loop has ensured that **all elements to the left of the meeting point ($i$) 
# match their corresponding elements to the right of the meeting point ($j$) after potential merges**.

# ### 🌟 **What the Algorithm Achieved**

# 1.  **Original Array:** $[1, 4, 3, 2, 5]$
# 2.  **Merge 1 (Left Side):** $[1, 4] \rightarrow [5]$. Array becomes $[\mathbf{5}, 3, 2, 5]$. (Index 1 is now 5)
# 3.  **Match:** Current $\text{arr}[1]=5$ matches $\text{arr}[4]=5$. Pointers move inward. Array is $\text{arr}[1:4] = [5, 3, 2]$.
# 4.  **Merge 2 (Right Side):** Current $\text{arr}[3]=2$. $\text{arr}[2]=3$. $\text{arr}[3] < \text{arr}[2]$. 
# Merge $\text{arr}[3]=2$ into $\text{arr}[2]=3$. $\text{arr}[2]$ becomes $\mathbf{5}$. Array is $[\mathbf{5}, \mathbf{5}, \mathbf{2}]$. (Index 2 is now 5)

# The final resulting "effective" array that is checked by the loop is $[5, 5]$. The elements being compared are:

# * $\text{Original } \text{arr}[0]$ merged with $\text{Original } \text{arr}[1] \rightarrow 5$. This matches $\text{Original } \text{arr}[4] \rightarrow 5$.
# * $\text{Original } \text{arr}[2]$ merged with $\text{Original } \text{arr}[3] \rightarrow 5$. This is the single middle element.

# The array $[1, 4, 3, 2, 5]$ can be reduced to the palindromic array $[5, 5, 5]$ in 2 merges:

# 1.  Merge $1$ and $4 \rightarrow \mathbf{5}$. Array is $[5, 3, 2, 5]$.
# 2.  Merge $3$ and $2 \rightarrow \mathbf{5}$. Array is $[5, 5, 5]$. **This is a palindrome.**

# The code correctly determines that **2** is the minimum number of operations required, even if the intermediate state 
# $\mathbf{[1, 5, 5, 2, 5]}$ produced by the in-place modification is not the final palindromic array.
