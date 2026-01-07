# There are many situations where we use integer values as index in array to see 
# presence or absence, we can use bit manipulations to optimize space in such problems.
# Let us consider below problem as an example.
# Given two numbers say a and b, mark the multiples of 2 and 5 between a and b using 
# less than O(|b - a|) space and output each of the multiples. 

# Note : We have to mark the multiples i.e save (key, value) pairs in memory such 
# that each key either have value as 1 or 0 representing as multiple of 2 or 5 or not respectively. 

# Examples :  

# Input : 2 10
# Output : 2 4 5 6 8 10

# Input: 60 95
# Output: 60 62 64 65 66 68 70 72 74 75 76 78 
#         80 82 84 85 86 88 90 92 94 95

import math

# Function to check if a particular bit is set (1) or not (0)
def checkBit(array, index):

    # index >> 5 → divides index by 32 → selects which integer in the array (array[0], array[1], etc.)
    # Example: index=8 → 8>>5 = 0 → look in array[0]
    int_index = index >> 5

    # index & 31 → finds position of bit inside that integer (0 to 31)
    # Example: index=8 → 8&31 = 8 → check the 8th bit
    bit_position = index & 31

    # (1 << (index & 31)) → creates a mask with only that one bit set to 1
    # Example: 1 << 8 = 256 (binary: 100000000)
    bit_mask = 1 << bit_position

    # Performs AND: if the bit is set, result is non-zero (truthy); otherwise 0 (falsy)
    # Example: if bit 8 is set → 349 & 256 = 256 → truthy → bit is set
    return array[int_index] & bit_mask

def setBit(array, index):
    # Same logic: find which integer and which bit position
    # Example: index=3 → array[0] and bit 3 (mask = 1<<3 = 8)


    int_index = index >> 5
    bit_position = index & 31
    bit_mask = 1 << bit_position
    
    # |= means: OR the current value with the mask and store back
    # This turns ON only the desired bit, leaves all other bits unchanged
    # Example: array[0] was 5 (binary ...0101), set bit 3 → becomes 13 (binary ...1101)
    array[int_index] |= bit_mask

def space_optimization_bit_manipulation(arr):

    # Total numbers in the range [a, b]  inclusive
    n = arr[1] - arr[0] + 1       # Example: 10 - 2 + 1 = 9 numbers (2 to 10)

    # Calculate how many 32-bit integers are needed to store n bits 
    size = math.ceil(n/32)        # Example: ceil(9 / 32) = ceil(0.281) = 1 → need 1 integer

    # Create the bit array filled with zeros
    bitArray = [0] * size          # Example: array = [0] → one integer with all 32 bits as 0

    # First pass: Mark all multiples of 2 or 5 in the bit array
    for num in range(arr[0],arr[1]+1):      # Loop through every number from 2 to 10
        # Convert actual number to 0-based index in our bit array
        index = num - arr[0]                # Example: num=2 → index=0, num=10 → index=8
        if num % 2 == 0 or num % 5 == 0:    # Check if number is divisible by 2 OR by 5
            # Examples that pass:
            # 2 → 2%2==0 → True
            # 4 → 4%2==0 → True
            # 5 → 5%5==0 → True
            # 6 → 6%2==0 → True
            # 8 → 8%2==0 → True
            # 10 → 10%2==0 and 10%5==0 → True
            setBit(bitArray, index)         # Mark this position by setting the bit to 1

    print("\n Multiple of 2 and 5 are:")

    for num in range(arr[0], arr[1]+1):
        index = num - arr[0]
        # If bit is 1 → this number is a multiple of 2 or 5
        # Examples: indices 0,2,3,4,6,8 are set → corresponds to 2,4,5,6,8,10
        if checkBit(bitArray, index):
            print(num, end = " ")
                




if __name__ == '__main__':
    space_optimization_bit_manipulation([2,10])
    space_optimization_bit_manipulation([60,95])




### Why Bit Masking is Done?

# Bit masking is used in this code for **extreme space optimization**.

# Normally, to mark whether each number in a range [a, b] is a multiple of 2 or 5, you might use:

# - A boolean array: `flags = [False] * (b - a + 1)` → each `False/True` takes **1 byte** (8 bits) in memory.
# - For range 2 to 10 (9 numbers): 9 bytes.
# - For a large range like 1 to 1,000,000: ~1 MB just for flags!

# But with **bit masking**, we store **one bit per number** instead of one byte:

# - 1 bit = 1/8th of a byte → **8 times less memory**.
# - We pack 32 bits into one integer (since Python integers are at least 32-bit effectively for bit operations).
# - So, one integer in the `array` can store flags for **32 numbers**.
# - For 9 numbers → need only 1 integer (32 bits, using just 9 of them).
# - For 1,000,000 numbers → need only ~31,250 integers (~125 KB instead of 1 MB).

# **Purpose of bit masking:**
# - Save memory when you only need to store **yes/no** (presence/absence) for many items.
# - Common in competitive programming, sieves (like Sieve of Eratosthenes), and memory-constrained problems.

# ### What Does the `array` Look Like?

# Let’s take the example: **a = 2, b = 10**

# - Numbers: 2, 3, 4, 5, 6, 7, 8, 9, 10 → 9 numbers
# - n = 9
# - size = ceil(9/32) = 1 → `array = [0]` initially
# - Each bit in `array[0]` represents one number:
#   - Bit 0 → number 2
#   - Bit 1 → number 3
#   - Bit 2 → number 4
#   - Bit 3 → number 5
#   - ...
#   - Bit 8 → number 10

# After marking multiples of 2 or 5 (2,4,5,6,8,10), the bits that get set are:
# - Index 0 (num 2) → bit 0
# - Index 2 (num 4) → bit 2
# - Index 3 (num 5) → bit 3
# - Index 4 (num 6) → bit 4
# - Index 6 (num 8) → bit 6
# - Index 8 (num 10) → bit 8

# So final value of `array[0]` becomes a number whose binary representation has 1s only in those positions.

# #### Final state of the array:

# ```python
# array = [349]
# ```

# #### Binary representation of 349 (lower 9 bits shown):

# | Bit Position | 8   | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
# |--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
# | Value (1/0)  | 1   | 0   | 1   | 0   | 1   | 1   | 1   | 0   | 1   |
# | Number       | 10  | 9   | 8   | 7   | 6   | 5   | 4   | 3   | 2   |
# | Marked?      | Yes | No  | Yes | No  | Yes | Yes | Yes | No  | Yes |

# Binary: `1 0 1 0 1 1 1 0 1` → which is **349** in decimal.

# #### Visual breakdown of how 349 is built:

# | Number | Index | Bit Set | Mask (1 << index) | array[0] after |= |
# |--------|-------|---------|-------------------|-------------------|
# | Start  | -     | -       | -                 | 0                 |
# | 2      | 0     | bit 0   | 1                 | 1                 |
# | 4      | 2     | bit 2   | 4                 | 5                 |
# | 5      | 3     | bit 3   | 8                 | 13                |
# | 6      | 4     | bit 4   | 16                | 29                |
# | 8      | 6     | bit 6   | 64                | 93                |
# | 10     | 8     | bit 8   | 256               | **349**           |

# So the **entire array** is just: `[349]`

# → One single integer holds information about **all 9 numbers**!

# ### Summary

# - **Why bit mask?** → To reduce memory usage dramatically (1 bit per item instead of 1 byte or more).
# - **What does the array look like?** → A small list of integers (here just one: `[349]`), where each bit in those integers acts like a tiny flag (0 = not multiple, 1 = multiple).
# - This is a classic space-optimization technique using **bit manipulation**.

# You’re essentially turning a bunch of yes/no flags into a compact binary representation — very efficient!