# Product of Array Except Self
# Medium


# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the 
# product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

def productExceptSelf(nums):
    """
    Calculates the product of all elements of nums except nums[i] for each index i.
    The algorithm runs in O(n) time and O(1) extra space (excluding the output array).
    
    Example Trace: nums = [1, 2, 3, 4]
    """
    n = len(nums)
    # Initialize the answer array with 1s. This array will store the final result.
    # It meets the O(1) extra space constraint as the output array is not counted.
    # answer = [1, 1, 1, 1]
    answer = [1] * n

    # --- PASS 1: Calculate Left/Prefix Products ---
    # At the end of this pass, answer[i] will contain the product of all elements 
    # to the left of index i.
    prefix_product = 1  # Initialize the running product of elements to the left (prefix)
                        # prefix_product = 1
    
    for i in range(n):
        # 1. Set answer[i] to the running prefix product (product of elements before nums[i])
        # i=0: answer[0] = 1 (Product to the left of 1 is 1) | answer = [1, 1, 1, 1]
        # i=1: answer[1] = 1 (Product to the left of 2 is 1) | answer = [1, 1, 1, 1]
        # i=2: answer[2] = 2 (Product to the left of 3 is 1*2) | answer = [1, 1, 2, 1]
        # i=3: answer[3] = 6 (Product to the left of 4 is 1*2*3) | answer = [1, 1, 2, 6]
        answer[i] = prefix_product
        
        # 2. Update the prefix product for the next iteration by including the current number
        # i=0: prefix_product = 1 * 1 = 1
        # i=1: prefix_product = 1 * 2 = 2
        # i=2: prefix_product = 2 * 3 = 6
        # i=3: prefix_product = 6 * 4 = 24
        prefix_product *= nums[i]

    # answer after Pass 1: [1, 1, 2, 6]

    # --- PASS 2: Calculate Right/Suffix Products and Finalize Result ---
    # We iterate backwards and multiply answer[i] (which has the Left Product) by the 
    # running suffix product (the Right Product).
    suffix_product = 1  # Initialize the running product of elements to the right (suffix)
                        # suffix_product = 1

    # Iterate from the last index down to 0
    for i in range(n - 1, -1, -1):
        # 1. Update answer[i] by multiplying the existing Left Product with the current Right Product
        # i=3: answer[3] = 6 * 1 = 6  | answer = [1, 1, 2, 6]
        # i=2: answer[2] = 2 * 4 = 8  | answer = [1, 1, 8, 6]
        # i=1: answer[1] = 1 * 12 = 12 | answer = [1, 12, 8, 6]
        # i=0: answer[0] = 1 * 24 = 24 | answer = [24, 12, 8, 6]
        answer[i] *= suffix_product
        
        # 2. Update the suffix product for the next iteration by including the current number
        # i=3: suffix_product = 1 * 4 = 4
        # i=2: suffix_product = 4 * 3 = 12
        # i=1: suffix_product = 12 * 2 = 24
        # i=0: suffix_product = 24 * 1 = 24
        suffix_product *= nums[i]
        
    return answer

# Time Complexity: O(n) (Two passes over the array)
# Space Complexity: O(1) (Excluding the output array)

# Example Usage:
# nums_1 = [1, 2, 3, 4]
# result_1 = productExceptSelf(nums_1) # [24, 12, 8, 6]

# nums_2 = [-1, 1, 0, -3, 3]
# result_2 = productExceptSelf(nums_2) # [0





if  __name__ == "__main__":
    print(f"Result1:{productExceptSelf([1,2,3,4])}")
    print(f"Result1:{productExceptSelf([-1,1,0,-3,3])}")


# ### The Big Idea: The Missing Piece

# Think of the product we need to find for any friend (index $i$) as a puzzle.

# For the friend at index $i$, their required product must include every number *except* the one they are holding.

# $$\text{Required Product} = \text{All numbers before } i \times \text{All numbers after } i$$



# Our two passes are just two easy ways to calculate these two sides of the product puzzle, and then we multiply them together.

# ---

# ### Pass 1: Finding the Left Half (The Prefix Score)

# In this pass, we are only concerned with building the "Left Product." We walk from left to right, and for each position, we record the total product accumulated so far.

# **Example: `nums = [1, 2, 3, 4]`**

# We use the `answer` array to store this Left Product. We start with a `Left Product running total` of $\mathbf{1}$.

# | Index (i) | Value $\text{nums}[i]$ | `Left Product running total` (Stored Here) | Action | `answer` Array | **What `answer[i]` has:** |
# | :-------: | :--------------------: | :---------------------------------------: | :----: | :------------: | :------------------------: |
# | 0 | 1 | **1** | $\text{answer}[0] = 1$. Then, new total: $1 \times 1 = 1$ | **[1,** 1, 1, 1] | Product to the left of 1 ($\emptyset$) |
# | 1 | 2 | **1** | $\text{answer}[1] = 1$. Then, new total: $1 \times 2 = 2$ | [1, **1,** 1, 1] | Product to the left of 2 (just 1) |
# | 2 | 3 | **2** | $\text{answer}[2] = 2$. Then, new total: $2 \times 3 = 6$ | [1, 1, **2,** 1] | Product to the left of 3 ($1 \times 2$) |
# | 3 | 4 | **6** | $\text{answer}[3] = 6$. Then, new total: $6 \times 4 = 24$ | [1, 1, 2, **6**] | Product to the left of 4 ($1 \times 2 \times 3$) |

# **End of Pass 1:** The `answer` array holds only the **LEFT SIDE** of the product for every single index: $[1, 1, 2, 6]$.

# ---

# ### Pass 2: Finding the Right Half and Finishing the Puzzle

# Now, we need the "Right Product" (or Suffix Product). We iterate backward from right to left, and we keep a separate `Right Product running total`.

# At each index $i$, the `answer[i]` already has the Left Product. We just need to multiply it by the Right Product we are currently calculating!

# **Example: `nums = [1, 2, 3, 4]` (Starting from `answer = [1, 1, 2, 6]`)**

# We start with a `Right Product running total` of $\mathbf{1}$.

# | Index (i) | Value $\text{nums}[i]$ | `Right Product running total` (Stored Here) | Action | `answer` Array (Final) | **Full Product:** |
# | :-------: | :--------------------: | :---------------------------------------: | :----: | :---------------------: | :---------------------------------: |
# | 3 | 4 | **1** | $\text{answer}[3] = 6 \times 1 = 6$. New total: $1 \times 4 = 4$ | [1, 1, 2, **6**] | $\text{Left}(6) \times \text{Right}(1)$ |
# | 2 | 3 | **4** | $\text{answer}[2] = 2 \times 4 = 8$. New total: $4 \times 3 = 12$ | [1, 1, **8**, 6] | $\text{Left}(2) \times \text{Right}(4)$ |
# | 1 | 2 | **12** | $\text{answer}[1] = 1 \times 12 = 12$. New total: $12 \times 2 = 24$ | [1, **12**, 8, 6] | $\text{Left}(1) \times \text{Right}(12)$ |
# | 0 | 1 | **24** | $\text{answer}[0] = 1 \times 24 = 24$. New total: $24 \times 1 = 24$ | [**24**, 12, 8, 6] | $\text{Left}(1) \times \text{Right}(24)$ |

# ### Summary of the "Aha!" Moment

# We never calculated the total product of the entire array. We only calculated:

# 1.  **Left Products** (Pass 1)
# 2.  **Right Products** (Pass 2, done simultaneously with multiplication)

# By multiplying these two pieces together, we automatically get the product of everything *except* the number at that index. Because we did this using two simple walks through the array, the time taken is only $O(n)$, which is super fast!